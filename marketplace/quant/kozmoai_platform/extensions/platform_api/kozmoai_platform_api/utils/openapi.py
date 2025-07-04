"""OpenAPI parsing Utils."""

from typing import Optional

from kozmoai_core.provider.utils.helpers import to_snake_case

TO_CAPS_STRINGS = [
    "Pe",
    "Peg",
    "Sloos",
    "Eps",
    "Ebit",
    "Ebitda",
    "Otc",
    "Cpi",
    "Pce",
    "Gdp",
    "Lbma",
    "Ipo",
    "Nbbo",
    "Ameribor",
    "Sonia",
    "Effr",
    "Sofr",
    "Iorb",
    "Estr",
    "Ecb",
    "Dpcredit",
    "Tcm",
    "Us",
    "Ice",
    "Bofa",
    "Hqm",
    "Sp500",
    "Sec",
    "Cftc",
    "Cot",
    "Etf",
    "Eu",
    "Tips",
    "Rss",
    "Sic",
    "Cik",
    "Bls",
    "Fred",
    "Cusip",
    "Ttm",
    "Id",
    "Ytd",
    "Yoy",
    "Dte",
    "Url",
    "Sedol",
    "Isin",
    "Figi",
    "Cusip",
    "Pdf",
]


def extract_providers(params: list[dict]) -> list[str]:
    """
    Extract provider options from parameters.

    Parameters
    ----------
    params : List[Dict]
        List of parameter dictionaries.

    Returns
    -------
    List[str]
        List of provider options.
    """
    provider_params = [p for p in params if p["name"] == "provider"]
    if provider_params:
        if provider_params[0].get("schema", {}).get("enum"):
            return provider_params[0]["schema"]["enum"]
        if provider_params[0].get("schema", {}).get("default"):
            return [str(provider_params[0]["schema"]["default"])]
    return []


def set_parameter_type(p: dict, p_schema: dict):
    """
    Determine and set the type for the parameter.

    Parameters
    ----------
    p : Dict
        Processed parameter dictionary.
    p_schema : Dict
        Schema dictionary for the parameter.
    """
    p_type = p_schema.get("type") if not p.get("type") else p.get("type")

    if p_type == "string":
        p["type"] = "text"

    if p_type in ("float", "integer") or (
        not isinstance(p["value"], bool) and isinstance(p["value"], (int, float))
    ):
        p["type"] = "number"

    if (
        p_type == "boolean"
        or p_schema.get("type") == "boolean"
        or ("anyOf" in p_schema and p_schema["anyOf"][0].get("type") == "boolean")
    ):
        p["type"] = "boolean"

    if "date" in p["parameter_name"]:
        p["type"] = "date"

    if "timeframe" in p["parameter_name"]:
        p["type"] = "text"

    if p["parameter_name"] == "limit":
        p["type"] = "number"

    if p.get("type") in ("array", "list") or isinstance(p.get("type"), list):
        p["type"] = "text"

    return p


