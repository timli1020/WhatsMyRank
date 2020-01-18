from riotwatcher import RiotWatcher, ApiError
from .apikey import apiKey
from django.shortcuts import redirect


def makeSearch(region, summonerName):

    watcher = RiotWatcher(apiKey())
    args = {}
    try:
        summoner = watcher.summoner.by_name(region, summonerName)

        id = summoner['id']
        account_id = summoner['accountId']
        stats = watcher.league.by_summoner(region, id)

        match_list_id = []
        matches = watcher.match.matchlist_by_account('na1', account_id)

        match_list = matches['matches']

        matches = []

        for match in match_list:
            match_list_id.append(match['gameId'])

        match = watcher.match.by_id('na1', match_list_id[0])

        print('*'*50)
        print(match)
        print('*'*50)

        args = {'summoner_name': summoner['name'],
                'profile_icon': summoner['profileIconId'],
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
