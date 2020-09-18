from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import AdminProfileForm
from .models import AdminProfile
from accounts.forms import UserUpdateForm

User = get_user_model()


class AdminDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admins/dashboard.html'

    def test_func(self):
        admin = User.objects.get(email=self.request.user)
        admin_profile = AdminProfile.objects.filter(user=admin)
        if self.request.user.role == 'admin' and self.request.user.adminprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('admins:update-profile', kwargs={'pk': self.request.user.id}))


class AdminProfileView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': AdminProfileForm(instance=request.user.adminprofile)
        }
        return render(request, 'admins/profile_form.html', context)


    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = AdminProfileForm(request.POST, request.FILES, instance=request.user.adminprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect(reverse('admins:profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = AdminProfileUpdateForm(instance=request.user.adminprofile)


    def test_func(self):
        if self.request.user.adminprofile == AdminProfile.objects.get(user_id=self.request.user.id):
            return True
        return False


class AdminProfileDetailView(LoginRequiredMixin,
                             UserPassesTestMixin, DetailView):
    model = AdminProfile
    template_name = 'admins/profile.html'
    context_object_name = 'admin_profile'

    def test_func(self):
        admin = User.objects.get(email=self.request.user)
        admin_profile = AdminProfile.objects.filter(user=admin)
        if self.request.user.adminprofile == AdminProfile.objects.get(user_id=self.request.user.id) and self.request.user.adminprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('admins:update-profile', kwargs={'pk': self.request.user.id}))
