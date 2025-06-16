#!/usr/bin/env python3
"""
PyPI Upload Helper Script

This script helps to prepare packages for upload to PyPI by:
1. Temporarily replacing file references with version constraints
2. Building the package
3. Optionally uploading to PyPI
4. Restoring the original configuration

Usage:
    python pypi_upload_helper.py --type [pandas-ta|extension|provider] --name [name] [--upload]

Examples:
    # Prepare pandas-ta-kozmoai (build only)
    python pypi_upload_helper.py --type pandas-ta

    # Prepare and upload pandas-ta-kozmoai
    python pypi_upload_helper.py --type pandas-ta --upload

    # Prepare technical extension (build only)
    python pypi_upload_helper.py --type extension --name technical

    # Prepare and upload technical extension
    python pypi_upload_helper.py --type extension --name technical --upload
"""

import os
import sys
import argparse
import subprocess
import re
import shutil
from pathlib import Path
from datetime import datetime


def run_command(cmd, cwd=None):
    """Run a shell command and print output"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=True, text=True, 
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result


def backup_file(file_path):
    """Create a backup of a file"""
    backup_path = f"{file_path}.backup"
    shutil.copy2(file_path, backup_path)
    print(f"Created backup: {backup_path}")
    return backup_path


def restore_file(file_path):
    """Restore a file from its backup"""
    backup_path = f"{file_path}.backup"
    if os.path.exists(backup_path):
        shutil.copy2(backup_path, file_path)
        os.remove(backup_path)
        print(f"Restored {file_path} from backup")
    else:
        print(f"No backup found for {file_path}")


def modify_pyproject_toml(file_path, timestamp=None):
    """Modify pyproject.toml to use version constraints and add dev timestamp"""
    with open(file_path, 'r') as f:
        content = f.read()

    # Add dev timestamp to version
    if timestamp:
        content = re.sub(r'(version\s*=\s*"[^"]+)(")', f'\\1.dev{timestamp}\\2', content)

    # Replace file references with version constraints
    content = re.sub(
        r'pandas-ta-kozmoai\s*=\s*{\s*path\s*=\s*"[^"]*",\s*develop\s*=\s*true\s*}',
        'pandas-ta-kozmoai = "^0.4.21"',
        content
    )
    
    # Replace other file references
    content = re.sub(
        r'{\s*path\s*=\s*"[^"]*",\s*develop\s*=\s*true[^}]*\s*}',
        '"^1.0.0"',
        content
    )

    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Modified {file_path}")


def get_package_path(pkg_type, pkg_name=None):
    """Get the path to the package directory"""
    base_path = Path(os.getcwd())
    
    # Navigate to the project root
    while not (base_path / 'marketplace').exists() and base_path != base_path.parent:
        base_path = base_path.parent
    
    if not (base_path / 'marketplace').exists():
        raise ValueError("Could not find project root. Run this script from within the project directory.")
    
    if pkg_type == 'pandas-ta':
        return base_path / 'marketplace' / 'quant' / 'pandas_ta_kozmoai'
    elif pkg_type == 'extension':
        if not pkg_name:
            raise ValueError("Extension name must be provided")
        return base_path / 'marketplace' / 'quant' / 'kozmoai_platform' / 'extensions' / pkg_name
    elif pkg_type == 'provider':
        if not pkg_name:
            raise ValueError("Provider name must be provided")
        return base_path / 'marketplace' / 'quant' / 'kozmoai_platform' / 'providers' / pkg_name
    else:
        raise ValueError(f"Unknown package type: {pkg_type}")


def prepare_and_build_package(pkg_type, pkg_name=None, upload=False):
    """Prepare and build a package for upload to PyPI"""
    pkg_path = get_package_path(pkg_type, pkg_name)
    pyproject_path = pkg_path / 'pyproject.toml'
    
    if not pyproject_path.exists():
        raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")
    
    print(f"Processing {pkg_type} package: {pkg_name or 'pandas-ta-kozmoai'}")
    print(f"Package path: {pkg_path}")
    
    try:
        # Backup the original pyproject.toml
        backup_file(pyproject_path)
        
        # Modify pyproject.toml
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        modify_pyproject_toml(pyproject_path, timestamp)
        
        # Build the package
        run_command('python -m build', cwd=pkg_path)
        
        # Upload to PyPI if requested
        if upload:
            run_command('twine upload --verbose dist/*', cwd=pkg_path)
        else:
            print("\nPackage built successfully but not uploaded.")
            print(f"To upload manually, run: cd {pkg_path} && twine upload dist/*")
        
    finally:
        # Always restore the original pyproject.toml
        restore_file(pyproject_path)


def main():
    parser = argparse.ArgumentParser(description='Prepare and upload packages to PyPI')
    parser.add_argument('--type', required=True, choices=['pandas-ta', 'extension', 'provider'],
                        help='Type of package to prepare')
    parser.add_argument('--name', help='Name of the extension or provider')
    parser.add_argument('--upload', action='store_true', help='Upload to PyPI after building')
    
    args = parser.parse_args()
    
    if args.type in ['extension', 'provider'] and not args.name:
        parser.error(f'--name is required for {args.type} packages')
    
    try:
        prepare_and_build_package(args.type, args.name, args.upload)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main() 