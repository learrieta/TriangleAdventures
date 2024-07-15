from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse 

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home_page','tours','twohour','threehour','fourhour','faq','how','who','contact','success']
    
    def location(self, item):
        return reverse(item)