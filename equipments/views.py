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
    queryset = Tractor.objects.approved()


class UserTractorListView(LoginRequiredMixin, ListView):
    """A view for showing tractors added by a particular user.

    - User must be logged in.
    """
    template_name = 'equipments/user_tractor_list.html'

    def get_queryset(self):
        return Tractor.objects.filter(user=self.request.user)


class TractorDetailView(DetailView):
    """A view for showing all details for a single tractor."""
    model = Tractor


class TractorAddView(LoginRequiredMixin, CreateView):
    """A view for adding a Tractor.

    - User must be logged in.
    """
    form_class = TractorForm
    template_name = 'equipments/tractor_form.html'
    success_url = reverse_lazy('equipments:user-tractors-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TractorUpdateView(LoginRequiredMixin, UpdateView):
    """A view for updating a tractor.

    - User must be logged in.
    - User can update the tractor he/she added only.
    """
    form_class = TractorForm
    template_name = 'equipments/update_tractor_form.html'
    success_url = reverse_lazy('equipments:user-tractors-list')

    def get_queryset(self):
        return Tractor.objects.filter(user=self.request.user)


class TractorDeleteView(LoginRequiredMixin, DeleteView):
    """A view to confirm deletion of the Tractor.

    - User must be logged in.
    - User can delete the tractor he/she added only.
    """
    success_url = reverse_lazy('equipments:user-tractors-list')

    def get_queryset(self):
        return Tractor.objects.filter(user=self.request.user)


class ImplementListView(ListView):
    """A view showing list of approved implements.

    The owner must accept terms and conditions for it to be shown.
    """
    queryset = Implement.objects.filter(agree_terms=True, approved=True)


class UserImplementListView(LoginRequiredMixin, ListView):
    """A view for showing implements added by a particular user.

    - User must be logged in.
    """
    template_name = 'equipments/user_implement_list.html'

    def get_queryset(self):
        return Implement.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ImplementDetailView(DetailView):
    """A view for showing details of single implement."""
    model = Implement


class ImplementAddView(LoginRequiredMixin, CreateView):
    """A view for adding an Implement.

    - User must be logged in.
    """
    form_class = ImplementForm
    template_name = 'equipments/implement_form.html'
    success_url = reverse_lazy('equipments:user-implements-list')


class ImplementUpdateView(LoginRequiredMixin, UpdateView):
    """A view to update the implement.

    - User must be logged in.
    - User can update the tractor he/she added only.
    """
    form_class = ImplementForm
    template_name = 'equipments/update_implement_form.html'
    success_url = reverse_lazy('equipments:user-implements-list')

    def get_queryset(self):
        return Implement.objects.filter(user=self.request.user)


class ImplementDeleteView(LoginRequiredMixin, DeleteView):
    """A view to confirm deletion of the Implement.

    - User must be logged in.
    - User can delete the implement he/she added only.
    """
    success_url = reverse_lazy('equipments:user-implements-list')

    def get_queryset(self):
        return Implement.objects.filter(user=self.request.user)


class TractorCategoryList(ListView):
    model = Tractor
    template_name = 'equipments/tractor_category_list.html'

    def get_queryset(self):
        self.tractor_type = get_object_or_404(
            TractorCategory, pk=self.kwargs['pk'])
        return Tractor.objects.filter(tractor_type=self.tractor_type)

    def get_context_data(self, **kwargs):
        context = super(TractorCategoryList, self).get_context_data(**kwargs)
        context['category'] = self.tractor_type
        return context


class ImplementCategoryList(ListView):
    template_name = 'equipments/implement_category_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(
            ImplementCategory, pk=self.kwargs['pk'])
        return Implement.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def implement_subcategory(request):
    category_id = request.GET.get('category')
    subcategories = ImplementSubCategory.objects.filter(
        category_id=category_id).order_by('name')
    return render(request, 'equipments/subcategory.html',
                  {'subcategories': subcategories})
