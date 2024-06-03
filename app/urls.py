from . import views
from django.urls import path,include

urlpatterns = [
    path("", views.app_form, name="App_insert"),
    path("edit/<int:id>", views.app_form, name="App_edit"),
    path("delete/<int:id>/", views.app_delete, name="App_delete"),
    path("list/", views.app_list, name="App_list")
]
