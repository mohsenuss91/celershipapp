from . import settings
from home.views import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', AboutPageView.as_view(), name='home'),
    path('app', CelerAppView.as_view(), name='app'),
    path('sec', CelerSecView.as_view(), name='sec'),
    path('web', CelerWebView.as_view(), name='web'),
    path('dee', CelerDeeView.as_view(), name='dee'),
    path('services', ServicesView.as_view(), name='services'),
    path('contact', ContactView.as_view(), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
