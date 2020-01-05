from django.shortcuts import render, redirect
from django.http import HttpResponse
from riotwatcher import RiotWatcher
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
        apiKey = 'RGAPI-d507af1d-8a94-4cc7-a371-5ae2a971fde8'
        watcher = RiotWatcher(apiKey)
        my_region = 'na1'
        me = watcher.summoner.by_name(my_region, summoner_name)
        id = me['id']
        rank = watcher.league.by_summoner(my_region, id)
        args = {'rank': rank[0]['tier']}
        return render(request, 'summoner_lookup/search.html', args)

    else:
        return redirect('/')
