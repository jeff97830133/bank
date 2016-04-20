from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, main, login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$', home),
	url(r'^main/$', main),
	url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
)
