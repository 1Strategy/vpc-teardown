#!/usr/bin/env python
import boto3

inuser = boto3.session.Session(profile_name='inContact-User')
client = inuser.client('ec2')
response = client.describe_regions()
r1 = response.get('Regions', {})
for x in r1:
    cl = inuser.client('ec2', region_name=x["RegionName"])
    response = cl.describe_vpcs()
    v = response.get('Vpcs', {})
    for z in v:
        p = map(z.pop, ['VpcId','CidrBlock','IsDefault'])
        if p[2]:
            print "I will be deleting", x["RegionName"], p
            #response_delete_vpc = cl.delete_vpc(DryRun=True,VpcId=p[0])
            #print response_delete_vpc
        else:
            print "I will NOT be deleting", x["RegionName"], p
