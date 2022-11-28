import json
import requests
import os
from app.src.models.vpn_attributes import VPNAttributes


cdc_host = os.environ['CDC_HOST']
domain = os.environ['DOMAIN']


def get_vpn_alternate(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ['FQDN_CONDUCTOR']
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

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
        for i in range(0, len(response_body)):
            external_data = {
                'ip': response_body[i]['destination']['device']['value'],
                'vpn_status': response_body[i]['health_status']['health_check_status']
            }

            vpn_alternate = VPNAttributes(**external_data)
            if vpn_alternate.vpn_status is False:
                return vpn_alternate.ip


def get_record_alternate_id(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ['FQDN_CONDUCTOR']
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

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

        for i in range(0, len(response_body)):
            external_data = {
                'id': response_body[i]['id'],
                'vpn_status': response_body[i]['health_status']['health_check_status']
            }

            vpn_alternate = VPNAttributes(**external_data)
            if vpn_alternate.vpn_status is False:
                return vpn_alternate.id


def get_vpn_location(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ['FQDN_CONDUCTOR']
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

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
        for i in range(0, len(response_body)):
            external_data = {
                'ip': response_body[i]['destination']['device']['value'],
                'vpn_status': response_body[i]['health_status']['health_check_status']
            }

            vpn_location = VPNAttributes(**external_data)
            if vpn_location.vpn_status is True:
                return vpn_location.ip


def get_record_location_id(vpn_name: str, token: str):
    if vpn_name == 'conductor':
        fqdn = os.environ['FQDN_CONDUCTOR']
        url = 'https://' + cdc_host + '/domains/' + domain + '/subdomains/' + fqdn + '/records'

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

        for i in range(0, len(response_body)):
            external_data = {
                'id': response_body[i]['id'],
                'vpn_status': response_body[i]['health_status']['health_check_status']
            }

            vpn_location_id = VPNAttributes(**external_data)
            if vpn_location_id.vpn_status is True:
                return vpn_location_id.id
