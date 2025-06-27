import voluptuous as vol
from homeassistant import config_entries

from .const import (
    DOMAIN,
    CONF_AUTOMATIONS_PATH,
    CONF_SCRIPTS_PATH,
    CONF_DEVICES_PATH,
)

DEFAULTS = {
    CONF_AUTOMATIONS_PATH: "automations.yaml",
    CONF_SCRIPTS_PATH: "scripts.yaml",
    CONF_DEVICES_PATH: "devices.yaml",
}

class HassLensConnectorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HassLens Connector."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="HassLens Connector", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_AUTOMATIONS_PATH, default=DEFAULTS[CONF_AUTOMATIONS_PATH]): str,
            vol.Required(CONF_SCRIPTS_PATH, default=DEFAULTS[CONF_SCRIPTS_PATH]): str,
            vol.Required(CONF_DEVICES_PATH, default=DEFAULTS[CONF_DEVICES_PATH]): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema)
