from django.shortcuts import render
import requests

def ok(request):
    return render(request, 'ok.html')

def home(request):
    response = requests.get('https://rickandmortyapi.com/api/character').json()
    return render(request, 'home.html', {'response': response})