def set_parameter_options(p: dict, p_schema: dict, providers: list[str]) -> dict:
    """
    Set options for the parameter based on the schema.

    Parameters
    ----------
    p : Dict
        Processed parameter dictionary.
    p_schema : Dict
        Schema dictionary for the parameter.
    providers : List[str]
        List of provider options.

    Returns
    -------
    Dict
        Updated parameter dictionary with options.
    """
    choices: dict[str, list[dict[str, str]]] = {}
    widget_configs: dict[str, dict] = {}
    multiple_items_allowed_dict: dict = {}
    is_provider_specific = False
    available_providers: set = set()
    unique_general_choices: list = []
    provider: str = ""

    # Handle provider-specific choices
    for provider in providers:
        if (provider in p_schema) or (len(providers) == 1):
            is_provider_specific = True
            provider_choices: list = []
            if provider not in available_providers:
                available_providers.add(provider)
            if provider in p_schema:
                provider_choices = p_schema[provider].get("choices", [])
                if widget_def := p_schema[provider].get("x-widget_config"):
                    widget_configs[provider] = widget_def
            elif len(providers) == 1 and "enum" in p_schema:
                provider_choices = p_schema["enum"]
                p_schema.pop("enum")
            if provider_choices:
                choices[provider] = [
                    {"label": str(c), "value": c} for c in provider_choices
                ]
            if provider in p_schema and p_schema[provider].get(
                "multiple_items_allowed", False
            ):
                multiple_items_allowed_dict[provider] = True

    # Check title for provider-specific information
    if "title" in p_schema:
        title_providers = set(p_schema["title"].split(","))
        if title_providers.intersection(providers):
            is_provider_specific = True
            available_providers.update(title_providers)

    # Handle general choices
    general_choices: list = []
    if "enum" in p_schema:
        general_choices.extend(
            [
                {"label": str(c), "value": c}
                for c in p_schema["enum"]
                if c not in ["null", None]
            ]
        )
    elif "anyOf" in p_schema:
        for sub_schema in p_schema["anyOf"]:
            if "enum" in sub_schema:
                general_choices.extend(
                    [
                        {"label": str(c), "value": c}
                        for c in sub_schema["enum"]
                        if c not in ["null", None]
                    ]
                )

    if general_choices:
        # Remove duplicates by converting list of dicts to a set of tuples and back to list of dicts
        unique_general_choices = sorted(
            [dict(t) for t in {tuple(d.items()) for d in general_choices}],
            key=lambda x: x["label"],
        )
        if not is_provider_specific:
            if len(providers) == 1:
                choices[providers[0]] = unique_general_choices
                multiple_items_allowed_dict[providers[0]] = p_schema.get(
                    "multiple_items_allowed", False
                )
            else:
                choices["other"] = unique_general_choices
                multiple_items_allowed_dict["other"] = p_schema.get(
                    "multiple_items_allowed", False
                )

    # Use general choices as fallback for providers without specific options
    for provider in available_providers:
        if provider not in choices:
            if "anyOf" in p_schema and p_schema["anyOf"]:
                fallback_choices = p_schema["anyOf"][0].get("enum", [])
                choices[provider] = [
                    {"label": str(c), "value": c}
                    for c in fallback_choices
                    if c not in ["null", None]
                ]
            else:
                choices[provider] = unique_general_choices

        if provider in p_schema and p_schema[provider].get("x-widget_config"):
            widget_configs[provider] = p_schema[provider].get("x-widget_config")

    p["options"] = choices
    p["multiple_items_allowed"] = multiple_items_allowed_dict

    if is_provider_specific:
        p["available_providers"] = list(available_providers)
        p["x-widget_config"] = widget_configs

    else:
        p["x-widget_config"] = (
            widget_configs.get(provider, {}) if provider else widget_configs
        )

    return p


def process_parameter(param: dict, providers: list[str]) -> dict:
    """
    Process a single parameter and return the processed dictionary.

    Parameters
    ----------
    param : Dict
        Parameter dictionary.
    providers : List[str]
        List of provider options.

    Returns
    -------
    Dict
        Processed parameter dictionary.
    """
    p: dict = {}
    param_name = param["name"]
    p["parameter_name"] = param_name
    p["label"] = (
        param_name.replace("_", " ").replace("fixedincome", "fixed income").title()
    )
    p["description"] = (
        (param.get("description", param_name).split(" (provider:")[0].strip())
        .split("Multiple comma separated items allowed")[0]
        .strip()
    )
    p["optional"] = param.get("required", False) is False

    if param_name == "provider":
        p["type"] = "text"
        p["label"] = "Provider"
        p["description"] = "Source of the data."
        p["available_providers"] = providers
        return p

    if param_name in ["symbol", "series_id", "release_id"]:
        p["type"] = "text"
        p["label"] = param_name.title().replace("_", " ").replace("Id", "ID")
        p["description"] = (
            p["description"]
            .split("Multiple comma separated items allowed for provider(s)")[0]
            .strip()
        )
        multiple_items_allowed_dict: dict = {}
        for _provider in providers:
            if _provider in param["schema"] and param["schema"][_provider].get(
                "multiple_items_allowed", False
            ):
                multiple_items_allowed_dict[_provider] = True

        p["multiple_items_allowed"] = multiple_items_allowed_dict
        if "Multiple comma separated items allowed" in p["description"]:
            p["description"] = (
                p["description"]
                .split("Multiple comma separated items allowed")[0]
                .strip()
            )

        if widget_config := param["schema"].get("x-widget_config", {}):
            p["x-widget_config"] = widget_config

        return p

    p_schema = param.get("schema", {})
    p["value"] = p_schema.get("default", None)
    p = set_parameter_options(p, p_schema, providers)
    p = set_parameter_type(p, p_schema)

    if title := p_schema.get("title", ""):
        p["label"] = (
            p.get("parameter_name", "").replace("_", " ").title()
            if ("," in title and title.replace(",", "").islower())
            or title.lower() in providers
            else title
        )

    if _widget_config := p_schema.get("x-widget_config", {}):
        p.update(_widget_config)

    return p


