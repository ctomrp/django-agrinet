from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("apps.products.urls")),
    path('producer_application/', include('apps.producer_application.urls')),
    path("sales/", include("apps.sales.urls")),
    path("users/", include("apps.users.urls")),
    path("", RedirectView.as_view(url="users/", permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
