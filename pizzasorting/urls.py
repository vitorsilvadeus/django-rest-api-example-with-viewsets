from django.urls import include, path
from django.contrib import admin
from .api import router

app_name = 'pizza'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
