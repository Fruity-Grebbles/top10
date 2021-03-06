from pleercom import PleerApi


def search(query):
    app_id, app_key = '761618', 'YcOMM2E9eEz3CEJFke5y'

    pleer = PleerApi(app_id, app_key)

    params = {'query': query}
    links = []
    try:
        for track in pleer.tracks_search(params=params)['tracks'].itervalues():
            links.append(pleer.tracks_get_download_link(track['id'])['url'])
        return links
    except Exception:
        for track in pleer.tracks_search(params=params)['tracks']:
            links.append(pleer.tracks_get_download_link(track['id'])['url'])
        return links
