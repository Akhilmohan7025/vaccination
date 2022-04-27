from django.urls import path
from owner import views

urlpatterns = [
    path("adminhome",views.AdminHome.as_view(),name="adminhome"),
    path("vaccin/add",views.AddVaccin.as_view(),name="addvaccin"),
    path("vaccin/list",views.VaccinList.as_view(),name="listvaccin"),
    path("vaccin/details/<int:id>", views.VaccinDetail.as_view(), name="vaccindetail"),






]