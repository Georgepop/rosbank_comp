
# информация получается с сайта партнера, обрабатывается в рб и отдается на сайт партнер

import requests
import json


url='http://127.0.0.1:5000'

r = requests.get(url)
print(r, r.text)


'''
Апи вход-
Фио
Ид машины
Стоимость машины
Срок кредита
'''

x={'car_id':123,
   'fio':'GHU',
   'loan_sum':200,
   'loan_term': 24  
       }


def make_request(x):
    
    data = {'X':x}
    j_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url+'/result', data=j_data, headers=headers)
    q=r.json()['output']
    return [r, q] # статус запроса+результат

make_request(x)


'''
Апи выход-
Номер клиента
Номер рассчетного счета
Наличие располагаемой суммы

'''
