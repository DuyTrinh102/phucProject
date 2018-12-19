from django.conf.urls import url

import views

urlpatterns = [
    url(r'^auth/sign-in/', views.api_sign_in, name='api_sign_in'),
]
