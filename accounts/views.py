from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import EmailMessage
from django.shortcuts import render, reverse
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import TemplateView

from accounts.forms import SignUpForm
from accounts.models import CustomUser
from accounts.tokens import account_activation_token
from farmers.models import FarmerProfile
from owners.models import OwnerProfile
from experts.models import ExpertProfile
from admins.models import AdminProfile


class UserLoginView(LoginView):
    """View for user to login in platform """
    template_name = 'accounts/login.html'


    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.role == 'farmer':
            if self.request.user.farmerprofile.region == '':
                return reverse('farmers:update-profile', kwargs={'pk': self.request.user.pk})
            else:
                return reverse('farmers:dashboard')
        elif self.request.user.role == 'owner':
            if self.request.user.ownerprofile.region == '':
                return reverse('owners:update-profile', kwargs={'pk': self.request.user.pk})
            else:
                return reverse('owners:dashboard')
        elif self.request.user.role == 'expert':
            if self.request.user.expertprofile.region == '':
                return reverse('experts:update-profile', kwargs={'pk': self.request.user.pk})
            else:
                return reverse('experts:dashboard')
        elif self.request.user.role == 'admin':
            if self.request.user.adminprofile.region == '':
                return reverse('admins:update-profile', kwargs={'pk': self.request.user.pk})
            else:
                return reverse('admins:dashboard')
        else:
            return f'/admin/'



def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data['email']
        user.save()

        # Create profile
        role = request.POST.get('role')
        if role == 'farmer':
            farmer_profile = FarmerProfile(user=user)
            farmer_profile.save()
        elif role == 'owner':
            owner_profile = OwnerProfile(user=user)
            owner_profile.save()
        elif role == 'expert':
            expert_profile = ExpertProfile(user=user)
            expert_profile.save()
        else:
            admin_profile = AdminProfile(user=user)
            admin_profile.save()

        # send confirmation email
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'http://127.0.0.1:8000' + reverse('accounts:confirm-email', kwargs={'user_id': user_id, 'token': token})
        message = get_template('accounts/account_activation_email.html').render({
            'confirm_url': url
        })
        mail = EmailMessage('Fagrimacs Account Confirmation', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'accounts/registration_pending.html',{
            'message': f'A confirmation email has been sent to your email. Please confirm to finish registration.'
            })
    return render(request, 'accounts/signup.html', {
        'form': form,
    })



class ConfirmRegistrationView(TemplateView):
    """View for user to confirm registration."""
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))

        user = CustomUser.objects.get(pk=user_id)

        context = {
            'message': 'Registration confirmation error. Please click the reset password to generate a new confirmation email.'
        }

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            context['message'] = 'Registration complete. Please login'

        return render(request, 'accounts/registration_complete.html', context)


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
