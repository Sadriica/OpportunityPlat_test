from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render

#def home(request):
#    return HttpResponse("Bienvenid@")

def home(request):
    home_conf = open("OpportunityPlat/Home.html")
    template_conf = Template(home_conf.read())
    home_conf.close()
    contexto = Context()
    documento = template_conf.render(contexto)
    return HttpResponse(documento)

#def home(request):
#    return render(request,'OpportunityPlat/templates/Home.html')