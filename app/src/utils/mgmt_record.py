from app.src.utils.get_attributes import get_record_alternate_id, get_vpn_alternate, get_record_location_id, \
    get_vpn_location
from app.src.utils.send_event import send_msg
import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

cdc_host = os.environ.get('CDC_HOST')
domain = os.environ.get('DOMAIN')


def update_record_alternate(vpn_name: str, requester: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        alternate_record_id = get_record_alternate_id(vpn_name, token)
        vpn_alternate = get_vpn_alternate(vpn_name, token)
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records/' + alternate_record_id

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
            'provider_name': os.environ.get('CONDUCTOR_PROVIDER_NAME'),
            'weight': os.environ.get('CONDUCTOR_RECORD_ON_TRAFFIC')
        }
        headers = {
            'x-tiger-token': 'Bearer ' + token
        }
        request_body = json.dumps(payload, indent=4)
        response = requests.request(
            'PUT',
            url,
            headers=headers,
            data=request_body
        )
        send_msg(fqdn, vpn_alternate)
        response_body = json.loads(response.text)
        return response_body


def update_record_location(vpn_name: str, requester: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        location_record_id = get_record_location_id(vpn_name, token)
        vpn_location = get_vpn_location(vpn_name, token)
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records/' + location_record_id

        payload = {
            'ttl': os.environ.get('CONDUCTOR_RECORD_TTL'),
            'record_type': os.environ.get('CONDUCTOR_RECORD_TYPE'),
            'description': os.environ.get('CONDUCTOR_DESCRIPTION'),
            'requester': requester,  # User set in url, e.g /api/action/{vpn_name}/{requester}
            'destination': {
                'value': vpn_location,
                'type': 'DEVICE'
            },
            'status': 'TO_UPDATE',
            'provider_name': os.environ.get('CONDUCTOR_PROVIDER_NAME'),
            'weight': os.environ.get('CONDUCTOR_RECORD_OFF_TRAFFIC')
        }
        headers = {
            'x-tiger-token': 'Bearer ' + token
        }
        request_body = json.dumps(payload, indent=4)
        response = requests.request(
            'PUT',
            url,
            headers=headers,
            data=request_body
        )
        response_body = json.loads(response.text)
        return response_body
