from django.urls import path
from . import views

app_name = 'os_config_management'

urlpatterns = [
    # ConfigItem URLs
    path('configitems/', views.ConfigItemListView.as_view(), name='configitem_list'),
    path('configitems/add/', views.ConfigItemEditView.as_view(), name='configitem_add'),
    path('configitems/<int:pk>/edit/', views.ConfigItemEditView.as_view(), name='configitem_edit'),
    path('configitems/<int:pk>/', views.ConfigItemDetailView.as_view(), name='configitem'),
    path('configitems/<int:pk>/changelog/', views.ConfigItemChangelogView.as_view(), name='configitem_changelog'),
    path('configitems/bulk/edit/', views.ConfigItemBulkEditView.as_view(), name='configitem_bulk_edit'),
    path('configitems/bulk/delete/', views.ConfigItemBulkDeleteView.as_view(), name='configitem_bulk_delete'),
    path('configitems/import/', views.ConfigItemImportView.as_view(), name='configitem_import'),

    # Configuration URLs
    path('configurations/', views.ConfigurationListView.as_view(), name='configuration_list'),
    path('configurations/add/', views.ConfigurationEditView.as_view(), name='configuration_add'),
    path('configurations/<int:pk>/edit/', views.ConfigurationEditView.as_view(), name='configuration_edit'),
    path('configurations/<int:pk>/', views.ConfigurationDetailView.as_view(), name='configuration'),
    path('configurations/<int:pk>/changelog/', views.ConfigurationChangelogView.as_view(), name='configuration_changelog'),
    path('configurations/bulk/edit/', views.ConfigurationBulkEditView.as_view(), name='configuration_bulk_edit'),
    path('configurations/bulk/delete/', views.ConfigurationBulkDeleteView.as_view(), name='configuration_bulk_delete'),
    path('configurations/import/', views.ConfigurationImportView.as_view(), name='configuration_import'),
]