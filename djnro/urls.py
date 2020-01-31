from django.conf.urls import include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the django admin interface:
from django.contrib import admin
admin.autodiscover()
import social_django.urls
import edumanage
import django
import accounts, accounts.views

urlpatterns = [
    url(r'^accounts/', include(social_django.urls, namespace='social')),
    url(r'^setlang/?$', edumanage.views.set_language, name='set_language'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^managelogin/(?P<backend>[^/]+)/$', edumanage.views.manage_login, name='manage_login'),
    url(r'^login/?', edumanage.views.user_login, name="login"),
    url(r'^altlogin/?', django.contrib.auth.views.login, {'template_name': 'overview/login.html'}, name="altlogin"),
    url(r'^logout/?', edumanage.views.user_logout, {'next_page': '/'}, name="logout"),
    url(r'^registration/accounts/activate/(?P<activation_key>\w+)/$', accounts.views.activate, name='activate_account'),
    url(
        r'^registration/activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'
    ),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('edumanage.urls')),
]
