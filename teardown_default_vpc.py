#!/usr/bin/env python
import boto3
from teardown_default_subnets import teardown_default_subnets
from teardown_default_route_tables import teardown_default_route_tables

# inuser = boto3.session.Session(profile_name='inContact-User')


def lambda_handler(event, context):
    event['targeted_resouces'] = []
    event['protected_resources'] = []
    teardown_default_vpcs(event, context)


def list_default_vpcs(event, context):
    vpcs_to_teardown = []
    region = event['region']
    ec2_client = boto3.client('ec2', region_name=region)
    vpcs = ec2_client.describe_vpcs()['Vpcs']

    for vpc in vpcs:
        if vpc.get('IsDefault', False):
            print('To be deleted: {vpc}, the default VPC in {region}'.format(region=region, vpc=vpc['VpcId']))
            vpcs_to_teardown.append(vpc['VpcId'])
        else:
            print(
                'Not to be deleted: {vpc} in {region}'.format(region=region,
                                                              vpc=vpc['VpcId'])
            )

    return vpcs_to_teardown


def teardown_vpcs(vpcs_to_teardown):

    for vpc in vpcs_to_teardown:
        pass
    # ec2_client.delete_vpc(DryRun=True, VpcId='vpc-b80e29d1')


def teardown_default_vpcs(event, context):

    payload = event

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions()
    regions = response.get('Regions', {})

    for region in regions:
        payload['region'] = region['RegionName']
        default_vpcs = list_default_vpcs(payload, None)
        print(default_vpcs)
        # teardown_default_route_tables(payload, None)

        # teardown_vpcs(default_vpcs)


if __name__ == "__main__":
    teardown_default_vpcs({}, {})
