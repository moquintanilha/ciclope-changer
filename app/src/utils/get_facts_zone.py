import boto3
import os
from app.src.models.record_attributes import Record

session = boto3.session.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                                aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
client = session.client('route53')


def get_facts_record():
    try:
        response = client.list_resource_record_sets(
            HostedZoneId=os.environ['HOSTED_ZONE_ID'],
            MaxItems='900'
        )
        records = []
        for i in response['ResourceRecordSets']:
            scope = os.environ['SCOPE']
            if 'conductor-' + scope + '-in-cloudexchange.mercadolibre.io.' in i['Name']:
                obj = Record(i['Name'], i['SetIdentifier'], i['Weight'], i['ResourceRecords'][0]['Value'])
                records.append({
                    'name': obj.name,
                    'identifier': obj.identifier,
                    'weight': obj.weight,
                    'ip_address': obj.ip_address
                })
        return records
    except Exception as e:
        raise e
