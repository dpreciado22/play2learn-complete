from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class MyAccountView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = "pages/my_account.html"
    success_url = reverse_lazy("pages:my-account")

    def get_object(self):
        return self.request.user

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "pages/register.html"
    success_url = reverse_lazy("login")