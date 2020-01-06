from riotwatcher import RiotWatcher
from .apikey import apiKey


def makeSearch(region, summonerName):

    watcher = RiotWatcher(apiKey())
    summoner = watcher.summoner.by_name(region, summonerName)

    id = summoner['id']
    stats = watcher.league.by_summoner(region, id)

    print('*'*50)
    print(stats)
    print('*'*50)

    args = {'summoner_name': stats[0]['summonerName'],
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
