from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import (
    ListView, TemplateView, DetailView, CreateView, DeleteView, UpdateView,
    FormView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import TractorForm, ImplementForm
from .models import (Tractor, Implement, ImplementSubCategory,
                     TractorCategory, ImplementCategory)


class TractorListView(ListView):
    """A view for showing all the approved tractors.

    The owner must accept terms and conditions for it to be shown here.
    """
    queryset = Tractor.objects.filter(agree_terms=True, approved=True)


class TractorDetailView(DetailView):
    """A view for showing all details for a single tractor."""
    model = Tractor


class TractorAddView(LoginRequiredMixin, FormView):
    """A view for adding a Tractor.

    User must be logged in.
    """
    form_class = TractorForm
    template_name = 'equipments/tractor_form.html'
    success_url = reverse_lazy('equipments:tractors')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if request.method == 'POST':
            if form.is_valid():
                form.instance.user = self.request.user
                for file in files:
                    # to do
                    pass
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class TractorUpdateView(LoginRequiredMixin, UpdateView):
    model = Tractor
    form_class = TractorForm
    template_name = 'equipments/update_tractor_form.html'
    success_url = reverse_lazy('equipments:tractors')


class TractorDeleteView(LoginRequiredMixin, DeleteView):
    model = Tractor
    success_url = reverse_lazy('equipments:tractors')


class ImplementListView(ListView):
    """A view showing list of approved implements.

    The owner must accept terms and conditions for it to be shown here.
    """
<<<<<<< HEAD
    queryset = Implement.objects.filter(agree_terms=True, approved=True)
=======
    queryset = Implement.objects.filter(status='approved', agree_terms=True)
>>>>>>> 96ec1d7... resolve conflicts


class ImplementDetailView(DetailView):
    """A view for showing details of single implement."""
    model = Implement


class ImplementAddView(LoginRequiredMixin, CreateView):
    """A view for adding an Implement.

    User must be logged in.
    """
    form_class = ImplementForm
    template_name = 'equipments/implement_form.html'
    success_url = reverse_lazy('equipments:implements')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if request.method == 'POST':
            if form.is_valid():
                form.instance.user = self.request.user
                for file in files:
                    # to do
                    pass
                form.save()
                return self.form_valid(form)
            else:
                context = {
                    'form': form,
                }
                return render(request, 'equipments/implement_form.html', context)


class ImplementUpdateView(LoginRequiredMixin, UpdateView):
    model = Implement
    form_class = ImplementForm
    template_name = 'equipments/update_implement_form.html'
    success_url = reverse_lazy('equipments:implements')


class ImplementDeleteView(LoginRequiredMixin, DeleteView):
    model = Implement
    success_url = reverse_lazy('equipments:implements')


class TractorCategoryList(ListView):
    model = Tractor
    template_name = 'equipments/tractor_category_list.html'

    def get_queryset(self):
        self.tractor_type = get_object_or_404(TractorCategory, pk=self.kwargs['pk'])
        return Tractor.objects.filter(tractor_type=self.tractor_type)

    def get_context_data(self, **kwargs):
        context = super(TractorCategoryList, self).get_context_data(**kwargs)
        context['category'] = self.tractor_type
        return context


class ImplementCategoryList(ListView):
    model = Implement
    template_name = 'equipments/implement_category_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(ImplementCategory, pk=self.kwargs['pk'])
        return Implement.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(ImplementCategoryList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


def implement_subcategory(request):
    category_id = request.GET.get('category')
    subcategories = ImplementSubCategory.objects.filter(
        category_id=category_id).order_by('name')
    return render(request, 'equipments/subcategory.html', {'subcategories': subcategories})
