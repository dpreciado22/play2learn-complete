from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("games/", include(("games.urls", "games"), namespace="games")),
    path("", include(("pages.urls", "pages"), namespace="pages")),

    # built-in auth (simple and fast)
    path("accounts/login/",  auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]