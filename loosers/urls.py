from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from athar_app import views as athar_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', athar_views.index, name='index'),
    path('athar/', include('athar_app.urls')),
    path('account/', include('user_app.urls')),
    path('contact', athar_views.contact, name='contact'),
    path('about-us', athar_views.about, name='about'),
]
