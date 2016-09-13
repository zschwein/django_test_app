__author__ = 'zschweinfurth'

from test_app.class_based_views.base.base_view import BaseView


class LoggedInView(BaseView):

    template_name = 'logged_in_view/logged_in_view_page.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        user = self.request.user

        context['username'] = user.username
        context['last_login'] = user.last_login.date()
        return context
