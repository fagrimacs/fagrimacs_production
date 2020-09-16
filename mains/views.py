from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from experts.models import ExpertProfile
from equipments.models import ImplementCategory, TractorCategory


class Homepage(TemplateView):
    template_name = 'mains/index.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['tractor_categories'] = TractorCategory.objects.all()
        context['implement_categories'] = ImplementCategory.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'mains/about.html'


class ExpertsList(ListView):
    model = ExpertProfile
