from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'authentication/register.html'  # comme un get() integré
    form_class = RegisterForm  # notre formulaire
    success_url = 'success'  # url de notre page de success

    def form_valid(self, form: form_class):
        form.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'authentication/registered.html'


class ConsultAccountView(TemplateView):
    template_name = 'authentication/account.html'

    def get(self, request):
        # url = '../../static/img/'
        return render(request, self.template_name, locals())
