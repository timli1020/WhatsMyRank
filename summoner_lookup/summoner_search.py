from riotwatcher import RiotWatcher
apiKey = 'RGAPI-d507af1d-8a94-4cc7-a371-5ae2a971fde8'


def makeSearch(region, summonerName):

    watcher = RiotWatcher(apiKey)
    summoner = watcher.summoner.by_name(region, summonerName)

    id = summoner['id']
    stats = watcher.league.by_summoner(region, id)

    args = {'summoner_name': stats[0]['summonerName'],
            'solo_queue_tier': stats[1]['tier'],
            'solo_queue_rank': stats[1]['rank'],
            'solo_queue_lp': stats[1]['leaguePoints']}

    return args
