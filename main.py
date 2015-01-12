import argparse

from tweet import get_users, new_data, get_links


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    parser.add_argument("--url", help='Use url as twitter.com/{account}/lists/{list name}', type=str)

    return parser


def run():
    parser = get_parser()
    args = parser.parse_args()
    if args.file and args.url:
        parser.error('You must use only one option - url or file.')

    if args.url:
        users = get_users(args.url)
        new_data(users)

    elif args.file:
        lists = get_links(args.file)
        for list in lists:
            users = get_users(list)
            new_data(users)

if __name__ == '__main__':
    run()
