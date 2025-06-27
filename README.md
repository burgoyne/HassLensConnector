# HassLens Connector

HassLens Connector is a Home Assistant custom integration that exposes your automation, script and device YAML files through a simple API. The integration is configured through the Home Assistant UI.

## Features
- Config flow setup via the UI
- Provides a secured REST endpoint for retrieving YAML files

## Installation
### HACS
1. In HACS, open **Integrations** and select **Custom repositories** from the menu.
2. Add this repository URL and set the category to `Integration`.
3. Search for "HassLens Connector" and install.
4. Restart Home Assistant.

### Manual
1. Copy the `custom_components/hasslens_connector` directory to your Home Assistant `custom_components` folder.
2. Restart Home Assistant.

## Configuration
Go to **Settings → Devices & Services → Add Integration** and search for "HassLens Connector". Enter paths for your automations, scripts and devices YAML files (defaults are provided).

## Privacy
This integration only reads the YAML files that you specify. No data is sent externally.

## License
MIT (see `LICENSE`)
