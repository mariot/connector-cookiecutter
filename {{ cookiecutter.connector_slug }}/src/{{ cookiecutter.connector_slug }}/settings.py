from pydantic import Field
from pydantic_settings import BaseSettings

from connectors_sdk import BaseConnectorSettings

{%- if cookiecutter.connector_type == "External Import" -%}
from connectors_sdk import BaseExternalImportConnectorConfig
{%- elif cookiecutter.connector_type == "Internal Enrichment" -%}
from connectors_sdk import BaseInternalEnrichmentConnectorConfig
{%- elif cookiecutter.connector_type == "Internal Export File" -%}
from connectors_sdk import BaseInternalExportFileConnectorConfig
{%- elif cookiecutter.connector_type == "Internal Import File" -%}
from connectors_sdk import BaseInternalImportFileConnectorConfig
{%- elif cookiecutter.connector_type == "Stream" -%}
from connectors_sdk import BaseStreamConnectorConfig
{% endif %}


class APIConfig(BaseSettings):
    """
    Define config vars specific to {{ cookiecutter.connector_name }}
    """

    api_base_url: str = Field(description="API key for authentication")


class {{ cookiecutter.connector_pascal_case }}ConnectorSettings(BaseConnectorSettings):
    """
    Override `BaseConnectorSettings` to include additional configuration parameters specific to the connector.
    """

    {%- if cookiecutter.connector_type == "External Import" -%}
    connector: BaseExternalImportConnectorConfig = Field(default_factory=BaseExternalImportConnectorConfig)
    {%- elif cookiecutter.connector_type == "Internal Enrichment" -%}
    connector: BaseInternalEnrichmentConnectorConfig = Field(default_factory=BaseInternalEnrichmentConnectorConfig)
    {%- elif cookiecutter.connector_type == "Internal Export File" -%}
    connector: BaseInternalExportFileConnectorConfig = Field(default_factory=BaseInternalExportFileConnectorConfig)
    {%- elif cookiecutter.connector_type == "Internal Import File" -%}
    connector: BaseInternalImportFileConnectorConfig = Field(default_factory=BaseInternalImportFileConnectorConfig)
    {%- elif cookiecutter.connector_type == "Stream" -%}
    connector: BaseStreamConnectorConfig = Field(default_factory=BaseStreamConnectorConfig)
    {% endif %}

    {{ cookiecutter.connector_slug }}: APIConfig = Field(default_factory=APIConfig)
