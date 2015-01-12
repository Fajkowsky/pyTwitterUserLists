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
    name = regexp.group('acc')
    list_name = regexp.group('list')
    if name and list_name:
        return {'name': name, 'slug': list_name}
    return None


def get_list_members(account, slug):
    response = api.request('lists/members', {'owner_screen_name': account, 'slug': slug})
    if response.status_code == 200:
        for item in response:
            return item['users']
    else:
        print("Can't make call!")


def get_users(url):
    parsed = parse_url(url)
    if parsed:
        users = get_list_members(parsed['name'], parsed['slug'])
