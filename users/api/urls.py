from django.urls import path
from users.api.viewsets import login_user, logout_user, register_user, period_data

app_name = "users"

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("period_data/", period_data, name="period_data"),
]
