from django.urls import path

from playground import views

# URL Config
urlpatterns = [
    path('hello/', views.say_hello)
]