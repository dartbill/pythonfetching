import requests
from .repo import Repo

URL = 'https://api.github.com/users/dartbill/repos'

def fetch_repos():
    '''call to Api'''
    req = requests.get(URL)
    for data in req.json():
        Repo(data)
    return data

