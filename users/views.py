import secrets  # 5

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class RegisterUser(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):  # 2
        user = form.save()
        user.is_active = False  # 3
        token = secrets.token_hex(16)  # 6
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'  # 7
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Здравствуйте! Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )  # 8
        return super().form_valid(form)  # 9


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))  # 10


class PasswordResetView(FormView):
    template_name = "password_reset.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        user = User.objects.get(email=email)

        new_password = User.objects.make_random_password()

        user.set_password(new_password)
        user.save()

        send_mail(
            subject="Новый пароль",
            message=f"Ваш новый пароль: {new_password}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return super().form_valid(form)