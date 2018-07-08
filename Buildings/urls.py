from django.conf.urls import url
from Buildings import views

urlpatterns = [
    url('getAllBuilding', views.getAllBuilding),
    url('addNewBuilding', views.testAddBuilding),
    url('editNameBuilding/(?P<building_id>[0-9]+)/$', views.testEditBuilding),
]