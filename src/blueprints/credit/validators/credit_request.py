from utils.validators import BaseRequest


class CreditRequest(BaseRequest):
    def rules(self):
        return {
             'foundingType': ['bail', 'required', 'filled','in:Startup,SME'],
             'cashBalance': ['bail', 'required', 'numeric'],
             'monthlyRevenue': ['bail', 'required', 'numeric'],
             'requestedCreditLine': ['bail', 'required', 'numeric'],
             'requestedDate': ['bail', 'required', 'filled', 'string', 'regex:^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$']
        }