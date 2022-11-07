from app.src.utils.get_attributes import get_record_id, get_vpn_alternate
from app.src.utils.send_event import send_msg
import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

cdc_host = os.environ.get('CDC_HOST')
domain = os.environ.get('DOMAIN')


def update_record(vpn_name: str, requester: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        record_id = get_record_id(vpn_name, token)
        vpn_alternate = get_vpn_alternate(vpn_name, token)
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records/' + record_id

        payload = {
            'ttl': os.environ.get('CONDUCTOR_RECORD_TTL'),
            'record_type': os.environ.get('CONDUCTOR_RECORD_TYPE'),
            'description': os.environ.get('CONDUCTOR_DESCRIPTION'),
            'requester': requester,  # User set in url, e.g /api/action/{vpn_name}/{requester}
            'destination': {
                'value': vpn_alternate,
                'type': 'DEVICE'
            },
            'status': 'TO_UPDATE',
            'provider_name': os.environ.get('CONDUCTOR_PROVIDER_NAME')
        }
        headers = {
            'X-auth-token': token
        }

        response = requests.request(
            'PUT',
            url,
            headers=headers,
            data=payload
        )
        send_msg(vpn_name, vpn_alternate)
        response_body = json.loads(response.text)
        return response_body
