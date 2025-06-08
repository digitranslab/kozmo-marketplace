# KozmoAI Platform - Core

## Overview

The Core extension serves as the foundational component of the KozmoAI Platform. It encapsulates essential functionalities and serves as an infrastructural base for other extensions. This extension is vital for maintaining the integrity and standardization of the platform.

## Key Features

- **Standardized Data Model** (`Data` Class): A flexible and dynamic Pydantic model capable of handling various data structures.
- **Standardized Query Params** (`QueryParams` Class): A Pydantic model for handling querying to different providers.
- **Dynamic Field Support**: Enables handling of undefined fields, providing versatility in data processing.
- **Robust Data Validation**: Utilizes Pydantic's validation features to ensure data integrity.
- **API Routing Mechanism** (`Router` Class): Simplifies the process of defining API routes and endpoints - out of the box Python and Web endpoints.

## Getting Started

### Prerequisites

- Python 3.9 or higher.
- Familiarity with FastAPI and Pydantic.

### Installation

Installing through pip:

```bash
pip install kozmoai-core
```

> Note that, the kozmoai-core is an infrastructural component of the KozmoAI Platform. It is not intended to be used as a standalone package.

### Usage

The Core extension is used as the basis for building and integrating new data sources, providers, and extensions into the KozmoAI Platform. It provides the necessary classes and structures for standardizing and handling data.

### Contributing

We welcome contributions! If you're looking to contribute, please:

- Follow the existing coding standards and conventions.
- Write clear, documented code.
- Ensure your code does not negatively impact performance.
- Test your contributions thoroughly.

Please refer to our [Contributing Guidelines](https://docs.kozmoai.co/platform/developer_guide/contributing).

### Collaboration

Engage with the development team and the community. Be open to feedback and collaborative discussions.

### Support

For support, questions, or more information, please visit [KozmoAI Platform Documentation](https://docs.kozmoai.co/platform).

### License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/digitranslab/digitranslab/blob/main/LICENSE) file for details.
