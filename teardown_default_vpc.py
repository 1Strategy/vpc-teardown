#!/usr/bin/env python
import boto3

# inuser = boto3.session.Session(profile_name='inContact-User')


def lambda_handler(event, context):

    vpcs_to_teardown = []

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions()
    regions = response.get('Regions', {})

    for region in regions:
        ec2_client = boto3.client('ec2', region_name=region["RegionName"])
        vpcs = ec2_client.describe_vpcs()['Vpcs']

        for vpc in vpcs:
            if vpc.get('IsDefault', False):
                print("Deleting {vpc}, the default VPC in {region}".format(region=region["RegionName"], vpc=vpc['VpcId']))
                vpcs_to_teardown.append(vpc['VpcId'])
            else:
                print "I will NOT be deleting", region["RegionName"], vpc['VpcId']
    print(vpcs_to_teardown)


def teardown_vpcs(vpcs_to_teardown):
    pass
    # response_delete_vpc = cl.delete_vpc(DryRun=True,VpcId=p[0])
    # print response_delete_vpc


if __name__ == "__main__":
    lambda_handler({}, {})
