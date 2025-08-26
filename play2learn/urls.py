from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("pages.urls")),
        path("accounts/login/",
         auth_views.LoginView.as_view(template_name="pages/login.html"),
         name="login"),
    path("accounts/logout/",
         auth_views.LogoutView.as_view(next_page="pages:homepage"),
         name="logout"),
]
