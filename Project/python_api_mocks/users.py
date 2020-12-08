import requests

user_url = 'http://jsonplaceholder.typicode.com/users'



def get_users():
    '''get list of users'''
    response = requests.get(user_url)

    if response.ok:
        return response
    else:
        return None    