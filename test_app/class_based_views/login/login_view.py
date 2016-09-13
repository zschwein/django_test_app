__author__ = 'zschweinfurth'

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from test_app.class_based_views.base.base_view import BaseView
from test_app.class_based_views.login.login_form import LoginForm


class LoginView(BaseView):
    form_class = LoginForm

    template_name = 'login/login_page.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()

        # capture and send next into context to resubmit with post
        # using login_required
        context['next'] = self.request.GET.get('next')

        return context

    def get(self, request, *args, **kwargs):
        # do custom things on the get method. in this case logout user from current request
        # , then return the parent's method to call get from the
        if kwargs.get('logout'):
            auth.logout(request)

        return super(LoginView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        if request.user is not None:
            auth.logout(request)

        form = self.form_class(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = auth.authenticate(username=form_data['username'], password=form_data['password'])

            # check the auth process
            if user is not None:
                # attache authed user to current session
                auth.login(request, user)
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('/')
            else:
                return TemplateResponse(request, self.template_name, self.get_context_data(**kwargs))