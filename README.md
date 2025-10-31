# OpenCTI Connector Cookiecutter Template

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating OpenCTI connectors quickly and easily.

## What is this?

This cookiecutter template helps you bootstrap a new OpenCTI connector project with all the necessary boilerplate code and configuration files. It generates a ready-to-use project structure with proper naming conventions, configuration files, and basic connector setup.

## Features

- 🚀 Quick project setup with minimal configuration
- 📝 Automatic naming convention handling (slug, PascalCase, UPPER_CASE)
- 🔧 Pre-configured environment files and YAML configurations
- 🆔 Auto-generated unique connector ID
- 📦 Support for all OpenCTI connector types
- 🐍 Python-based connector structure using `pycti` library

## Prerequisites

- Python 3.x
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) installed:
  ```bash
  pip install cookiecutter
  ```

## Usage

### Creating a New Connector

Run the following command in your terminal:
```bash
bash cookiecutter https://github.com/mariot/connector-cookiecutter
```
# Or if local:
```bash
cookiecutter /path/to/connector-cookiecutter
```

You will be prompted to provide the following information:

- **connector_name**: The human-readable name of your connector (e.g., "My Connector")
- **connector_description**: A brief description of what your connector does
- **connector_type**: Choose from:
    - External Import
    - Internal Enrichment
    - Internal Export File
    - Internal Import File
    - Stream
- **opencti_url**: Your OpenCTI instance URL (default: http://localhost:8080)
- **opencti_token**: Your OpenCTI API token

The template will automatically generate:
- `connector_id`: A unique UUID for your connector
- `connector_slug`: Snake_case version of the name (e.g., "my_connector")
- `connector_upper_slug`: Upper snake_case version (e.g., "MY_CONNECTOR")
- `connector_pascal_case`: PascalCase version (e.g., "MyConnector")
- `connector_scope`: The scope for your connector

### Generated Project Structure

After running cookiecutter, you'll get a project structure like this:
```
my_connector/
    ├── main.py # Entry point for the connector
    ├── config.yml # Main configuration file
    ├── config.yml.sample # Sample configuration
    ├── .env.example # Example environment variables
    └── my_connector/ # Connector package
        └── settings.py # Settings module
```


### Next Steps

After generating your connector:

1. **Navigate to your project:**
   ```bash
   cd your_connector_name
   ```

2. **Set up your environment:**

3. **Install dependencies:**

4. **Implement your connector logic:**
    - Edit the generated files to add your specific connector functionality
    - The `main.py` file provides the basic structure to get started

5. **Configure your connector:**
    - Update `config.yml` with your OpenCTI instance details
    - Add any connector-specific configuration parameters

6. **Run your connector:**
   ```bash
   python main.py
   ```

## Configuration

The template generates two types of configuration files:

### Environment Variables (.env)
Used for deployment and sensitive information:
- `OPENCTI_URL`: OpenCTI instance URL
- `OPENCTI_TOKEN`: Authentication token
- `CONNECTOR_ID`: Unique connector identifier
- `CONNECTOR_NAME`: Display name
- `CONNECTOR_LOG_LEVEL`: Logging level (debug, info, warning, error)
- `CONNECTOR_SCOPE`: Connector scope
- `CONNECTOR_DURATION_PERIOD`: Execution interval (ISO-8601 format)

### YAML Configuration (config.yml)
Structured configuration for the connector with OpenCTI settings, connector metadata, and custom connector-specific parameters.

## OpenCTI Connector Types

- **External Import**: Fetch data from external sources into OpenCTI
- **Internal Enrichment**: Enrich existing data within OpenCTI
- **Internal Export File**: Export data from OpenCTI to files
- **Internal Import File**: Import files into OpenCTI
- **Stream**: Process real-time data streams

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This template is available under the Apache License.

## Resources

- [OpenCTI Documentation](https://docs.opencti.io/)
- [OpenCTI Connectors](https://github.com/OpenCTI-Platform/connectors)
- [pycti Library](https://github.com/OpenCTI-Platform/client-python)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)