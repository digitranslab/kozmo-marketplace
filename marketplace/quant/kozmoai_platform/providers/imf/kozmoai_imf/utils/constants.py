"""IMF Constants."""

# pylint: disable=line-too-long
# flake8: noqa: E501

FSI_PRESETS = [
    "fsi_core",
    "fsi_core_underlying",
    "fsi_other",
    "fsi_encouraged_set",
    "fsi_balance_sheets",
    "fsi_all",
]

IRFCL_HEADLINE = "RAF_USD,RAFA_USD,RAFAFX_USD,RAOFA_USD,RAPFA_USD,RAFAIMF_USD,RAFASDR_USD,RAFAGOLD_USD,RACFA_USD,RAMDCD_USD,RAMFIFC_USD,RAMSR_USD"

RESERVE_ASSETS_AND_OTHER_FX_ASSETS = "RAF_USD,RAFA_USD,RAFAFX_USD,RAFAFXS_USD,RAFAFXSI_USD,RAFAFXCD_USD,RAFAFXCDN_USD,RAFAFXCDBI_USD,RAFAFXCDBIA_USD,RAFAFXCDBO_USD,RAFAFXCDBOA_USD,RAFAIMF_USD,RAFASDR_USD,RAFAGOLD_USD,RAFAGOLDV_OZT,RAFAO_USD,RAFAOF_USD,RAFAOL_USD,RAFAOO_USD,RAOFA_USD,RAOFAS_USD,RAOFAD_USD,RAOFAL_USD,RAOFAF_USD,RAOFAG_USD"

PREDETERMINED_DRAINS_ON_FX_ASSETS = "RAPFA_USD,RAPFALSD_USD,RAPFALSD_1M_USD,RAPFALSD_1M_3M_USD,RAPFALSD_3M_1Y_USD,RAPFALSDOP_USD,RAPFALSDOP_1M_USD,RAPFALSDOP_1M_3M_USD,RAPFALSDOP_3M_1Y_USD,RAPFALSDOI_USD,RAPFALSDOI_1M_USD,RAPFALSDOI_1M_3M_USD,RAPFALSDOI_3M_1Y_USD,RAPFALSDIP_USD,RAPFALSDIP_1M_USD,RAPFALSDIP_1M_3M_USD,RAPFALSDIP_3M_1Y_USD,RAPFALSDII_USD,RAPFALSDII_1M_USD,RAPFALSDII_1M_3M_USD,RAPFALSDII_3M_1Y_USD,RAPFAFFS_USD,RAPFAFFS_1M_USD,RAPFAFFS_1M_3M_USD,RAPFAFFS_3M_1Y_USD,RAPFAFFL_USD,RAPFAFFL_1M_USD,RAPFAFFL_1M_3M_USD,RAPFAFFL_3M_1Y_USD,RAPFAO_USD,RAPFAO_1M_USD,RAPFAO_1M_3M_USD,RAPFAO_3M_1Y_USD,RAPFAOOR_USD,RAPFAOOR_1M_USD,RAPFAOOR_1M_3M_USD,RAPFAOOR_3M_1Y_USD,RAPFAOIRR_USD,RAPFAOIRR_1M_USD,RAPFAOIRR_1M_3M_USD,RAPFAOIRR_3M_1Y_USD,RAPFAOOC_USD,RAPFAOOC_1M_USD,RAPFAOOC_1M_3M_USD,RAPFAOOC_3M_1Y_USD,RAPFAOIC_USD,RAPFAOIC_1M_USD,RAPFAOIC_1M_3M_USD,RAPFAOIC_3M_1Y_USD,RAPFAOOP_USD,RAPFAOOP_1M_USD,RAPFAOOP_1M_3M_USD,RAPFAOOP_3M_1Y_USD,RAPFAOIR_USD,RAPFAOIR_1M_USD,RAPFAOIR_1M_3M_USD,RAPFAOIR_3M_1Y_USD,RAFA_RAPFA_RO"

