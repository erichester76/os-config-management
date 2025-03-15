from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

items = (
    PluginMenuItem(
        link='plugins:os_config_management:configitem_list',
        link_text='Config Items',
        permissions=['os_config_management.view_configitem'],
        buttons=(
            PluginMenuButton(
                link='plugins:os_config_management:configitem_bulk_edit',
                title='Bulk Edit',
                icon_class='mdi mdi-edit',
                color='blue',
                permissions=['os_config_management.change_configitem']
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configitem_bulk_delete',
                title='Bulk Delete',
                icon_class='mdi mdi-trash',
                color='red',
                permissions=['os_config_management.delete_configitem']
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configitem_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color='green',
                permissions=['os_config_management.add_configitem']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:os_config_management:configuration_list',
        link_text='Configurations',
        permissions=['os_config_management.view_configuration'],
        buttons=(
            PluginMenuButton(
                link='plugins:os_config_management:configuration_bulk_edit',
                title='Bulk Edit',
                icon_class='mdi mdi-edit',
                color='blue',
                permissions=['os_config_management.change_configuration']
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configuration_bulk_delete',
                title='Bulk Delete',
                icon_class='mdi mdi-trash',
                color='red',
                permissions=['os_config_management.delete_configuration']
            ),
            PluginMenuButton(
                link='plugins:os_config_management:configuration_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color='green',
                permissions=['os_config_management.add_configuration']
            ),
        )
    ),
)

menu = PluginMenu(
    label='Config Management',
    icon_class='mdi mdi-harddisk',
    groups=(('Configurations', items),)
)