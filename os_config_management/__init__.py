from netbox.plugins import PluginConfig

class OSMgmtConfig(PluginConfig):
    name = 'os_config_management'
    verbose_name = 'OS Config Management'
    description = 'Netbox Plugin for Configuring OS-level Configuration Hierarchies for Virtual Machines'
    version = '0.1.0'
    author = 'Eric Hester'
    author_email = 'hester1@clemson.edu'
    base_url = 'config_management'
    min_version = '4.1.0'
    max_version = '4.2.99'

config = OSMgmtConfig