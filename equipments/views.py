from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import (
    ListView, TemplateView, DetailView, CreateView, DeleteView, UpdateView,
    FormView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import TractorForm, ImplementForm
from .models import (Tractor, Implement, ImplementSubCategory,
                     TractorCategory, ImplementCategory)


class AddTractorView(LoginRequiredMixin, FormView):
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



class ImplementView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        if self.request.user.role == 'owner':
            return True


def implement_subcategory(request):
    category_id = request.GET.get('category')
    subcategories = ImplementSubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'equipments/subcategory.html', {'subcategories': subcategories})


class ListTractor(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Tractor
    template_name = 'equipments/tractors.html'
    context_object_name = 'tractors'

    def get_queryset(self, *args, **kwargs):
        return Tractor.objects.all().filter(user=self.request.user)

    def test_func(self):
        if self.request.user.role == 'owner':
            return True


class TractorDetailView(DetailView):
    model = Tractor
    template_name = 'equipments/tractor_detail.html'
    context_object_name = 'tractor'

    def get_context_data(self, **kwargs):
        context = super(TractorDetailView, self).get_context_data(**kwargs)
        context['tractors'] = Tractor.objects.all()
        return context


class ImplementDetailView(DetailView):
    model = Implement
    template_name = 'equipments/implement_detail.html'
    context_object_name = 'implement'

    def get_context_data(self, **kwargs):
        context = super(ImplementDetailView, self).get_context_data(**kwargs)
        context['implements'] = Implement.objects.all()
        return context


class ListImplement(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Implement
    template_name = 'equipments/implements.html'
    context_object_name = 'implements'

    def get_queryset(self, *args, **kwargs):
        return Implement.objects.all().filter(user=self.request.user)

    def test_func(self):
        return self.request.user.role == 'owner'


class UpdateTractor(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = TractorForm
    template_name = 'equipments/update_tractor_form.html'
    success_url = reverse_lazy('equipments:tractors')
    queryset = Tractor.objects.all()

    def test_func(self):
        return self.request.user.role == 'owner'


class UpdateImplement(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ImplementForm
    template_name = 'equipments/update_implement_form.html'
    success_url = reverse_lazy('equipments:implements')
    queryset = Implement.objects.all()

    def test_func(self):
        if self.request.user.role == 'owner':
            return True


class DeleteTractor(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tractor
    success_url = reverse_lazy('equipments:tractors')

    def test_func(self):
        if self.request.user.role == 'owner':
            return True


class DeleteImplement(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Implement
    success_url = reverse_lazy('equipments:implements')

    def test_func(self):
        if self.request.user.role == 'owner':
            return True


class TractorListHome(TemplateView):
    template_name = 'equipments/tractor_list.html'

    def get_context_data(self, **kwargs):
        context = super(TractorListHome, self).get_context_data(**kwargs)
        context['tractors'] = Tractor.objects.all()
        return context


class ImplementListHome(TemplateView):
    template_name = 'equipments/implement_list.html'

    def get_context_data(self, **kwargs):
        context = super(ImplementListHome, self).get_context_data(**kwargs)
        context['implements'] = Implement.objects.all()
        return context


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
