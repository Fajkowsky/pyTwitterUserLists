import argparse
from tweet import parse_url

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    parser.add_argument("--url", type=str)

    return parser


def run():
    parser = get_parser()
    args = parser.parse_args()
    if args.file and args.url:
        parser.error('You must use only one option - url or file.')

    if args.url:
        parse_url(args.url)


if __name__ == '__main__':
    run()
