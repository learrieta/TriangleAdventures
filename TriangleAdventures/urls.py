
from django.contrib import admin
from django.urls import path,include
from base.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static' : StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, { 'sitemaps' : sitemaps}),
    path('', include('base.urls'))
    
]
