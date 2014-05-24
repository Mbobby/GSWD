from __future__ import absolute_import 

#django imports
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

#local imports
from .forms import RegistrationForm, LoginForm

#class to handle home page view
class HomePageView(generic.TemplateView):
	template_name = "home.html"

#class to handle sign up
class SignUpView(generic.CreateView):
	form_class = RegistrationForm
	model = User
	template_name = 'accounts/signup.html'

#class to handle login
class LoginView(generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'
	
	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username = username , password = password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form) 