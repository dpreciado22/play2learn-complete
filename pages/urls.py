from django.urls import path

from .views import AboutUsView, HomePageView, MyAccountView

app_name= 'pages'
urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('', HomePageView.as_view(), name='homepage'),
    path('account/', MyAccountView.as_view(), name='my-account'),
]