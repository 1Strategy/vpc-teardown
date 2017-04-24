#!/usr/bin/env python
import boto3

inuser = boto3.session.Session(profile_name='inContact-User')
client = inuser.client('ec2')
response = client.describe_regions()
regions = response.get('Regions', {})

for region in regions:
    vpc_client = inuser.client('ec2', region_name=region["RegionName"])
    response = vpc_client.describe_vpcs()
    vpcs = response.get('Vpcs', {})
    for vpc in vpcs:
        vpc_id = map(vpc.pop, ['VpcId', 'CidrBlock', 'IsDefault'])
        if vpc_id[2]:
            print "I will be deleting", vpc["RegionName"], vpc_id
            #response_delete_vpc = cl.delete_vpc(DryRun=True,VpcId=p[0])
            #print response_delete_vpc
        else:
            print "I will NOT be deleting", vpc["RegionName"], vpc_id
