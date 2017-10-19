#!/usr/bin/env python3

import argparse
import itertools
import json
import xml.etree.ElementTree

import requests


APPCAST_URL = 'https://download.docker.com/mac/{channel}/appcast.xml'
DOWNLOAD_URL = 'https://download.docker.com/mac/{channel}/{build}/Docker.dmg'


def get_latest_build_number(channel):
    """
    Parse the appcast XML to find the Build number of the latest release.
    """
    url = APPCAST_URL.format(channel=channel)
    resp = requests.get(url)

    ns = {'sparkle': '{http://www.andymatuschak.org/xml-namespaces/sparkle}'}
    root = xml.etree.ElementTree.fromstring(resp.text)

    for enclosure in root.findall('.//enclosure', ns):
        version_attrib = '{ns}version'.format(ns=ns['sparkle'])
        version = enclosure.attrib[version_attrib]
        return int(version)
    return None


def scan(channel, latest_build, limit=None):
    build_limit = latest_build - limit if limit else 0

    builds = []
    for build in range(latest_build, build_limit, -1):
        try:
            resp = requests.head(DOWNLOAD_URL.format(
                channel=channel,
                build=build
            ))
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            continue

        headers = resp.headers
        headers['url'] = resp.url
        builds.append(dict(headers))

    return builds


def main():
    parser = argparse.ArgumentParser(
        description='Scrape for Docker for Mac release download links'
    )
    parser.add_argument('channel', choices=['stable', 'edge'])
    parser.add_argument('--limit', type=int,
                        help='Maximum number of builds to scan for')
    parser.add_argument('--out', type=str,
                        help='JSON file to output build info')
    args = parser.parse_args()

    if args.out is None:
        args.out = args.channel + '.json'

    latest_build = get_latest_build_number(args.channel)
    builds = scan(args.channel, latest_build, limit=args.limit)

    with open(args.out, 'w') as f:
        json.dump(builds, f)
    print('Wrote {}.'.format(args.out))


if __name__ == '__main__':
    main()

