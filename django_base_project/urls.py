from django_api_admin.sites import site
from django.urls import path, include

urlpatterns = [
    path('admin/', site.urls),
    path('apps/', include('apps.urls')),
]
