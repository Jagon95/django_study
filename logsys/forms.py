from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from .models import User, Profile


# class RegistrationForm(UserCreationForm):
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            # 'username',
            # 'password1',
            # 'password2',
            # Field('firstname', style="color: #333;", css_class="whatever", id="firstname"),
            # # 'secondname',
            # # 'patronymic',
            Fieldset(
                'Sign up',
                'username',
                'password1',
                'password2',
                # 'patronymic',
            ),
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('patronymic', 'additionalInfo')
