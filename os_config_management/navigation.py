from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

items = (
    PluginMenuItem(
        link='plugins:netbox_os_config:configitem_list',
        link_text='Config Items',
        permissions=['netbox_os_config.view_configitem'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_os_config:configitem_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_os_config:configitem_import',
                title='Import',
                icon_class='mdi mdi-upload',
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_os_config:configset_list',
        link_text='Config Sets',
        permissions=['netbox_os_config.view_configset'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_os_config:configset_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_os_config:configset_import',
                title='Import',
                icon_class='mdi mdi-upload',
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_os_config:osconfig_list',
        link_text='OS Configurations',
        permissions=['netbox_os_config.view_osconfig'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_os_config:osconfig_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_os_config:osconfig_import',
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