import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

cdc_host = os.environ.get('CDC_HOST')
domain = os.environ.get('DOMAIN')


def record_healthcheck(record_id: str, token: str, fqdn: str):
    url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records/' + record_id + \
          '/healthcheck'

    payload = {}
    headers = {
        'x-tiger-token': 'Bearer ' + token
    }
    response = requests.request(
        'GET',
        url,
        headers=headers,
        data=payload
    )
    response_body = json.loads(response.text)
    print(response_body)
