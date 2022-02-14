# Serverless-Flask

The fastest way to a Flask application with [Serverless](https://github.com/serverless/serverless).

## Usage

```
$ npm install -g serverless
$ serverless install --url https://github.com/ingvalles/serverless-flask-challenge --name my-flask-app
$ cd my-flask-app && npm install
$ serverless deploy
```

Once the deploy is complete, run `sls info` to get the endpoint:

```
$ sls info
Service Information
<snip>
endpoints:
  ANY - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev <-- Endpoint
  ANY - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
```

Copy paste into your browser, and _voila_!

## Local development

To develop locally, create a virtual environment and install your dependencies:

```
python -m virtualenv venv (only is you no have virtual enviroment)
virtualenv venv
venv/Scripts/activate
pip install -r requirements.txt
```

Run testcase:

```
serverless offline --stage local
python -m pytest src/tests --cov='src/blueprints' -p no:warnings  (Other terminal)
```

Then, run your app:

```
serverless wsgi serve --stage local
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

Navigate to [localhost:5000](http://localhost:5000) to see your app running locally.

## Configuration
example call endppoint:

curl --location --request POST 'http://localhost:5000/tribal/credit/check' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "foundingType": "SME",
    "cashBalance": 435.30,
    "monthlyRevenue": 4235.45,
    "requestedCreditLine": 5000,
    "requestedDate": "2021-07-19T16:32:59.860Z"
}'

## Code http
```
http   code      message
200    TRI0002   AUTHORIZED
200    TRI0003   REJECTED
400    TRI0020   SALES_AGENT_WILL_CONTACT
422    TRI0001   INVALID_REQUEST
429    TRI0010   TOO_MANY_REQUESTS          
```
