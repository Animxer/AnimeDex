import requests


def update_views(anime):
    try:
        requests.get(
            'https://animxer-api-bids.vercel.app/db/view?anime='+anime.strip())
    except:
        pass
    return


def update_watch(anime):
    try:
        requests.get(
            'https://animxer-api-bids.vercel.app/db/watch?anime='+anime.strip())
    except:
        pass
    return