CONTINGENT_DRAINS_FX_ASSETS = "RACFA_USD,RACFAL_USD,RACFAL_1M_USD,RACFAL_1M_3M_USD,RACFAL_3M_1Y_USD,RACFALG_USD,RACFALG_1M_USD,RACFALG_1M_3M_USD,RACFALO_USD,RACFALO_1M_USD,RACFALO_1M_3M_USD,RACFALO_3M_1Y_USD,RACFAS_USD,RACFACB_USD,RACFACB_1M_USD,RACFACB_1M_3M_USD,RACFACB_3M_1Y_USD,RACFACBA_USD,RACFACBA_1M_USD,RACFACBA_1M_3M_USD,RACFACBA_3M_1Y_USD,RACFACBAOI_USD,RACFACBAOI_1M_USD,RACFACBAOI_1M_3M_USD,RACFACBAON_USD,RACFACBAON_1M_USD,RACFACBAON_1M_3M_USD,RACFACBAON_3M_1Y_USD,RACFACBABIS_USD,RACFACBAIMF_1M_USD,RACFACBAIMF_1M_3M_USD,RACFACBAIMF_3M_1Y_USD,RACFACBAIMF_USD,RACFACBFIR_USD,RACFACBFIR_1M_USD,RACFACBFIR_1M_3M_USD,RACFACBFIR_3M_1Y_USD,RACFACBFIO_USD,RACFACBFIO_1M_USD,RACFACBFIO_1M_3M_USD,RACFACBFIO_3M_1Y_USD,RACFACT_USD,RACFACT_1M_USD,RACFACT_1M_3M_USD,RACFACT_3M_1Y_USD,RACFACTA_USD,RACFACTA_1M_USD,RACFACTA_1M_3M_USD,RACFACTA_3M_1Y_USD,RACFACTAOI_USD,RACFACTAOI_1M_USD,RACFACTAOI_1M_3M_USD,RACFACTAOI_3M_1Y_USD,RACFACTAON_USD,RACFACTAON_1M_USD,RACFACTAON_1M_3M_USD,RACFACTAON_3M_1Y_USD,RACFACTABIS_USD,RACFACTABIS_1M_USD,RACFACTABIS_1M_3M_USD,RACFACTABIS_3M_1Y_USD,RACFACTAIMF_USD,RACFACTAIMF_1M_USD,RACFACTFIR_USD,RACFACTFIR_1M_USD,RACFACTFIR_1M_3M_USD,RACFACTFIR_3M_1Y_USD,RACFACTFIO_USD,RACFACTFIO_1M_USD,RACFACTFIO_1M_3M_USD,RACFACTFIO_3M_1Y_USD,RACFAPPS_USD,RACFAPPS_1M_USD,RACFAPPS_1M_3M_USD,RACFAPPS_3M_1Y_USD,RACFAPPSBP_USD,RACFAPPSBP_1M_USD,RACFAPPSBP_1M_3M_USD,RACFAPPSBP_3M_1Y_USD,RACFAPPSWC_USD,RACFAPPSWC_1M_USD,RACFAPPSWC_1M_3M_USD,RACFAPPSWC_3M_1Y_USD,RACFAPPL_USD,RACFAPPL_1M_USD,RACFAPPL_1M_3M_USD,RACFAPPL_3M_1Y_USD,RACFAPPLBC_USD,RACFAPPLBC_1M_USD,RACFAPPLBC_1M_3M_USD,RACFAPPLBC_3M_1Y_USD,RACFAPPLWP_USD,RACFAPPLWP_1M_USD,RACFAPPLWP_1M_3M_USD,RACFAPPLWP_3M_1Y_USD,RACFAMPAS_USD,RACFAMPAS_1M_USD,RACFAMPAS_1M_3M_USD,RACFAMPAS_3M_1Y_USD,RACFAMPAL_USD,RACFAMPAL_1M_USD,RACFAMPAL_1M_3M_USD,RACFAMPAL_3M_1Y_USD,RACFAMPBS_USD,RACFAMPBS_1M_USD,RACFAMPBS_1M_3M_USD,RACFAMPBS_3M_1Y_USD,RACFAMPBL_USD,RACFAMPBL_1M_USD,RACFAMPBL_1M_3M_USD,RACFAMPBL_3M_1Y_USD,RACFAMPCS_USD,RACFAMPCS_1M_USD,RACFAMPCS_1M_3M_USD,RACFAMPCS_3M_1Y_USD,RACFAMPCL_USD,RACFAMPCL_1M_USD,RACFAMPCL_1M_3M_USD,RACFAMPCL_3M_1Y_USD,RACFAMPDS_USD,RACFAMPDS_1M_USD,RACFAMPDS_1M_3M_USD,RACFAMPDS_3M_1Y_USD,RACFAMPDL_USD,RACFAMPDL_1M_USD,RACFAMPDL_1M_3M_USD,RACFAMPDL_3M_1Y_USD,RACFAMPES_USD,RACFAMPES_1M_USD,RACFAMPES_1M_3M_USD,RACFAMPES_3M_1Y_USD,RACFAMPEL_USD,RACFAMPEL_1M_USD,RACFAMPEL_1M_3M_USD,RACFAMPEL_3M_1Y_USD,RACFAMPFS_USD,RACFAMPFS_1M_USD,RACFAMPFS_1M_3M_USD,RACFAMPFS_3M_1Y_USD,RACFAMPFL_USD,RACFAMPFL_1M_USD,RACFAMPFL_1M_3M_USD,RACFAMPFL_3M_1Y_USD"

