import boto3


ec2_client = []


def lambda_handler(event, context):
    global ec2_client
    ec2_client = boto3.client('ec2', region_name=event['region'])
    subnets = ec2_client.describe_subnets()

    for subnet in subnets['Subnets']:
        print(subnet['VpcId'])
        print(subnet['SubnetId'])


lambda_handler({'region': 'us-west-2'}, {})
