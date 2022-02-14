import json
import time

from utils.data import remove_content_files

def test_validate_request_accepted_too_many_request(test_app):
    client = test_app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'foundingType': "SME",
        'cashBalance': 435.30,
        'monthlyRevenue': 4235.45,
        'requestedCreditLine': 100,
        'requestedDate': '2021-07-19T16:32:59.860Z'
    }
    print(json.dumps(data))
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(2)
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(2)
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(2)
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('accepted')
    assert resp.status_code == 429
    assert 'code' in data
    assert data['code'] == 'TRI0010'
    assert data['message'] == 'TOO_MANY_REQUESTS'

def test_validate_request_reject_too_many_request(test_app):
    client = test_app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'foundingType': "SME",
        'cashBalance': 435.30,
        'monthlyRevenue': 4235.45,
        'requestedCreditLine': 5000,
        'requestedDate': '2021-07-19T16:32:59.860Z'
    }
    print(json.dumps(data))
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(3) 
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('rejected')
    assert resp.status_code == 429
    assert 'code' in data
    assert data['code'] == 'TRI0010'
    assert data['message'] == 'TOO_MANY_REQUESTS'


def test_validate_request_reject_sales_agent_will_contact(test_app):
    client = test_app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'foundingType': "SME",
        'cashBalance': 435.30,
        'monthlyRevenue': 4235.45,
        'requestedCreditLine': 5000,
        'requestedDate': '2021-07-19T16:32:59.860Z'
    }
    print(json.dumps(data))
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(1)
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(1) 
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(1) 
    client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)
    time.sleep(2)  
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('rejected')
    assert resp.status_code == 400
    assert 'code' in data
    assert data['code'] == 'TRI0020'
    assert data['message'] == 'SALES_AGENT_WILL_CONTACT'


    