def get_query_schema_for_widget(
    openapi_json: dict, command_route: str
) -> tuple[list[dict], bool]:
    """
    Extract the query schema for a widget.

    Parameters
    ----------
    openapi_json : dict
        The OpenAPI specification as a dictionary.
    command_route : str
        The route of the command in the OpenAPI specification.

    Returns
    -------
    Tuple[List[Dict], bool]
        A tuple containing the list of processed parameters and a boolean indicating if a chart is present.
    """
    has_chart = False
    command = openapi_json["paths"][command_route]
    schema_method = list(command)[0]
    command = command[schema_method]
    params = command.get("parameters", [])
    route_params: list[dict] = []
    providers: list[str] = extract_providers(params)
    if not providers:
        providers = ["custom"]
    for param in params:
        if param["name"] in ["sort", "order"]:
            continue
        if param["name"] == "chart":
            has_chart = True
            continue

        p = process_parameter(param, providers)
        if "show" not in p:
            p["show"] = True
        route_params.append(p)

    return route_params, has_chart


def get_data_schema_for_widget(openapi_json, operation_id, route: Optional[str] = None):
    """
    Get the data schema for a widget based on its operationId.

    Args:
        openapi (dict): The OpenAPI specification as a dictionary.
        operation_id (str): The operationId of the widget.

    Returns:
        dict: The schema dictionary for the widget's data.
    """
    # Find the route and method for the given operationId

    if not route:
        for path, methods in openapi_json["paths"].items():
            for _method, details in methods.items():
                if details.get("operationId") == operation_id:
                    route = path
                    break

    _route = openapi_json["paths"].get(route, {}).get("get", {})

    if (
        schema := _route.get("responses", {})
        .get("200", {})
        .get("content", {})
        .get("application/json", {})
        .get("schema", {})
    ):
        # Get the reference to the schema from the successful response

        if "items" in schema:
            response_ref = schema["items"].get("$ref")
        else:
            response_ref = schema.get("$ref") or _route["responses"]["200"]["content"][
                "application/json"
            ].get("schema")

        if isinstance(response_ref, dict) and "type" in response_ref:
            response_ref = response_ref["type"]

        if response_ref:
            # Extract the schema name from the reference
            schema_name = response_ref.split("/")[-1]
            # Fetch and return the schema from components
            if schema_name and schema_name in openapi_json.get("components", {}).get(
                "schemas", {}
            ):
                props = openapi_json["components"]["schemas"][schema_name].get(
                    "properties", {}
                )
                if props and "results" in props:
                    return props["results"]

            return openapi_json["components"]["schemas"].get(schema_name, schema_name)
    # Return None if the schema is not found
    return None


