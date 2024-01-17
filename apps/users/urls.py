from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("client/", views.client_dashboard, name="client_dashboard"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    path("logout/", views.custom_logout, name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("producer/", views.producer_dashboard, name="producer_dashboard"),
    path("register_client/", views.user_client_registration, name="client_register_form"),
    path("register_producer/", views.user_producer_registration, name="producer_register_form"),
    path("", views.CustomLoginView.as_view(), name="login"),
    path("search_results/", views.SearchResultsView.as_view(), name="search_results"),
    path("unauthorized_access/", views.unauthorized_access, name="unauthorized_access"),
    path("client/<int:product_id>", views.client_product_detail, name="client_product_detail"),
]

