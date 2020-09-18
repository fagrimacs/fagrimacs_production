from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import ExpertProfileForm
from .models import ExpertProfile
from accounts.forms import UserUpdateForm


class ExpertDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'experts/dashboard.html'

    def test_func(self):
        expert = User.objects.get(email=self.request.user)
        expert_profile = ExpertProfile.objects.filter(user=expert)
        if self.request.user.role == 'expert' and self.request.user.expertprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('experts:update-profile', kwargs={'pk': self.request.user.id}))



class ExpertProfileView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': ExpertProfileForm(instance=request.user.expertprofile)
        }
        return render(request, 'experts/profile_form.html', context)


    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ExpertProfileForm(request.POST, request.FILES, instance=request.user.expertprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect(reverse('experts:profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ExpertProfileUpdateForm(instance=request.user.expertprofile)


    def test_func(self):
        if self.request.user.expertprofile == ExpertProfile.objects.get(user_id=self.request.user.id):
            return True
        return False


class ExpertProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ExpertProfile
    template_name = 'experts/profile.html'
    context_object_name = 'expert_profile'

    def test_func(self):
        expert = CustomUser.objects.get(email=self.request.user)
        expert_profile = ExpertProfile.objects.filter(user=expert)
        if self.request.user.expertprofile == ExpertProfile.objects.get(user_id=self.request.user.id) and self.request.user.expertprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('experts:update-profile', kwargs={'pk': self.request.user.id}))
