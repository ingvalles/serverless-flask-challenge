import json
from datetime import datetime

ACCEPTED_ROUTE = 'data/data-accepted.json'
REJECTED_ROUTE = 'data/data-rejected.json'

def write_json(new_data, status):
    file_name = ACCEPTED_ROUTE
    if status == 'rejected':
        file_name = REJECTED_ROUTE
    with open(file_name,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    file.close()    
    json_data = json.load(open(file_name))
    if status == 'accepted':
        return check_count_request_accepted(json_data)
    return check_count_request_rejected(json_data)
   
def exist_data_json(status):
    file_name = ACCEPTED_ROUTE
    if status == 'rejected':
        file_name = REJECTED_ROUTE
    json_data = json.load(open(file_name))
    total = len(json_data)
    return total

def check_count_request_accepted(json_data):   
    total = len(json_data)
    print(len(json_data))   
    if total >= 3:        
        date_start = datetime.strptime(json_data[total-1], '%Y-%m-%d %H:%M:%S')
        date_end = datetime.strptime(json_data[total-3], '%Y-%m-%d %H:%M:%S')       
        total_seconds = get_seconds_from_dates(date_start, date_end) 
        if total_seconds <= 120:
            return False    
    return True

def check_count_request_rejected(json_data):   
    total = len(json_data)
    print(len(json_data))   
    if total >= 2:
        date_start = datetime.strptime(json_data[total-1], '%Y-%m-%d %H:%M:%S')
        date_end = datetime.strptime(json_data[total-2], '%Y-%m-%d %H:%M:%S')       
        total_seconds = get_seconds_from_dates(date_start, date_end) 
        if total_seconds <= 30:
            return False    
    return True

def check_count_request_rejected_fail():
    file_name = REJECTED_ROUTE
    json_data = json.load(open(file_name))   
    total = len(json_data)
    print(len(json_data))   
    if total >= 5:     
        date_start = datetime.strptime(json_data[total-1], '%Y-%m-%d %H:%M:%S')
        date_end = datetime.strptime(json_data[total-5], '%Y-%m-%d %H:%M:%S')       
        total_seconds = get_seconds_from_dates(date_start, date_end)       
        if total_seconds <= 30:
            return False    
    return True


def get_seconds_from_dates(date_start, date_end):
    dif_time = date_start - date_end
    total_seconds= dif_time.total_seconds()
    return total_seconds 

def remove_content_files(type):
    print(type)
    file_name = ACCEPTED_ROUTE
    if type == 'rejected':
        file_name = REJECTED_ROUTE
    data = [ ]
    with open(file_name, 'w') as out_file:
        json.dump(data, out_file)    
    out_file.close() 
    return True     