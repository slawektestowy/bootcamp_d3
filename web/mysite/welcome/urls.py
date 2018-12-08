

from django.urls import path

from .views import hello_view, hello_name_view

urlpatterns = [
    path('', hello_view),
    path('<name>', hello_name_view)
]
