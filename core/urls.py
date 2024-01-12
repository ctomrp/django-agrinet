from django.contrib import admin
from django.urls import path,include


urlpatterns = [

    path("admin/", admin.site.urls),
    path('producer_application/', include('apps.producer_application.urls')),
    
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.urls')),

]
