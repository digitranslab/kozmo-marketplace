"""Script to build the KozmoAI platform static assets."""

# flake8: noqa: S603
# pylint: disable=import-outside-toplevel

import subprocess
import sys


def main():
    """Build the KozmoAI platform static assets."""
    try:
        from kozmoai import build

        build()
    except (
        ImportError,
        ModuleNotFoundError,
        AttributeError,
    ) as e:
        print(  # noqa: T201
            "\nKozmoAI build script not found, installing from PyPI...\n",
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "kozmoai", "--no-deps"],
            check=True,
        )
        try:
            subprocess.run(
                [sys.executable, "-c", "import kozmoai; kozmoai.build()"],
                check=True,
            )
        except (subprocess.CalledProcessError, AttributeError):
            raise RuntimeError(
                "Failed to find the KozmoAI build script. Install with `pip install kozmoai --no-deps`"
            ) from e


if __name__ == "__main__":
    main()
