from django.conf.urls import url

import views

urlpatterns = [
    url(r'^auth/sign-in/', views.api_sign_in, name='api_sign_in'),
    url(r'^device/add/', views.api_device_add, name='api_device_add'),
    url(r'^device/measure/update/', views.api_device_measure_update, name='api_device_measure_update'),
]
