from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import SignUpForm, UserProfileForm
from accounts.tokens import account_activation_token
from accounts.models import UserProfile

User = get_user_model()

if not settings.DEBUG:
    BASE_URL = 'https://fagrimacs.com'
else:
    BASE_URL = 'http://127.0.0.1:8000'


class UserLoginView(LoginView):
    """View for user to login in platform """
    template_name = 'accounts/login.html'

    def get_success_url(self):
        """Url which user redirected when log in."""
        url = self.get_redirect_url()
        if url:
            return url
        elif not self.request.user.is_superuser:
            # Non superuser should be redirected to their profiles
            return '/'
        else:
            return '/admin/'


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user_email = form.cleaned_data['email']
        user.save()

        # send confirmation email
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = BASE_URL + reverse('accounts:confirm-email',
                                 kwargs={'user_id': user_id, 'token': token})
        message = get_template(
            'accounts/account_activation_email.html').render(
                {'confirm_url': url})
        mail = EmailMessage(
            'Fagrimacs Account Confirmation',
            message,
            to=[user_email],
            from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'accounts/registration_pending.html',
                      {'message': (
                          'A confirmation email has been sent to your email'
                          '. Please confirm to finish registration.')}
                      )
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


class ConfirmRegistrationView(TemplateView):
    """View for user to confirm registration."""
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))

        user = User.objects.get(pk=user_id)

        context = {
            'message': 'Registration confirmation error. Please click the reset password to generate a new confirmation email.'
        }

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            UserProfile.objects.create(user=user)
            user.save()
            context['message'] = 'Registration complete. Please login'

        return render(request, 'accounts/registration_complete.html', context)


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    model = UserProfile


class UserProfileUpdateView(LoginRequiredMixin,
                            SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('accounts:user-profile')
    success_message = 'Profile update successful.'
