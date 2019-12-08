from flask import Flask, jsonify, make_response, request, Response

import json

import pandas as pd
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "this's RosBank api"


@app.route('/result', methods=['POST'])
def score() -> Response:
    try:
        features = request.json['X']
        res=process(features)
        return make_response(jsonify({'output': res}))
    
    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')




'''
Апи обработка-
Проверка наличия человека как клиента
Проверка баланса счетов
Проверка текуших задолженностей
Проверка обеспечения кредита и кредитной истории
Сканирование человека выезд из страны
'''

def process(x):
    
    '''
    работа с апи росбанка
    rosbakapi=''
    r = requests.post(rosbakapi, data=x)
    q=r.json()['output']
    '''
    
    # тестовые данные для примера
    q={'max_money_amount':20000,
        'month_rate':0.02,
        'credit_history_ok':True,
        'is_client':True,
        'client_id':2134114,
            'office_inf':'м.Комсомольская'} ##
       
    
    feilds={'max_money_amount':float, 'month_rate':float, 'credit_history_ok':bool,'is_client':bool,'client_id':int,
            'office_inf':str}
    q={k:v for k,v in q.items() if k in feilds.keys()}
    q['funds_ok']=True if q['max_money_amount']>=x['loan_sum']*q['month_rate'] else False
    
    q={k:v for k,v in q.items() if k in feilds.keys()}
   
    res=''
    if q['is_client']==False:
        res='not_client' 
    elif q['credit_history_ok']==True:
        feilds={'office_inf':str, 'client_id':int, 'funds_ok':bool}
        res={k:v for k,v in q.items() if k in feilds.keys()}
        res['status_ok']=True
    else:
        res='bad_credit'
        
    return res
   

if __name__ == '__main__':
    app.run( port=5000, debug=True)

