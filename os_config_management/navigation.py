from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

items = (
    PluginMenuItem(
        link='plugins:os_config_management:configitem_list',
        link_text='Config Items',
        permissions=['netbox_os_config.view_configitem'],
        buttons=(
            PluginMenuButton(
                link='plugins:os_config_management:configitem_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configitem_import',
                title='Import',
                icon_class='mdi mdi-upload',
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:os_config_management:configset_list',
        link_text='Config Sets',
        permissions=['netbox_os_config.view_configset'],
        buttons=(
            PluginMenuButton(
                link='plugins:os_config_management:configset_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configset_import',
                title='Import',
                icon_class='mdi mdi-upload',
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:os_config_management:osconfig_list',
        link_text='OS Configurations',
        permissions=['netbox_os_config.view_osconfig'],
        buttons=(
            PluginMenuButton(
                link='plugins:os_config_management:osconfig_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:os_config_management:osconfig_import',
                title='Import',
                icon_class='mdi mdi-upload',
            ),
        )
    ),
)

menu = PluginMenu(
    label='OS Config Management',
    icon_class='mdi mdi-harddisk',
    groups=(('OS Configuration', items),)
)