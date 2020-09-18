from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import FarmerProfileForm
from .models import FarmerProfile
from accounts.forms import UserUpdateForm

User = get_user_model()


class FarmerDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'farmers/dashboard.html'

    # def test_func(self):
    #     farmer = User.objects.get(email=self.request.user)
    #     farmer_profile = FarmerProfile.objects.filter(user=farmer)
    #     if self.request.user.role == 'farmer' and self.request.user.farmerprofile.region != '':
    #         return True

    def handle_no_permission(self):
        return redirect(reverse('farmers:update-profile', kwargs={'pk': self.request.user.id}))



class FarmerProfileView(LoginRequiredMixin, View):

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': FarmerProfileForm(instance=request.user.farmerprofile)
        }
        return render(request, 'farmers/profile_form.html', context)


    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = FarmerProfileForm(request.POST, request.FILES, instance=request.user.farmerprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect(reverse('farmers:profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = FarmerProfileUpdateForm(instance=request.user.farmerprofile)


    # def test_func(self):
    #     if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.request.user.id):
    #         return True
    #     return False


class FarmerProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FarmerProfile
    template_name = 'farmers/profile.html'
    context_object_name = 'farmer_profile'

    def test_func(self):
        farmer = User.objects.get(email=self.request.user)
        farmer_profile = FarmerProfile.objects.filter(user=farmer)
        if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.request.user.id) and self.request.user.farmerprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('farmers:update-profile', kwargs={'pk': self.request.user.id}))
