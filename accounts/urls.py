
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


urlpatterns = [
    # sign up
    path('new/', AuthenticationNewUser.as_view()),
    # login
    path('api-token-auth/', obtain_auth_token),
]