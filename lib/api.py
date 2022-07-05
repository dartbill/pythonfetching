import requests
from .repo import Repo

URL = ''

def fetch_repos(username):
    '''call to Api'''
    req = requests.get(f'https://api.github.com/users/{username}/repos')
    for data in req.json():
        Repo(data)
    return data

