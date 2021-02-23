import requests


def get_data(username):
    repository_list = []
    url = 'https://api.github.com/users/' + str(username) + '/repos'
    data = requests.get(url=url)
    if data.status_code == 200:
        resitory = data.json()
        for i in resitory:
            repository_list.append(i['name'])
        return repository_list

    else:
        return "ERROR"
