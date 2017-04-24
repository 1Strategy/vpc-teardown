#!/usr/bin/env python
import boto3
import json

inuser = boto3.session.Session(profile_name='ic-identity')
client = inuser.client('sts', region_name='ap-southeast-1')
assumedRoleObject = client.assume_role(
    RoleArn='arn:aws:iam::751344753113:role/GroupAccess-Contractors-1Strategy',
    RoleSessionName='test-ic-compliance',
    DurationSeconds=3600,
    SerialNumber='arn:aws:iam::736763050260:mfa/aaron.caldiero',
    TokenCode='958360'
)
print assumedRoleObject["AssumedRoleUser"]
print assumedRoleObject["AssumedRoleUser"]["AssumedRoleId"]
print assumedRoleObject["AssumedRoleUser"]["Arn"]
print assumedRoleObject["Credentials"]
print assumedRoleObject["Credentials"]["SecretAccessKey"]
print assumedRoleObject["Credentials"]["SessionToken"]
print assumedRoleObject["Credentials"]["Expiration"]
print assumedRoleObject["Credentials"]["AccessKeyId"]

credentials = assumedRoleObject['Credentials']

# Use the temporary credentials that AssumeRole returns to make a
# connection to Amazon S3
s3_resource = boto3.resource(
    's3',
    aws_access_key_id = credentials['AccessKeyId'],
    aws_secret_access_key = credentials['SecretAccessKey'],
    aws_session_token = credentials['SessionToken'],
)

# Use the Amazon S3 resource object that is now configured with the
# credentials to access your S3 buckets.
for bucket in s3_resource.buckets.all():
    print(bucket.name)

# cl = inuser.client('ec2', region_name='ap-southeast-1')
# response = cl.describe_vpcs()
# v = response.get('Vpcs', {})
# print v
# response_delete_vpc = cl.delete_vpc(DryRun=True,VpcId=p[0])
# print response_delete_vpc
