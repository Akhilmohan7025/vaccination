from django.shortcuts import render
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView
from owner.models import Vaccin
from owner.forms import Vaccinform
from django.urls import reverse_lazy

# Create your views here.


class AdminHome(View):
    def get(self,request,*args,**kwargs):
        adhome=Vaccin.objects.all()
        context = {"adhome":adhome}
        return render(request, "adminhome.html", context)
class AddVaccin(CreateView):
    model = Vaccin
    form_class = Vaccinform
    template_name = "vaccin_add.html"
    success_url = reverse_lazy('listvaccin')
    pk_url_kwarg = 'id'


class VaccinList(ListView):
    model = Vaccin
    context_object_name = "item"
    template_name = "vacin_list.html"


class VaccinDetail(DetailView):
    model = Vaccin
    context_object_name = "vaccin"
    template_name = "vaccin_detail.html"
    pk_url_kwarg = 'id'

