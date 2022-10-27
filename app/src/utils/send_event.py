import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

chat_ops_url = os.environ.get('CHAT_OPS_URL')


def send_msg(host: str, vpn_alternate: str):
    url = chat_ops_url

    payload = {
        "host": host,
        "vpnAlternate": vpn_alternate
    }

    headers = {}

    response = requests.request(
        'POST',
        url,
        headers=headers,
        data=payload
    )

    response_body = json.loads(response.text)
    return response_body
