import json
from utils.data import remove_content_files

def test_validate_request_sme_accepted(test_app):
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
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('accepted')    
    assert resp.status_code == 200
    assert 'code' in data
    assert data['code'] == 'TRI0002'

def test_validate_request_startup_accepted(test_app):
    client = test_app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'foundingType': "Startup",
        'cashBalance': 435.30,
        'monthlyRevenue': 4235.45,
        'requestedCreditLine': 100,
        'requestedDate': '2021-07-19T16:32:59.860Z'
    }
    print(json.dumps(data))
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('accepted')
    assert resp.status_code == 200
    assert 'code' in data
    assert data['code'] == 'TRI0002'

def test_validate_request_sme_rejected(test_app):
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
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('rejected')
    assert resp.status_code == 200
    assert 'code' in data
    assert data['code'] == 'TRI0003'

def test_validate_request_startup_rejected(test_app):
    client = test_app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'foundingType': "Startup",
        'cashBalance': 435.30,
        'monthlyRevenue': 4235.45,
        'requestedCreditLine': 5000,
        'requestedDate': '2021-07-19T16:32:59.860Z'
    }
    print(json.dumps(data))
    resp = client.post('/tribal/credit/check', data=json.dumps(data), headers=headers)    
    data = json.loads(resp.data.decode())
    print(data)
    remove_content_files('rejected')
    assert resp.status_code == 200
    assert 'code' in data
    assert data['code'] == 'TRI0003'
    
