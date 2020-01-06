from riotwatcher import RiotWatcher, ApiError
from .apikey import apiKey
from django.shortcuts import redirect


def makeSearch(region, summonerName):

    watcher = RiotWatcher(apiKey())
    args = {}
    try:
        summoner = watcher.summoner.by_name(region, summonerName)

        id = summoner['id']
        stats = watcher.league.by_summoner(region, id)

        print('*'*50)
        print(summoner)
        print('*'*50)

        args = {'summoner_name': summoner['name'],
                'solo_queue_tier': None,
                'solo_queue_rank': None,
                'solo_queue_lp': None,
                'flex_queue_tier': None,
                'flex_queue_rank': None,
                'flex_queue_lp': None}

        for queue in stats:
            if queue['queueType'] == 'RANKED_FLEX_SR':
                args['flex_queue_tier'] = queue['tier']
                args['flex_queue_rank'] = queue['rank']
                args['flex_queue_lp'] = queue['leaguePoints']

            if queue['queueType'] == 'RANKED_SOLO_5x5':
                args['solo_queue_tier'] = queue['tier']
                args['solo_queue_rank'] = queue['rank']
                args['solo_queue_lp'] = queue['leaguePoints']

        return args

    except ApiError as err:
        if err.response.status_code == 404:
            args['summoner_name'] = 'No summoner with this name found'
            return args
