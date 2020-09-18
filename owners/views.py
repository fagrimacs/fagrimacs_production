from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import OwnerProfileForm
from .models import OwnerProfile
from accounts.forms import UserUpdateForm

User = get_user_model()


class OwnerDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'owners/dashboard.html'

    def test_func(self):
        owner = User.objects.get(email=self.request.user)
        owner_profile = OwnerProfile.objects.filter(user=owner)
        if self.request.user.role == 'owner' and self.request.user.ownerprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect('owners:update-profile',kwargs={'pk': self.request.user.id})


class OwnerProfileView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': OwnerProfileForm(instance=request.user.ownerprofile)
        }
        return render(request, 'owners/profile_form.html', context)


    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = OwnerProfileForm(request.POST, request.FILES, instance=request.user.ownerprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect(reverse('owners:profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = OwnerProfileUpdateForm(instance=request.user.ownerprofile)


    def test_func(self):
        if self.request.user.ownerprofile == OwnerProfile.objects.get(user_id=self.request.user.id):
            return True
        return False


class OwnerProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = OwnerProfile
    template_name = 'owners/profile.html'
    context_object_name = 'owner_profile'

    def test_func(self):
        owner = User.objects.get(email=self.request.user)
        owner_profile = OwnerProfile.objects.filter(user=owner)
        if self.request.user.ownerprofile == OwnerProfile.objects.get(user_id=self.request.user.id) and self.request.user.ownerprofile.region != '':
            return True

    def handle_no_permission(self):
        return redirect(reverse('owners:update-profile', kwargs={'pk': self.request.user.id}))
