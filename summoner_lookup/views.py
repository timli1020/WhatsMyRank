from django.shortcuts import render, redirect
from django.http import HttpResponse
from riotwatcher import RiotWatcher
from .summoner_search import makeSearch
# Create your views here.


def home(request):
    return render(request, 'summoner_lookup/home.html')


def search(request):
    print(request.method)
    if request.method == "POST":
        print('*'*50)
        print(request.POST)
        print('*'*50)

        summoner_name = request.POST.get('summoner_name', None)
        my_region = 'na1'

        args = makeSearch(my_region, summoner_name)

        print('*'*50)
        print(args)
        print('*'*50)

        return render(request, 'summoner_lookup/search.html', args)

    else:
        return redirect('/')
