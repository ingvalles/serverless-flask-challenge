from http.client import ACCEPTED
from flask import request
from flask_sieve import validate
from flask_restful import Resource
from datetime import datetime
from ..lib.check_rules import check_line_credit,exist_line_credit,save_line_credit,check_fail_rejected

from ..validators import CreditRequest

from utils.json import render_json

ACCEPTED_CREDIT = 'accepted'
REJECTED_CREDIT = 'rejected'

class Check(Resource):
    @validate(CreditRequest)
    def post(self):
        founding_type = request.json.get('foundingType')
        cash_balance = request.json.get('cashBalance')
        monthly_revenue = request.json.get('monthlyRevenue')
        requested_creditLine = request.json.get('requestedCreditLine')
        count_data_exist_accepted = exist_line_credit(ACCEPTED_CREDIT)        
        check_line = True  
        if (count_data_exist_accepted == 0):                        
            check_line =  check_line_credit(founding_type, cash_balance, monthly_revenue, requested_creditLine)                                     
        if(check_line):
             if(save_line_credit(ACCEPTED_CREDIT) == False):
                 return render_json(429, {'code': 'TRI0010', 'message': 'TOO_MANY_REQUESTS'})
             return render_json(200, {'code': 'TRI0002', 'message': 'AUTHORIZED'})
        if(save_line_credit(REJECTED_CREDIT) == False):            
            if(not check_fail_rejected()):
                return render_json(400, {'code': 'TRI0020', 'message': 'SALES_AGENT_WILL_CONTACT'}) 
            return render_json(429, {'code': 'TRI0010', 'message': 'TOO_MANY_REQUESTS'})               
        return render_json(200, {'code': 'TRI0003', 'message': 'REJECTED'})
    
  


       
        