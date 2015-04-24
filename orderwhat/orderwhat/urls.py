from django.conf.urls import patterns, include, url
from django.contrib import admin
import views as coreviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orderwhat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', coreviews.SplashView.as_view())
)
