# -*- coding: utf-8 -*-
from TwitterAPI import TwitterAPI
from settings import *
import re


api = TwitterAPI(
    consumer_key,
    consumer_secret,
    access_token_key,
    access_token_secret
)


def get_links(path):
    with open(path, "r") as input_file:
        return input_file.readlines()


def parse_url(url):
    regexp = re.search(r'(?P<acc>[a-zA-Z]*)/lists/(?P<list>.*)', url)
    name = regexp.group('acc')
    list_name = regexp.group('list')
    if name and list_name:
        return {'name': name, 'slug': list_name}
    return None


def get_users(url):
    def get_list_members(account, slug):
        response = api.request('lists/members', {'owner_screen_name': account, 'slug': slug})
        if response.status_code == 200:
            for item in response:
                return item['users']
        else:
            print("Can't make call!")

    parsed = parse_url(url)
    if parsed:
        users = get_list_members(parsed['name'], parsed['slug'])
        return users
    return []


def new_data(users, url):
    with open('template', "r") as input_file:
        template = unicode(input_file.read())

    with open('sheet.csv', "a+") as output_file:
        for user in users:
            try:
                expanded_url = user['entities']['url']['urls'][0]['expanded_url']
            except KeyError:
                expanded_url = None

            data = template.format(
                name=user['name'],
                expanded_url=expanded_url,
                screen_name=user['screen_name'],
                description=user['description'],
                protected=user['protected'],
                followers_count=user['followers_count'],
                friends_count=user['friends_count'],
                listed_count=user['listed_count'],
                verified=user['verified'],
                statuses_count=user['statuses_count'],
                lang=user['lang'],
                location=user['location'],
                profile_image_url=user['profile_image_url'],
                id=user['id'],
                url=url
            )
            output_file.write(data.encode('UTF-8') + '\n')