#1. Посмотреть документацию к API GitHub, разобраться как вывести список
# репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import json
import requests

url = 'http://api.github.com'
user = 'JonikSE'
response = requests.get(f'{url}/users/{user}/repos')
j_data = response.json()
for i in j_data:
    print(i['name'])

with open('repositories.json', 'w') as outfile:
    json.dump(j_data, outfile)