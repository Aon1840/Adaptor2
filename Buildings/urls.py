from django.conf.urls import url
from Buildings import views

urlpatterns = [
    url('getAllBuilding', views.getAllBuilding),
    url('addNewBuilding', views.testAddBuilding),
]