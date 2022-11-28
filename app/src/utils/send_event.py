import requests
import os


chat_ops_url = os.environ['CHATOPS_URL']


def send_msg(host: str, vpn_alternate: str):
    url = chat_ops_url

    payload = {
        "host": host,
        "vpnAlternate": vpn_alternate
    }

    headers = {}

    requests.request(
        'POST',
        url,
        headers=headers,
        data=payload
    )
