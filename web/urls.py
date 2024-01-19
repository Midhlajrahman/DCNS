from . import views
from django.urls import path

app_name="web"

urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name="about"),
    path("service/",views.service,name="service"),
    path("service_details/<slug:slug>", views.service_details, name="service_details"),
    path("updates/",views.updates,name="updates"),
    path("update_details/<slug:slug>",views.update_details,name="update_details"),
    path("contact/",views.contact,name="contact")
]
