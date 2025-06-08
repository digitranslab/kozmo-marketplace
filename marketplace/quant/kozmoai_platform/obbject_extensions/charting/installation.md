---
title: Installation
sidebar_position: 1
description: This page outlines the installation of the kozmoai-charting extension.
keywords:
- tutorial
- KozmoAI Platform
- Installation
- Python client
- Fast API
- getting started
- extensions
- charting
- view
- Plotly
- toolkit
- community
- Plotly
- KozmoAIFigure
- PyWry
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Installation - Charting - Extensions | KozmoAI Platform Docs" />

## PyPI

To install the extension, run the following command in this folder:

```bash
pip install kozmoai-charting
```

> Find the latest version on [PyPI](https://pypi.org/project/kozmoai-charting/).

## Editable Mode

To install from source in editable mode, navigate into the folder, `~/kozmoai_platform/extensions/charting`, and enter:

```console
pip install -e .
```

After installation, the Python interface will automatically rebuild on initialization.  This process can also be triggered manually with:

```python
import kozmoai
kozmoai.build()
```

The Python interpreter may need to be restarted.

## PyWry Dependency In Linux

When using Linux distributions, the PyWry dependency requires certain dependencies to be installed first.

- Debian-based / Ubuntu / Mint:
`sudo apt install libwebkit2gtk-4.0-dev`

- Arch Linux / Manjaro:
`sudo pacman -S webkit2gtk`

- Fedora:
`sudo dnf install gtk3-devel webkit2gtk3-devel`

If Rust (Cargo) is required, install it:

```console
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```
