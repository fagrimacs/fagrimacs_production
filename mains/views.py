from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.messages.views import SuccessMessageMixin

from experts.models import ExpertProfile
from equipments.models import ImplementCategory, TractorCategory

from mains.forms import ContactForm


class Homepage(TemplateView):
    template_name = 'mains/index.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['tractor_categories'] = TractorCategory.objects.all()
        context['implement_categories'] = ImplementCategory.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'mains/about.html'


class ContactUsView(SuccessMessageMixin, FormView):
    template_name = 'mains/contact.html'
    form_class = ContactForm
    success_url = '/'
    success_message = ('Thank you for contacting us. '
                       'We will get to you shortly.')

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ExpertsList(ListView):
    model = ExpertProfile
