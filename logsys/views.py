from __future__ import absolute_import
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm
from .forms import RegistrationForm
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
