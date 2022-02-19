#2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# .Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.

import json
import requests

url = 'https://api.vk.com/method/groups.get'

with open('C:/Users/Лиза/Desktop/parsing/venv/user_id.txt') as u:
    user_id = u.read()

v = '5.131'

with open('C:/Users/Лиза/Desktop/parsing/venv/access_token.txt') as a:
    access_token =a.read()

params = {'user_id' : user_id, 'v' : v, 'access_token' : access_token}
response = requests.get(url, params = params)
j_data = response.json()
print(j_data)

with open('vk_groups.json', 'w') as f:
    json.dump(j_data, f)