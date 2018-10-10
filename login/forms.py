from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email уже используется")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return password2

    def save(self, commit=True):
        User = get_user_model()
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def authenticate(self, email=None, password=None):
        User = get_user_model()
        try:
            user = User.get(email=email)
            if User.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['first_name', 'patronymic', 'last_name', 'avatar']

