from TwitterAPI import TwitterAPI
from settings import *
import re

api = TwitterAPI(
    consumer_key,
    consumer_secret,
    access_token_key,
    access_token_secret
)


def parse_url(url):
    regexp = re.search(r'(?P<acc>[a-zA-Z]*)/lists/(?P<list>.*)', url)
    account = regexp.group('acc')
    list_name = regexp.group('list')
    if account and list_name:
        return {'account': account, 'list': list_name}
    return None
