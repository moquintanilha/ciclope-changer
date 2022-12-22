from app.src.utils.get_facts_zone import get_facts_record
from app.src.utils.send_event import send_msg
from app.src.config.logging_config import CustomFormatter
import logging
import os
import boto3

logger = logging.getLogger('Ciclope')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(CustomFormatter())
logger.addHandler(console_handler)

session = boto3.session.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
client = session.client('route53')


def switch_vpn(vpn_name: str, requester: str, comment: str):
    try:
        if vpn_name == 'conductor':
            scope = os.environ['SCOPE']
            fqdn = 'conductor-' + scope + '-in-cloudexchange.mercadolibre.io.'
            record_attributes = get_facts_record()
            for each_record in record_attributes:
                if each_record['weight'] == 0:
                    vpn_alternate = each_record['ip_address']
                    response_alternate = client.change_resource_record_sets(
                        HostedZoneId=os.environ['HOSTED_ZONE_ID'],
                        ChangeBatch={
                            'Comment': 'Requester: ' + requester + 'Message: ' + comment,
                            'Changes': [
                                {
                                    'Action': 'UPSERT',
                                    'ResourceRecordSet': {
                                        'Name': str(fqdn),
                                        'Type': str(os.environ['CONDUCTOR_RECORD_TYPE']),
                                        'SetIdentifier': each_record['identifier'],
                                        'TTL': int(os.environ['CONDUCTOR_RECORD_TTL']),
                                        'Weight': int(os.environ['CONDUCTOR_RECORD_ON_TRAFFIC']),
                                        'ResourceRecords': [
                                            {
                                                'Value': vpn_alternate
                                            },
                                        ]
                                    }
                                }
                            ]
                        }
                    )
                if each_record['weight'] == 255:
                    vpn_location = each_record['ip_address']
                    response_location = client.change_resource_record_sets(
                        HostedZoneId=os.environ['HOSTED_ZONE_ID'],
                        ChangeBatch={
                            'Comment': 'Requester: ' + requester + 'Message: ' + comment,
                            'Changes': [
                                {
                                    'Action': 'UPSERT',
                                    'ResourceRecordSet': {
                                        'Name': str(fqdn),
                                        'Type': str(os.environ['CONDUCTOR_RECORD_TYPE']),
                                        'SetIdentifier': each_record['identifier'],
                                        'TTL': int(os.environ['CONDUCTOR_RECORD_TTL']),
                                        'Weight': int(os.environ['CONDUCTOR_RECORD_OFF_TRAFFIC']),
                                        'ResourceRecords': [
                                            {
                                                'Value': vpn_location
                                            },
                                        ]
                                    }
                                }
                            ]
                        }
                    )
        if response_alternate['ResponseMetadata']['HTTPStatusCode'] == 200 and \
                response_location['ResponseMetadata']['HTTPStatusCode'] == 200:
            logger.info('Received a request to change traffic on the VPN ' + vpn_name)
            logger.info('requester: ' + requester)
            logger.info('comment: ' + comment)
            send_msg(fqdn, vpn_alternate)
    except Exception as e:
        raise e
