"""Install for development script."""

# flake8: noqa: S603

import subprocess
import sys
from pathlib import Path

from tomlkit import dumps, load, loads

PLATFORM_PATH = Path(__file__).parent.resolve()
LOCK = PLATFORM_PATH / "poetry.lock"
PYPROJECT = PLATFORM_PATH / "pyproject.toml"
CLI_PATH = Path(__file__).parent.parent.resolve() / "cli"
CLI_PYPROJECT = CLI_PATH / "pyproject.toml"
CLI_LOCK = CLI_PATH / "poetry.lock"

LOCAL_DEPS = """
[tool.poetry.dependencies]
python = ">=3.9,<3.13"
kozmoai-devtools = { path = "./extensions/devtools", develop = true, markers = "python_version >= '3.10'" }
kozmoai-core = { path = "./core", develop = true }
kozmoai-platform-api = { path = "./extensions/platform_api", develop = true }

kozmoai-benzinga = { path = "./providers/benzinga", develop = true }
kozmoai-bls = { path = "./providers/bls", develop = true }
kozmoai-cftc = { path = "./providers/cftc", develop = true }
kozmoai-econdb = { path = "./providers/econdb", develop = true }
kozmoai-federal-reserve = { path = "./providers/federal_reserve", develop = true }
kozmoai-fmp = { path = "./providers/fmp", develop = true }
kozmoai-fred = { path = "./providers/fred", develop = true }
kozmoai-imf = { path = "./providers/imf", develop = true }
kozmoai-intrinio = { path = "./providers/intrinio", develop = true }
kozmoai-oecd = { path = "./providers/oecd", develop = true }
kozmoai-polygon = { path = "./providers/polygon", develop = true }
kozmoai-sec = { path = "./providers/sec", develop = true }
kozmoai-tiingo = { path = "./providers/tiingo", develop = true }
kozmoai-tradingeconomics = { path = "./providers/tradingeconomics", develop = true }
kozmoai-us-eia = { path = "./providers/eia", develop = true }
kozmoai-yfinance = { path = "./providers/yfinance", develop = true }

kozmoai-commodity = { path = "./extensions/commodity", develop = true }
kozmoai-crypto = { path = "./extensions/crypto", develop = true }
kozmoai-currency = { path = "./extensions/currency", develop = true }
kozmoai-derivatives = { path = "./extensions/derivatives", develop = true }
kozmoai-economy = { path = "./extensions/economy", develop = true }
kozmoai-equity = { path = "./extensions/equity", develop = true }
kozmoai-etf = { path = "./extensions/etf", develop = true }
kozmoai-fixedincome = { path = "./extensions/fixedincome", develop = true }
kozmoai-index = { path = "./extensions/index", develop = true }
kozmoai-news = { path = "./extensions/news", develop = true }
kozmoai-regulators = { path = "./extensions/regulators", develop = true }

# Community dependencies
kozmoai-alpha-vantage = { path = "./providers/alpha_vantage", optional = true, develop = true }
kozmoai-biztoc = { path = "./providers/biztoc", optional = true, develop = true }
kozmoai-cboe = { path = "./providers/cboe", optional = true, develop = true }
kozmoai-deribit = { path = "./providers/deribit", optional = true, develop = true }
kozmoai-ecb = { path = "./providers/ecb", optional = true, develop = true }
kozmoai-finra = { path = "./providers/finra", optional = true, develop = true }
kozmoai-finviz = { path = "./providers/finviz", optional = true, develop = true }
kozmoai-government-us = { path = "./providers/government_us", optional = true, develop = true }
kozmoai-multpl = { path = "./providers/multpl", optional = true, develop = true }
kozmoai-nasdaq = { path = "./providers/nasdaq", optional = true, develop = true }
kozmoai-seeking-alpha = { path = "./providers/seeking_alpha", optional = true, develop = true }
kozmoai-stockgrid = { path = "./providers/stockgrid" , optional = true,  develop = true }
kozmoai_tmx = { path = "./providers/tmx", optional = true, develop = true }
kozmoai_tradier = { path = "./providers/tradier", optional = true, develop = true }
kozmoai-wsj = { path = "./providers/wsj", optional = true, develop = true }

kozmoai-charting = { path = "./obbject_extensions/charting", optional = true, develop = true }
kozmoai-econometrics = { path = "./extensions/econometrics", optional = true, develop = true }
kozmoai-quantitative = { path = "./extensions/quantitative", optional = true, develop = true }
kozmoai-technical = { path = "./extensions/technical", optional = true, develop = true }
"""


