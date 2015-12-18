from pleercom import PleerApi


def search(query):
    app_id, app_key = '761618', 'YcOMM2E9eEz3CEJFke5y'

    pleer = PleerApi(app_id, app_key)

    params = {'query': query}
    return pleer.tracks_search(params=params)
    
