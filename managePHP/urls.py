from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loadPHPHome, name='loadPHPHome'),
    url(r'^installExtensions', views.installExtensions, name='installExtensions'),
    url(r'^V2/installExtensionsV2', views.installExtensionsV2, name='installExtensionsV2'),
    url(r'^getExtensionsInformation', views.getExtensionsInformation, name='getExtensionsInformation'),
    url(r'^submitExtensionRequest', views.submitExtensionRequest, name='submitExtensionRequest'),
    url(r'^getRequestStatus', views.getRequestStatus, name='getRequestStatus'),
    url(r'^editPHPConfigs', views.editPHPConfigs, name='editPHPConfigs'),
    url(r'^V2/editPHPConfigsV2', views.editPHPConfigsV2, name='editPHPConfigsV2'),
    url(r'^getCurrentPHPConfig', views.getCurrentPHPConfig, name='getCurrentPHPConfig'),
    url(r'^savePHPConfigBasic', views.savePHPConfigBasic, name='savePHPConfigBasic'),
    url(r'^getCurrentAdvancedPHPConfig', views.getCurrentAdvancedPHPConfig, name='getCurrentAdvancedPHPConfig'),
    url(r'^savePHPConfigAdvance', views.savePHPConfigAdvance, name='savePHPConfigAdvance'),
    url(r'^restartPHP', views.restartPHP, name='restartPHP'),

]
