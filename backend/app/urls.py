from django.urls import path
from app import views

urlpatterns = [
    path("", views.formView, name="index"),
    # path("next/", views.next, name="next"),
    # path("form/", views.form, name="form"),
]
