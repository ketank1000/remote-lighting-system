from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='index'),
    # url(r'^website/', include('website.foo.urls')),
    url(r'^login/','auth.views.login_user',name='login'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'website.views.home',name='index'),
    url(r'^about/', 'website.views.about',name='about'),
    url(r'^blog/', 'website.views.blog',name='blog'),
    url(r'^contact/', 'website.views.contact',name='contact'),
    url(r'^register/', 'auth.views.register_user',name='register'),
    url(r'^connect_user/', 'auth.views.connect_user',name='connect_user'),
    url(r'^user_home/','auth.views.user_home',name='user_home'),
    url(r'^edit/','website.views.edit',name='edit'),
    url(r'^logout/','auth.views.logout',name='logout'),
    url(r'^view/','website.views.view',name='view'), 
    url(r'^user_contact/','website.views.user_contact',name='user_contact'),
    url(r'^settings/','website.views.settings',name='settings'), 
    url(r'^temp/','website.views.temp',name='temp'),
    url(r'^temp1/','website.views.temp1',name='temp1'),
    url(r'^tempgr/','website.views.tempgr',name='tempgr'),
    url(r'^update/','auth.views.update',name='update'),
    url(r'^edit_update/','auth.views.edit_update',name='edit_update'),
    url(r'^group_update/','auth.views.group_update',name='group_update'),
    url(r'^add_group/','auth.views.add_group',name='add_group'),
    url(r'^group_status/','auth.views.group_status',name='group_status'),
    url(r'^group/','website.views.group',name='group'),
    url(r'^automation/','website.views.automation',name='automation'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
