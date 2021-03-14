from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from login import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', core_views.home, name='home'),
    path("",include('django.contrib.auth.urls')),
]
