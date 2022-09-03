from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("shorten/<str:hash>/", views.shorten, name="shorten"),
    path("<str:url_hash>/", views.redirect_hash, name="redirect"),
]
