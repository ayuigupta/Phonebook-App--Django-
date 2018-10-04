from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^contact_list$', views.contact_list, name='contact_list'),
    url(r'^add_contact$', views.contact_new, name='contact_new'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^contact/(?P<pk>\d+)/$', views.contact_detail, name='contact_detail'),
    url(r'^contact/(?P<pk>\d+)/edit/$', views.contact_edit, name='contact_edit'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.contact_delete, name='contact_delete')
]

