from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('tours/', views.tours, name='tours'),
    path('2-hour-tour/', views.two_hour, name='twohour'),
    path('3-hour-tour/', views.three_hour, name='threehour'),
    path('4-hour-tour/', views.four_hour, name='fourhour'),
    path('faq/', views.faq, name='faq'),
    path('how_it_works/', views.how, name='how'),
    path('who_we_are/', views.who, name='who'),
    path('contactus/', views.contact, name='contact'),
    path('success/', views.success, name='success')
]