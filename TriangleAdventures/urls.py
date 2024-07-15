
from django.contrib import admin
from django.urls import path,include
from base.sitemaps import StaticSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static' : StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, { 'sitemaps' : sitemaps}, name= 'django.contrib.sitemaps.views.sitemap'),
    path('', include('base.urls'))
    
]