def data_schema_to_columns_defs(  # noqa: PLR0912  # pylint: disable=too-many-branches
    openapi_json,
    operation_id,
    provider,
    route: Optional[str] = None,
    get_widget_config: bool = False,
):
    """Convert data schema to column definitions for the widget."""
    # Initialize an empty list to hold the schema references
    schema_refs: list = []

    result_schema_ref = get_data_schema_for_widget(openapi_json, operation_id, route)

    # Check if 'anyOf' is in the result_schema_ref and handle the nested structure
    if result_schema_ref and "anyOf" in result_schema_ref:
        for item in result_schema_ref["anyOf"]:
            # When there are multiple providers a 'oneOf' is used
            if "items" in item and "oneOf" in item["items"]:
                # Extract the $ref values
                schema_refs.extend(
                    [
                        oneOf_item["$ref"].split("/")[-1]
                        for oneOf_item in item["items"]["oneOf"]
                        if "$ref" in oneOf_item
                    ]
                )
            # When there's only one model there is no oneOf
            elif "items" in item and "$ref" in item["items"]:
                schema_refs.append(item["items"]["$ref"].split("/")[-1])
            elif "$ref" in item:
                schema_refs.append(item["$ref"].split("/")[-1])
            elif "oneOf" in item:
                for ref in item.get("oneOf", []):
                    maybe_ref = ref.get("$ref").split("/")[-1]
                    if maybe_ref.lower().startswith(provider):
                        schema_refs.append(maybe_ref)
                        break

    # Fetch the schemas using the extracted references
    schemas = [
        openapi_json["components"]["schemas"][ref]
        for ref in schema_refs
        if ref and ref in openapi_json["components"]["schemas"]
    ]

    if not schemas and result_schema_ref and "properties" in result_schema_ref:
        schemas.append(result_schema_ref)

    # Proceed with finding common keys and generating column definitions
    if not schemas:
        return []

    target_schema: dict = {}

    if len(schemas) == 1:
        target_schema = schemas[0]
    else:
        for schema in schemas:
            if (
                schema.get("description", "")
                .lower()
                .startswith(provider.lower().replace("tradingeconomics", "te"))
            ) or (
                schema.get("description", "").lower().startswith("us government")
                or (schema.get("description", "").lower().startswith(provider))
            ):
                target_schema = schema
                break

    if get_widget_config:
        return target_schema.get("x-widget_config", {})

    keys = list(target_schema.get("properties", {}))

    column_defs: list = []
    for key in keys:
        cell_data_type = None
        formatterFn = None
        prop = target_schema.get("properties", {}).get(key)
        # Handle prop types for both when there's a single prop type or multiple
        if "items" in prop:
            items = prop.get("items", {})
            items = items.get("anyOf", items)
            prop["anyOf"] = items if isinstance(items, list) else [items]
            types = [
                sub_prop.get("type") for sub_prop in prop["anyOf"] if "type" in sub_prop
            ]
            if "number" in types or "integer" in types or "float" in types:
                cell_data_type = "number"
            elif "string" in types and any(
                sub_prop.get("format") in ["date", "date-time"]
                for sub_prop in prop["anyOf"]
                if "format" in sub_prop
            ):
                cell_data_type = "date"
            else:
                cell_data_type = "text"
        elif "anyOf" in prop:
            types = [
                sub_prop.get("type") for sub_prop in prop["anyOf"] if "type" in sub_prop
            ]
            if "number" in types or "integer" in types or "float" in types:
                cell_data_type = "number"
            elif "string" in types and any(
                sub_prop.get("format") in ["date", "date-time"]
                for sub_prop in prop["anyOf"]
                if "format" in sub_prop
            ):
                cell_data_type = "date"
            else:
                cell_data_type = "text"
        else:
            prop_type = prop.get("type", None)
            if prop_type in ["number", "integer", "float"]:
                cell_data_type = "number"
                if prop_type == "integer":
                    formatterFn = "int"
            elif "format" in prop and prop["format"] in ["date", "date-time"]:
                cell_data_type = "date"
            else:
                cell_data_type = "text"

        column_def: dict = {}
        # OpenAPI changes some of the field names.
        k = to_snake_case(key)
        column_def["field"] = k
        if k in [
            "symbol",
            "symbol_root",
            "series_id",
            "date",
            "published",
            "fiscal_year",
            "period_ending",
            "period_beginning",
            "order",
            "name",
            "title",
            "cusip",
            "isin",
            "expiration",
            "dte",
            "strike",
            "option_type",
        ]:
            column_def["pinned"] = "left"

        column_def["formatterFn"] = formatterFn
        header_name = prop.get("title", key.title())
        column_def["headerName"] = " ".join(
            [
                (word.upper() if word in TO_CAPS_STRINGS else word)
                for word in header_name.split(" ")
            ]
        )
        column_def["headerTooltip"] = prop.get(
            "description", prop.get("title", key.title())
        )
        column_def["cellDataType"] = cell_data_type
        measurement = prop.get("x-unit_measurement")

        if measurement == "percent":
            column_def["formatterFn"] = (
                "normalizedPercent"
                if prop.get("x-frontend_multiply") == 100
                else "percent"
            )
            column_def["renderFn"] = "greenRed"

        if k in ["cik", "isin", "figi", "cusip", "sedol", "symbol"]:
            column_def["cellDataType"] = "text"
            column_def["headerName"] = (
                column_def["headerName"].upper() if k != "symbol" else "Symbol"
            )

        if k in ["fiscal_year", "year", "year_born"]:
            column_def["cellDataType"] = "number"
            column_def["formatterFn"] = "none"

        if "date" in column_def["headerTooltip"].lower():
            column_def["cellDataType"] = "date"

        if (
            route
            and route.endswith("chains")
            and column_def.get("field")
            in [
                "underlying_symbol",
                "contract_symbol",
                "underlying_price",
                "contract_symbol",
            ]
        ):
            column_def["hide"] = True

        if column_def.get("field") in [
            "delta",
            "gamma",
            "theta",
            "vega",
            "rho",
            "vega",
            "charm",
            "vanna",
            "vomma",
        ]:
            column_def["formatterFn"] = "none"
            if column_def["field"] in ["delta", "theta", "rho"]:
                column_def["renderFn"] = "greenRed"

        if (
            route
            and route.endswith("chains")
            and column_def["field"] == "implied_volatility"
        ):
            column_def["formatterFn"] = "normalizedPercent"

        if column_def.get("field") == "change":
            column_def["renderFn"] = "greenRed"

        if _widget_config := prop.get("x-widget_config", {}):

            if _widget_config.get("exclude"):
                continue

            column_def.update(_widget_config)

        column_defs.append(column_def)
    return column_defs
