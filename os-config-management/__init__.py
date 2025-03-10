from netbox.plugins import PluginConfig

class OSConfigConfig(PluginConfig):
    name = 'os_config_management'
    verbose_name = 'OS Configuration Hierarchy'
    description = 'A plugin to manage OS-level configuration hierarchies for virtual machines.'
    version = '0.1'
    author = 'Eric hester'
    author_email = 'hester1@clemson.edu'
    base_url = 'os-config'
    required_settings = []
    default_settings = {}

config = OSConfigConfig