from django.urls import path

from .views import AboutUsView, HomePageView, MyAccountView

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about/", AboutUsView.as_view(), name="about-us"),
    path("register/", SignUpView.as_view(), name="register"),
    path("account/", MyAccountView.as_view(), name="my-account"),
]