

from django.urls import path

from .views import add_numbers

urlpatterns = [
    path('<int:l1>/<int:l2>', add_numbers)
]
