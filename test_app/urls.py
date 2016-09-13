from django.conf.urls import patterns, include, url

from django.contrib import admin
from test_app.class_based_views.create_user.create_user_view import CreateUserView
from test_app.class_based_views.login.login_view import LoginView
from django.contrib.auth.decorators import login_required
from budget.views.class_based_views.expenditure.expenditure_view import ExpenditureView
from test_app.class_based_views.logged_in_view.logged_in_view import LoggedInView
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^budget', include('budget.urls', namespace="bugd")),
    url(r'^user$', CreateUserView.as_view(), name="create_user"),
    url(r'^login(?P<logout>/logout)?$', LoginView.as_view(), name="login"),
    url(r'exp', login_required(ExpenditureView.as_view()), name='exp'),
    url(r'^$', login_required(LoggedInView.as_view()), name='logged_in'),
]
