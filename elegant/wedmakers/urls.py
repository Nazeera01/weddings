from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns =  [

        path('', views.home,name='home'),
        path('contact/', views.contact, name='contact'),
        path('about/', views.about, name='about'),
        path('client_register/',views.client_register,name='client_register'),
        path('event_register/',views.event_register,name='event_register'),
        path('vendor_register/',views.vendor_register,name='vendor_register'),
        path('venue_register/',views.venue_register,name='venue_register'),
        path('vendor/',views.vendor,name='vendor'),
        path('venue/',views.venue,name='venue'),
        path('register/',views.user_register,name='register'),
        path('vendor_page/',views.vendor_page,name='vendor_page'),
        path('venue_page/',views.venue_page,name='venue_page'),
        path('login/', views.user_login, name='login'),
        path('logout/',views.user_logout, name='logout'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)