IRFCL_MEMORANDUM_ITEMS = "RAMDCD_USD,RAMFIFC_USD,RAMPA_USD,RAMFFS_USD,RAMPAOA_USD,RAMSR_USD,RAMSRLRI_USD,RAMSRLRN_USD,RAMSRBRI_USD,RAMSRBAN_USD,RAMFDA_USD,RAMFDAF_USD,RAMFDAU_USD,RAMFDAW_USD,RAMFDAP_USD,RAMFDAO_USD,RAMFFL_USD,RAMPPS_USD,RAMPPSBP_USD,RAMPPSWC_USD,RAMPPL_USD,RAMPPLBP_USD,RAMPPLWC_USD,RAMCR_USD,RAMCRISDR_USD,RAMCRIC_USD_USD,RAMCRIC_EUR_USD,RAMCRIC_CNY_USD,RAMCRIC_JPY_USD,RAMCRIC_GBP_USD,RAMCROSDR_USD"

IRFCL_TABLES = {
    "reserve_assets_and_other_fx_assets": RESERVE_ASSETS_AND_OTHER_FX_ASSETS,
    "predetermined_drains_on_fx_assets": PREDETERMINED_DRAINS_ON_FX_ASSETS,
    "contingent_drains_fx_assets": CONTINGENT_DRAINS_FX_ASSETS,
    "memorandum_items": IRFCL_MEMORANDUM_ITEMS,
}

IRFCL_PRESET = {
    "irfcl_top_lines": IRFCL_HEADLINE,
    **IRFCL_TABLES,
    "gold_reserves": "RAFAGOLD_USD,RAFAGOLDV_OZT",
    "derivative_assets": "RAMFDA_USD",
}

FREQUENCY_DICT = {
    "month": "M",
    "quarter": "Q",
    "annual": "A",
}
REF_SECTORS_DICT = {
    "government_ex_social_security": "S1311",
    "central_bank": "S121",
    "monetary_authorities": "S1X",
    "all_sectors": "",
}

SECTOR_MAP = {v: k for k, v in REF_SECTORS_DICT.items()}

UNIT_MULTIPLIERS_MAP = {
    "0": "Units",
    "2": "Hundreds",
    "3": "Thousands",
    "6": "Millions",
    "9": "Billions",
    "12": "Trillions",
    "N15": "Quadrillionths",
    "N14": "Hundred Trillionths",
    "N13": "Ten Trillionths",
    "N12": "Trillionths",
    "N11": "Hundred Billionths",
    "N10": "Ten Billionths",
    "N9": "Billionths",
    "N8": "Hundred Millionths",
    "N7": "Ten Millionths",
    "N6": "Millionths",
    "N5": "Hundred Thousandths",
    "N4": "Ten Thousandths",
    "N3": "Thousandths",
    "N2": "Hundredths",
    "N1": "Tenths",
    "1": "Tens",
    "4": "Ten Thousands",
    "5": "Hundred Thousands",
    "7": "Ten Millions",
    "8": "Hundred Millions",
    "10": "Ten Billions",
    "11": "Hundred Billions",
    "13": "Ten Trillions",
    "14": "Hundred Trillions",
    "15": "Quadrillions",
}

TIME_FORMAT_MAP = {
    "P1Y": "Annual",
    "P6M": "Bi-annual",
    "P3M": "Quarterly",
    "P1M": "Monthly",
    "P7D": "Weekly",
    "P1D": "Daily",
}

REF_SECTOR_MAP = {
    "S1311": "Central government excluding social security",
    "S121": "Central Bank",
    "S1X": "Monetary Authorities",
    "1C_AS": "All Sectors",
    "AllSectorsIncludingAllSectors": "All Sectors Including All Sectors",
}


def load_symbols(dataset: str) -> dict:
    """Load IMF symbol list."""
    # pylint: disable=import-outside-toplevel
    import json  # noqa
    from json.decoder import JSONDecodeError
    from pathlib import Path
    from kozmoai_core.app.model.abstract.error import KozmoAIError

    try:
        symbols_file = Path(__file__).parents[1].joinpath("assets", "imf_symbols.json")
        with symbols_file.open(encoding="utf-8") as file:
            symbols = json.load(file)
    except (FileNotFoundError, JSONDecodeError) as e:
        raise KozmoAIError(
            f"Failed to load IMF symbols from the static file: {e}"
        ) from e

    if dataset == "all":
        return symbols

    return {k: v for k, v in symbols.items() if v["dataset"] == dataset}
