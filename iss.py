#!/usr/bin/env python

__author__ = 'Timothy La (tla111)'

import requests


def main():

    r = requests.get("http://api.open-notify.org/astros.json")
    print(r.json())

    coords = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    return coords


if __name__ == '__main__':
    main()
