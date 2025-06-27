import logging
from aiohttp.web import Response
from homeassistant.components.http import HomeAssistantView

from .const import (
    CONF_AUTOMATIONS_PATH,
    CONF_SCRIPTS_PATH,
    CONF_DEVICES_PATH,
)

_LOGGER = logging.getLogger(__name__)

class HassLensConnectorAPI(HomeAssistantView):
    """REST API to expose YAML files."""

    url = "/api/hasslens_connector/{yaml_type}"
    name = "api:hasslens_connector"
    requires_auth = True

    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry

    async def get(self, request, yaml_type):
        key_map = {
            "automations": CONF_AUTOMATIONS_PATH,
            "scripts": CONF_SCRIPTS_PATH,
            "devices": CONF_DEVICES_PATH,
        }

        if yaml_type not in key_map:
            return Response(status=404, text="Invalid YAML type")

        rel_path = self.entry.data.get(key_map[yaml_type])
        abs_path = self.hass.config.path(rel_path)

        try:
            with open(abs_path, "r", encoding="utf-8") as file:
                contents = file.read()
        except FileNotFoundError:
            return Response(status=404, text="File not found")
        except Exception:  # noqa: broad-except
            _LOGGER.exception("Failed to read %s", abs_path)
            return Response(status=500, text="Internal server error")

        return Response(text=contents, content_type="text/yaml")
