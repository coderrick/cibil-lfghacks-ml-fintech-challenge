import requests
from flask import Flask, render_template
from google.cloud import bigquery

# [END bigquery_simple_app_all]
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    # url = ''
    # city = ''

    # r = requests.get(url.format(city)).json()
    # print(r)
    return render_template('index.html')

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