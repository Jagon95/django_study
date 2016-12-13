from __future__ import absolute_import
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm, RegistrationForm
from .forms import UserForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


class HomePageView(generic.TemplateView):
    template_name = 'logsys/home.html'


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'logsys/signup.html'


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('logsys:user')
    template_name = 'logsys/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
            # raise Http404
            # return render_to_response('logsys/index', {username: username})
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('logsys:home')

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super(LogOutView, self).get(self.request, *args, **kwargs)


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('logsys:home')
        # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user) # instance тут для автозаполнения форм текущими значениями
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'logsys/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