def extract_dependencies(local_dep_path, dev: bool = False):
    """Extract development dependencies from a given package's pyproject.toml."""
    package_pyproject_path = PLATFORM_PATH / local_dep_path
    if package_pyproject_path.exists():
        with open(package_pyproject_path / "pyproject.toml") as f:
            package_pyproject_toml = load(f)
        if dev:
            return (
                package_pyproject_toml.get("tool", {})
                .get("poetry", {})
                .get("group", {})
                .get("dev", {})
                .get("dependencies", {})
            )
        return (
            package_pyproject_toml.get("tool", {})
            .get("poetry", {})
            .get("dependencies", {})
        )
    return {}


def get_all_dev_dependencies():
    """Aggregate development dependencies from all local packages."""
    all_dev_dependencies = {}
    local_deps = loads(LOCAL_DEPS).get("tool", {}).get("poetry", {})["dependencies"]
    for _, package_info in local_deps.items():
        if "path" in package_info:
            dev_deps = extract_dependencies(Path(package_info["path"]), dev=True)
            all_dev_dependencies.update(dev_deps)
    return all_dev_dependencies


def install_platform_local(_extras: bool = False):
    """Install the Platform locally for development purposes."""
    original_lock = LOCK.read_text()
    original_pyproject = PYPROJECT.read_text()

    local_deps = loads(LOCAL_DEPS).get("tool", {}).get("poetry", {})["dependencies"]
    with open(PYPROJECT) as f:
        pyproject_toml = load(f)
    pyproject_toml.get("tool", {}).get("poetry", {}).get("dependencies", {}).update(
        local_deps
    )

    # Extract and add devtools dependencies manually if Python version is 3.9
    if sys.version_info[:2] == (3, 9):
        devtools_deps = extract_dependencies(Path("./extensions/devtools"), dev=False)
        devtools_deps.remove("python")
        pyproject_toml.get("tool", {}).get("poetry", {}).get("dependencies", {}).update(
            devtools_deps
        )

    if _extras:
        dev_dependencies = get_all_dev_dependencies()
        pyproject_toml.get("tool", {}).get("poetry", {}).setdefault(
            "group", {}
        ).setdefault("dev", {}).setdefault("dependencies", {})
        pyproject_toml.get("tool", {}).get("poetry", {})["group"]["dev"][
            "dependencies"
        ].update(dev_dependencies)

    TEMP_PYPROJECT = dumps(pyproject_toml)

    try:
        with open(PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEMP_PYPROJECT)

        CMD = [sys.executable, "-m", "poetry"]
        extras_args = ["-E", "all"] if _extras else []

        subprocess.run(
            CMD + ["lock"],
            cwd=PLATFORM_PATH,
            check=True,
        )
        subprocess.run(
            CMD + ["install"] + extras_args,
            cwd=PLATFORM_PATH,
            check=True,
        )

    except (Exception, KeyboardInterrupt) as e:
        print(e)  # noqa: T201
        print("Restoring pyproject.toml and poetry.lock")  # noqa: T201

    finally:
        # Revert pyproject.toml and poetry.lock to their original state.
        with open(PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
            f.write(original_pyproject)

        with open(LOCK, "w", encoding="utf-8", newline="\n") as f:
            f.write(original_lock)


def install_platform_cli():
    """Install the CLI locally for development purposes."""
    original_lock = CLI_LOCK.read_text()
    original_pyproject = CLI_PYPROJECT.read_text()

    with open(CLI_PYPROJECT) as f:
        pyproject_toml = load(f)

    # remove "kozmoai" from dependencies
    pyproject_toml.get("tool", {}).get("poetry", {}).get("dependencies", {}).pop(
        "kozmoai", None
    )

    TEMP_PYPROJECT = dumps(pyproject_toml)

    try:
        with open(CLI_PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEMP_PYPROJECT)

        CMD = [sys.executable, "-m", "poetry"]

        subprocess.run(
            CMD + ["lock"],
            cwd=CLI_PATH,
            check=True,  # noqa: S603
        )
        subprocess.run(CMD + ["install"], cwd=CLI_PATH, check=True)  # noqa: S603

    except (Exception, KeyboardInterrupt) as e:
        print(e)  # noqa: T201
        print("Restoring pyproject.toml and poetry.lock")  # noqa: T201

    finally:
        # Revert pyproject.toml and poetry.lock to their original state.
        with open(CLI_PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
            f.write(original_pyproject)

        with open(CLI_LOCK, "w", encoding="utf-8", newline="\n") as f:
            f.write(original_lock)


if __name__ == "__main__":
    args = sys.argv[1:]
    extras = any(arg.lower() in ["-e", "--extras"] for arg in args)
    cli = any(arg.lower() in ["-c", "--cli"] for arg in args)
    install_platform_local(extras)
    if cli:
        install_platform_cli()
