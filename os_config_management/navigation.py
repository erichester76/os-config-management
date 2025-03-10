from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

items = (
    PluginMenuItem(
        link='plugins:os_config_management:configitem_list',
        link_text='Config Items',
        permissions=['os_config_management.view_configitem']
    ),
    PluginMenuItem(
        link='plugins:os_config_management:configset_list',
        link_text='Config Sets',
        permissions=['os_config_management.view_configset']
    ),
    PluginMenuItem(
        link='plugins:os_config_management:osconfig_list',
        link_text='OS Configurations',
        permissions=['os_config_management.view_osconfig']
    ),
)

menu = PluginMenu(
    label='OS Configuration Management',
    icon_class='mdi mdi-harddisk',
    groups=(('OS Configuration', items),)
)