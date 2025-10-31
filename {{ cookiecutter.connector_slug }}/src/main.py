from pycti import OpenCTIConnectorHelper
from {{ cookiecutter.connector_slug }}.settings import {{ cookiecutter.connector_pascal_case }}ConnectorSettings

if __name__ == "__main__":
    config = {{ cookiecutter.connector_pascal_case }}ConnectorSettings()
    helper = OpenCTIConnectorHelper(config=config.to_helper_config())
