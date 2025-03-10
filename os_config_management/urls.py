from django.urls import path
from . import views
from . import models

urlpatterns = [
    # ConfigItem URLs
    path('config-items/', views.ConfigItemListView.as_view(), name='configitem_list'),
    path('config-items/add/', views.ConfigItemEditView.as_view(), name='configitem_add'),
    path('config-items/import/', views.ConfigItemImportView.as_view(), name='configitem_import'),
    path('config-items/<int:pk>/', views.ConfigItemView.as_view(), name='configitem'),
    path('config-items/<int:pk>/edit/', views.ConfigItemEditView.as_view(), name='configitem_edit'),
    path('config-items/<int:pk>/delete/', views.ConfigItemDeleteView.as_view(), name='configitem_delete'),
    path('config-items/bulk-edit/', views.ConfigItemBulkEditView.as_view(), name='configitem_bulk_edit'),
    path('config-items/bulk-delete/', views.ConfigItemBulkDeleteView.as_view(), name='configitem_bulk_delete'),
    path('config-items/<int:pk>/changelog/', views.ConfigItemChangeLogView.as_view(), name='configitem_changelog', kwargs={'model': models.ConfigItem}),

    # ConfigSet URLs
    path('config-sets/', views.ConfigSetListView.as_view(), name='configset_list'),
    path('config-sets/add/', views.ConfigSetEditView.as_view(), name='configset_add'),
    path('config-sets/import/', views.ConfigSetImportView.as_view(), name='configset_import'),
    path('config-sets/<int:pk>/', views.ConfigSetView.as_view(), name='configset'),
    path('config-sets/<int:pk>/edit/', views.ConfigSetEditView.as_view(), name='configset_edit'),
    path('config-sets/<int:pk>/delete/', views.ConfigSetDeleteView.as_view(), name='configset_delete'),
    path('config-sets/bulk-edit/', views.ConfigSetBulkEditView.as_view(), name='configset_bulk_edit'),
    path('config-sets/bulk-delete/', views.ConfigSetBulkDeleteView.as_view(), name='configset_bulk_delete'),
    path('config-sets/<int:pk>/changelog/', views.ConfigSetChangeLogView.as_view(), name='configset_changelog', kwargs={'model': models.ConfigSet}),
    
    # OSConfig URLs
    path('os-configs/', views.OSConfigListView.as_view(), name='osconfig_list'),
    path('os-configs/add/', views.OSConfigEditView.as_view(), name='osconfig_add'),
    path('os-configs/import/', views.OSConfigImportView.as_view(), name='osconfig_import'),
    path('os-configs/<int:pk>/', views.OSConfigView.as_view(), name='osconfig'),
    path('os-configs/<int:pk>/edit/', views.OSConfigEditView.as_view(), name='osconfig_edit'),
    path('os-configs/<int:pk>/delete/', views.OSConfigDeleteView.as_view(), name='osconfig_delete'),
    path('os-configs/bulk-edit/', views.OSConfigBulkEditView.as_view(), name='osconfig_bulk_edit'),
    path('os-configs/bulk-delete/', views.OSConfigBulkDeleteView.as_view(), name='osconfig_bulk_delete'),
    path('os-configs/<int:pk>/changelog/', views.OSConfigChangeLogView.as_view(), name='osconfig_changelog', kwargs={'model': models.OSConfig}),    
]