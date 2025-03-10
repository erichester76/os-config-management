from django.urls import path
from . import views

urlpatterns = [
    # ConfigItem URLs
    path('config-items/', views.ConfigItemListView.as_view(), name='configitem_list'),
    path('config-items/add/', views.ConfigItemEditView.as_view(), name='configitem_add'),
    path('config-items/<int:pk>/', views.ConfigItemView.as_view(), name='configitem'),
    path('config-items/<int:pk>/edit/', views.ConfigItemEditView.as_view(), name='configitem_edit'),
    path('config-items/<int:pk>/delete/', views.ConfigItemDeleteView.as_view(), name='configitem_delete'),
    
    # ConfigSet URLs
    path('config-sets/', views.ConfigSetListView.as_view(), name='configset_list'),
    path('config-sets/add/', views.ConfigSetEditView.as_view(), name='configset_add'),
    path('config-sets/<int:pk>/', views.ConfigSetView.as_view(), name='configset'),
    path('config-sets/<int:pk>/edit/', views.ConfigSetEditView.as_view(), name='configset_edit'),
    path('config-sets/<int:pk>/delete/', views.ConfigSetDeleteView.as_view(), name='configset_delete'),
    
    # OSConfig URLs
    path('os-configs/', views.OSConfigListView.as_view(), name='osconfig_list'),
    path('os-configs/add/', views.OSConfigEditView.as_view(), name='osconfig_add'),
    path('os-configs/<int:pk>/', views.OSConfigView.as_view(), name='osconfig'),
    path('os-configs/<int:pk>/edit/', views.OSConfigEditView.as_view(), name='osconfig_edit'),
    path('os-configs/<int:pk>/delete/', views.OSConfigDeleteView.as_view(), name='osconfig_delete'),
]