from django.shortcuts import render
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Divulgacoes
import requests
from django.contrib.auth.decorators import login_required
from .forms import CommunityActionForm, DonationForm, HealthServiceForm, EstablishmentForm 

@login_required
def formevent(request):
    if request.method == 'POST':
        divulgacao = Divulgacoes()
        divulgacao.nomeEvento = request.POST['nomeEvento']
        divulgacao.categoria = request.POST['categoria']
        divulgacao.cidade = request.POST['cidade']
        divulgacao.bairro = request.POST['bairro']
        divulgacao.endereco = request.POST['endereco']
        divulgacao.cep = request.POST['cep']
        divulgacao.telefone = request.POST['telefone']
        divulgacao.horarioInicio = request.POST['horarioInicio']
        divulgacao.horarioFim = request.POST['horarioFim']
        divulgacao.data = request.POST['data']
        divulgacao.user = request.user
        divulgacao.save()
        return render(request , 'index.html')
    return render(request , 'formevent.html')

def mapa(request, id):
    latitude = 0
    longitude = 0
    if request.method == "POST":
        chave = "AIzaSyDroa8JCUm2JfRZ_7eVMb4Fqx8ufr0Mz_A"
        div = Divulgacoes.objects.get(id=id)
        address = div.endereco+"+"+div.cidade
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+chave)
        if r.status_code == 200:
            dados = json.loads(r.content)
        return render(request, 'mapa.html')
    return render(request, 'mapa.html')



def servicolist(request):
    div = Divulgacoes.objects.all()
    return render(request, 'servicolist.html', {'div':div})


def create_establishment(request):
    title = "Cadastrar Estabelecimento"
    if request.method == "POST":
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = EstablishmentForm()
        return render(request, 'establishment.html', {'form': form,'title':title})


from .forms import CommunityActionForm, DonationForm, HealthServiceForm, EstablishmentForm 
    
def create_health_service(request):
    title = "Cadastrar Serviço de Saude"
    if request.method == "POST":
        form = HealthServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = HealthServiceForm()
        return render(request, 'establishment.html', {'form': form,'title':title})

def create_donation(request):
    title = "Cadastrar Doação"
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = DonationForm()
        return render(request, 'establishment.html', {'form': form,'title':title})
