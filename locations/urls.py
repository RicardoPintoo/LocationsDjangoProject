from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='all-loactions'), # url.com/locations/
    path('<slug:location_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:location_slug>', views.details, name='details'), #domain.com/locations/<dynamic-path-segment>
]
