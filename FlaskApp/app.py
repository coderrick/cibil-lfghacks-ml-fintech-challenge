import requests
from flask import Flask, render_template, request
from google.cloud import bigquery

# [END bigquery_simple_app_all]
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    print(password)
    # url = ''
    # city = ''

    # r = requests.get(url.format(city)).json()
    # print(r)
    url = "https://ussouthcentral.services.azureml.net/workspaces/22baaa55d81b43fbae6d10a81e886417/services/54a2204a96c14cfbb71e4f7243963ddc/execute"
    querystring = {"api-version":"2.0","format":"swagger"}

    payload = "{\r\n        \"Inputs\": {\r\n                \"input1\":\r\n                [\r\n                    {\r\n                            \"userid\": \"7\",   \r\n                            \"age\": \"35\",   \r\n                            \"gender\": \"F\",   \r\n                            \"item_class\": \"jewelry\",   \r\n                            \"freq\": \"0.5\",   \r\n                            \"price\": \"75\",   \r\n                            \"label\": \"none\"   \r\n                    }\r\n                ]\r\n        },\r\n    \"GlobalParameters\":  {\r\n    }\r\n}\r\n"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer nzSKK7RPVTuHNCivdG1XA9CuFh5vE/cGk+WNJODe+cwS8uDThkPeTVP1Nrpwq1FA9r5acetc2NVKysTpZCwqGg==",
        'cache-control': "no-cache",
        'Postman-Token': "1af1e5d8-30ce-4a80-9c91-fba989be1ebc"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)

    return render_template('index.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/consultation')
def consultation():
    return render_template('consultation.html')


def query_stackoverflow():
    client = bigquery.Client()
    query_job = client.query("""
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10""")

    results = query_job.result()  
    for row in results:
        print("{} : {} views".format(row.url, row.view_count))
    # [END bigquery_simple_app_print]

query_stackoverflow()

if __name__ == '__main__':
    app.run()