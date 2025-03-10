from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

items = (
    PluginMenuItem(
        link='plugins:netbox_os_config:configitem_list',
        link_text='Config Items',
        permissions=['netbox_os_config.view_configitem']
    ),
    PluginMenuItem(
        link='plugins:netbox_os_config:configset_list',
        link_text='Config Sets',
        permissions=['netbox_os_config.view_configset']
    ),
    PluginMenuItem(
        link='plugins:netbox_os_config:osconfig_list',
        link_text='OS Configurations',
        permissions=['netbox_os_config.view_osconfig']
    ),
)

menu = PluginMenu(
    label='OS Configuration Management',
    icon_class='mdi mdi-harddisk',
    groups=(('OS Configuration', items),)
)