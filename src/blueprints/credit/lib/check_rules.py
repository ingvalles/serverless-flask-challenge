from datetime import datetime

from utils.data import write_json,exist_data_json,check_count_request_rejected_fail

def check_line_credit(founding_type,cash_balance,monthly_revenue,requested_creditLine):            
    if(founding_type == "SME"):
        amount = monthly_revenue / 5
        print(amount)
        if(amount > requested_creditLine):
            return True
        return False                
    else:
        amount = cash_balance / 3
        credit_line = max([amount,monthly_revenue])  
        if(credit_line > requested_creditLine):
            return True
        return False

def save_line_credit(status):
    current_time = datetime.now()         
    json_data =  current_time.strftime('%Y-%m-%d %H:%M:%S')   
    print(json_data)
    return write_json(json_data,status)

def exist_line_credit(status):
    total = exist_data_json(status)    
    return total

def check_fail_rejected():
    total = check_count_request_rejected_fail()    
    return total
