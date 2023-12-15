# -*- coding: utf-8 -*-
"""
    coinify-tools

    clooney
    ~~~~~~~~~~~~

    Little script to clone all repos from a given BitBucket team/user.

    :author: Bruno Saboia de Albuquerque <bsa@coinify.com>
    :copyright: (c) 2017 Coinify ApS
"""

from git import Repo
from requests.auth import HTTPBasicAuth

import argparse
import json
import os
import requests
import sys

def get_repos(username, password, team):
    bitbucket_api_root = 'https://api.bitbucket.org/1.0/users/'
    raw_request = requests.get(bitbucket_api_root + team, auth=HTTPBasicAuth(username, password))
    dict_request = json.loads(raw_request.content.decode('utf-8'))
    repos = dict_request['repositories']

    return repos

def clone_all(repos):
    i = 1
    success_clone = 0
    for repo in repos:
        name = repo['name']
        clone_path = os.path.abspath(os.path.join(full_path, name))

        if os.path.exists(clone_path):
            print('Skipping repo {} of {} because path {} exists'.format(i, len(repos), clone_path))
        else:
            # Folder name should be the repo's name
            print('Cloning repo {} of {}. Repo name: {}'.format(i, len(repos), name))
            try:
                git_repo_loc = 'git@bitbucket.org:{}/{}.git'.format(team, name)
                Repo.clone_from(git_repo_loc, clone_path)
                print('Cloning complete for repo {}'.format(name))
                success_clone = success_clone + 1
            except Exception as e:
                print('Unable to clone repo {}. Reason: {} (exit code {})'.format(name, e.stderr, e.status))
        i = i + 1

    print('Successfully cloned {} out of {} repos'.format(success_clone, len(repos)))

parser = argparse.ArgumentParser(description='clooney - clone all repos from a given BitBucket team/user')

parser.add_argument('-f',
                    '--full-path',
                    dest='full_path',
                    required=False,
                    help='Full path of directory which will hold the cloned repos')

parser.add_argument('-u',
                    '--username',
                    dest="username",
                    required=True,
                    help='Bitbucket username')

parser.add_argument('-p',
                    '--password',
                    dest="password",
                    required=False,
                    help='Bitbucket password')

parser.add_argument('-t',
                    '--team',
                    dest="team",
                    required=False,
                    help='The target team/user')

parser.set_defaults(full_path='')
parser.set_defaults(password='')
parser.set_defaults(team='')

args = parser.parse_args()

username = args.username
password = args.password
full_path = args.full_path
team = args.team

if not team:
    team = username

if __name__ == '__main__':
    try:
        print('Fetching repos...')
        repos = get_repos(username, password, team)
        print('Done: {} repos fetched'.format(len(repos)))
    except Exception as e:
        print('FATAL: Could not get repos: ({}). Terminating script.'.format(e))
        sys.exit(1)

    clone_all(repos)