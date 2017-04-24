#!/usr/bin/env python
import boto3
import json

inuser = boto3.session.Session(profile_name='ic-compliance')
cl = inuser.client('ec2', region_name='us-east-1')
vpc_response = cl.describe_vpcs()
v = vpc_response.get('Vpcs', {})
print v[0]['VpcId'], v[0]['IsDefault']
#response_delete_vpc = cl.delete_vpc(DryRun=True,VpcId=v[0]['VpcId'])
#response_delete_vpc = cl.delete_vpc(VpcId=v[0]['VpcId'])
#print response_delete_vpc
subnet_response = cl.describe_subnets()
subnets = subnet_response.get('Subnets', {})
#print subnets[0]['VpcId']
for x in subnets:
    #print x['VpcId'], x['DefaultForAz'], x['SubnetId']
    #print x['SubnetId']
    if x['DefaultForAz']:
        print "I will be deleting this Subnet", x['SubnetId']
        #delete_subnet_response = cl.delete_subnet(DryRun=True,SubnetId=x['SubnetId'])
        #print delete_subnet_response
    else:
        print "I will NOT be deleting", x['SubnetId']

igw_response = cl.describe_internet_gateways()
igws = igw_response.get('InternetGateways', {})
for x in igws:
    #print x['InternetGatewayId'], x['Attachments'][0]['VpcId']
    #if x['InternetGatewayId']:
    if x['Attachments'][0]['VpcId'] == v[0]['VpcId'] and v[0]['IsDefault'] == True:
        print "I will be detaching and deleting this InternetGateway", x['InternetGatewayId']
        #detach_igw_response = cl.detach_internet_gateway(DryRun=True,InternetGatewayId=x['InternetGatewayId'],VpcId=v[0]['VpcId'])
        #print detach_igw_response
        #delete_igw_response = cl.delete_internet_gateway(DryRun=True,InternetGatewayId=x['InternetGatewayId'])
        #print delete_igw_response
    else:
        print "I will NOT be deleting", x['InternetGatewayId']

nacl_response = cl.describe_network_acls()
nacls = nacl_response.get('NetworkAcls', {})
#print nacls
for x in nacls:
    #print x['NetworkAclId']
    if x['IsDefault']:
        print "I will be deleting this NACL", x['NetworkAclId']
        #delete_nacl_response = cl.delete_network_acl(DryRun=True,NetworkAclId=x['SubnetId'])
        #print delete_nacl_response
    else:
        print "I will NOT be deleting", x['NetworkAclId']

rtb_response = cl.describe_route_tables()
rtbs = rtb_response.get('RouteTables', {})
for x in rtbs:
    #print x['RouteTableId'], x['VpcId']
    if x['VpcId'] == v[0]['VpcId'] and v[0]['IsDefault'] == True:
        print "I will be deleting this Route Table", x['RouteTableId']
        #delete_rtb_response = cl.delete_route_table(DryRun=True,RouteTableId=x['RouteTableId'])
        #print delete_rtb_response
    else:
        print "I will NOT be deleting", x['RouteTableId']

sg_response = cl.describe_security_groups()
sgs = sg_response.get('SecurityGroups', {})
for x in sgs:
    #print x['GroupId'], x['GroupName'], x['VpcId']
    if x['VpcId'] == v[0]['VpcId'] and v[0]['IsDefault'] == True:
        print "I will be deleting this SecurityGroup", x['GroupId']
        #delete_sg_response = cl.delete_security_group(DryRun=True,GroupName=x['GroupName'],GroupId=x['GroupId'])
        #print delete_sg_response
    else:
        print "I will NOT be deleting", x['GroupId']
