from django.conf.urls import patterns, include, url
from django.contrib import admin

from gaadi.views.dashboard import dashboard
from gaadi.views.login import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gaadi_panel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login.login,name="login" ),
    url(r'^dashboard/', dashboard.dashboard,name="dashboard" ),
    url(r'^logout/', login.logout,name="logout" ),
)
