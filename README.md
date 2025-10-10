# HassLens Connector

HassLens Connector is a Home Assistant custom integration that exposes your automation, script and device YAML files through a simple API. The integration is configured through the Home Assistant UI.

It is designed to work with the [HassLens](https://hasslens.com) application, which provides a dashboard for visualizing and managing your Home Assistant entities.

## Features
- Provides a secured REST endpoint for retrieving configuration files for use in the HassLens application.

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
Go to **Settings → Devices & Services → Add Integration** and search for "HassLens Connector".

When configuring you will be asked to provide paths for your automations, scripts, and devices files. The form is prefilled with defaults; if you accept the prefilled values they will be saved. These default values will work for most Home Assistant installations.

Defaults:
- Automations: `automations.yaml`
- Scripts: `scripts.yaml`
- Devices: `.storage/core.device_registry`

API endpoint
- The integration exposes: `/api/hasslens_connector/{yaml_type}` where `{yaml_type}` is `automations`, `scripts`, or `devices`.
- The endpoint requires authentication which will be handled by Home Assistant's long-lived access tokens (configured through your HassLens account). 

## Privacy
This integration only reads the files that you specify. No files are modified, and data is sent securely to your HassLens application dashboard.  

## License
MIT (see `LICENSE`)
