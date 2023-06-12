from django.urls import path, include

from apps.accounts.views.login import CustomLoginView
from apps.accounts.views.signUp import CustomRegisterView

app_name = "accounts"


urlpatterns = [

    path(
        "signup",
        CustomRegisterView.as_view(),
        name="accounts_signup",
    ),
    path("login", CustomLoginView.as_view(), name="accounts_login"),

]
