from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Review
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Review.objects.order_by("-created_at")
        featured = qs.filter(featured=True)
        ctx["review_list"] = featured if featured.exists() else qs[:10]
        return ctx

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

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ["text"]  # keep it simple
    template_name = "pages/review_form.html"
    success_url = reverse_lazy("pages:homepage")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContactView(TemplateView):
    template_name = "pages/contact.html"

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Contact from {form.cleaned_data['name']}",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@example.com"],  # or use settings.ADMINS
            )
            return TemplateView.as_view(template_name="pages/contact_thanks.html")(request)
        return self.get(request, form=form)

    def get(self, request, form=None, *args, **kwargs):
        return self.render_to_response({"form": form or ContactForm()})