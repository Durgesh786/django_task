from django.urls import path
from django.views.generic import RedirectView

from web.user.views import login, dashboard, logout, register, otp, add_emails, list_emails
urlpatterns = [

    path('login/', login, name="admin_login"),
    path('register/', register, name="register"),
    path('otp_verification/', otp, name="otp"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name="logout"),
    path('add_email/', add_emails, name="add_email"),
    path('list_email/', list_emails, name="list_email"),

    path('', RedirectView.as_view(url='login/', permanent=False)),
]
