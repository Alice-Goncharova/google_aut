
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
   path('admin/', admin.site.urls),
   path('oauth/', include('oauthapp.urls')),
   path('social-auth/', include('social_django.urls', namespace='social')),
]