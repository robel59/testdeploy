# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from website import urls as wesiturl
from website import views as view
from payment import urls as nhj
from promotion import urls as promotio
from django.views.generic import TemplateView

urlpatterns = [

    #re_path(r'^schedule/', include('schedule.urls')),
    #re_path(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),

    path('admin/', admin.site.urls),          # Django admin route
    path("", include(("apps.authentication.urls", "account"),namespace='account')), # Auth routes - login / register
    path("", include(("home.urls", "main"),namespace='main')),
    path("", include("allauth.urls")),
    path('webuse/',include("webuser.urls")), #my app urls
    path('website/', include((wesiturl,'website'),namespace='website')),
    path('paypal/', include('paypal.standard.ipn.urls')),      
    path('payment/', include((nhj,'payment'),namespace='payment')),
    re_path(r'^getdatareport/', view.getdatareport),#api for get usernewuser
    path('newuser/<str:id>', view.newuser),
    path('storedata/<str:id>', view.storedata),#api for requesing from 
   
         # UI Kits Html files

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
