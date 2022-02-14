from flask import Blueprint, current_app
from flask_sieve import validate
from flask_restful import Api, Resource

# from .validators import CreditRequest
from .check import Check

credit = Blueprint(
    "credit",
    __name__,
    url_prefix='/' + current_app.config['SERVICE_ROUTE']
)
api = Api(credit)


# class Credit(Resource):
#     @validate(CreditRequest)
#     def post(self):
#         return {"message": "receive request"}


api.add_resource(Check, "/credit/check")
