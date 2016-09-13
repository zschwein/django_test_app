__author__ = 'zschweinfurth'
from django.views.generic import TemplateView
from test_app.class_based_views.create_user.create_user_form import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.models import User

class CreateUserView(TemplateView):
    form_class = CreateUserForm

    template_name = 'create_user/create_user_page.html'

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()

        return context

    def post(self, request, *args, **kwargs):
        # create a bound form. basically a form with data
        form = self.form_class(request.POST)
        # run is_valid form method, checking if all necessary data was collected from form
        # i have ignore error handeling for now
        if form.is_valid():
            clean = form.cleaned_data
            # create the user
            user = User.objects.create_user(username=clean['username'], password=clean['password'])
            return HttpResponse(user.username)
        else:
            return HttpResponse('Nope. Your info is no good!!.')

        #return self

