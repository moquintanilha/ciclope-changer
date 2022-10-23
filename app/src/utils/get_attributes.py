import json
from dotenv import load_dotenv
import requests
import os
from app.src.models.vpn_attributes import VPNAttributes

load_dotenv()

cdc_host = os.environ.get('CDC_HOST')
domain = os.environ.get('DOMAIN')


def get_all_records(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        URL = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

        payload = {}
        headers = {
            'X-auth-token': token
        }

        response = requests.request(
            'GET',
            URL,
            headers=headers,
            data=payload
        )

        response_body = json.loads(response.text)
        return response_body


def get_vpn_alternate(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        URL = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

        payload = {}
        headers = {
            'X-auth-token': token
        }

        response = requests.request(
            'GET',
            URL,
            headers=headers,
            data=payload
        )

        response_body = json.loads(response.text)
        for i in range(0, len(response_body)):
            external_data = {
                'ip': response_body[i]['destination']['device']['value'],
                'vpn_status': response_body[i]['health_status']['health_check_status']
            }

            vpn_alternate = VPNAttributes(**external_data)
            if vpn_alternate.vpn_status is False:
                return vpn_alternate.ip


def get_record_id(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ.get('FQDN_CONDUCTOR')
        URL = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

        payload = {}
        headers = {
            'X-auth-token': token
        }

        response = requests.request(
            'GET',
            URL,
            headers=headers,
            data=payload
        )

        response_body = json.loads(response.text)

        for i in range(0, len(response_body)):
            external_data = {
                'id': response_body[i]['subdomain']['id']
            }

            vpn_alternate = VPNAttributes(**external_data)

        return vpn_alternate.id
