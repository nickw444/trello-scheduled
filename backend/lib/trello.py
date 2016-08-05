from urllib.parse import urljoin, urlencode
import requests

class TrelloAPIException(Exception):
    pass

class TrelloClient():
    def __init__(self, api_key, api_base='https://trello.com/'):
        self.api_key = api_key
        self.api_base = api_base

    def _build_url(self, url, params=None, key=True, **kwargs):
        if params is None:
            params = {}

        if key:
            params['key'] = self.api_key

        params.update(kwargs)

        return urljoin(self.api_base, url) + '?{}'.format(urlencode(params))

    def fetch_token(self, token, access_token):
        ep = '/1/tokens/{}'.format(token)
        rv = requests.get(self._build_url(ep, token=access_token))
        if rv.status_code != 200:
            return TrelloAPIException()

        return rv.json()

    def fetch_member(self, member, access_token, **kwargs):
        ep = '/1/members/{}'.format(member)
        rv = requests.get(self._build_url(ep, token=access_token, **kwargs))
        if rv.status_code != 200:
            return TrelloAPIException()

        return rv.json()
        