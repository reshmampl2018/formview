from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=NameForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))

class CBV_modelform(FormView):
    template_name='CBV_modelform.html'
    form_class=studentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted ')