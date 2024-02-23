from django.urls import path
from . views import CustomLogin, CustomRegister, StartupDetail, StartupCreate, StartupUpdate, StartupDelete, HomePage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', HomePage, name="home"),
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', CustomRegister.as_view(), name="register"),

    path('startup/<int:pk>/', StartupDetail.as_view(), name="startup"),
    path('startup-create/', StartupCreate.as_view(), name="startup-create"),
    path('startup-update/<int:pk>/', StartupUpdate.as_view(), name="startup-update"),
    path('startup-delete/<int:pk>/', StartupDelete.as_view(), name="startup-delete"),
]