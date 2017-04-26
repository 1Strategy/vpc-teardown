import boto3


ec2_client = []


def lambda_handler(event, context):
    teardown_default_subnets(event, context)


def teardown_default_subnets(event, context):
    global ec2_client
    ec2_client = boto3.client('ec2', region_name=event['region'])

    global dry_run
    dry_run = event.get('dry_run', True)

    protected_resources = event.get('protected_resources', [])
    targeted_resources = event.get('targeted_resources', [])

    subnets = ec2_client.describe_subnets()['Subnets']

    for subnet in subnets:
        vpc_id = subnet['VpcId']
        if targeted_resource(targeted_resources, vpc_id) and not \
                protected_resource(protected_resources, vpc_id):
            print(subnet['SubnetId'])


def protected_resource(protected_resources, resource):
    if resource in protected_resources:
        return True
    return False


def targeted_resource(targeted_resources, resource):
    if resource in targeted_resources:
        return True
    return False


if __name__ == '__main__':
    lambda_handler({'region': 'us-west-2'}, {})
