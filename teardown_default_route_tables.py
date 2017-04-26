import boto3


ec2_client = []


def lambda_handler(event, context):
    pass


def teardown_default_route_tables(event, context):

    global ec2_client

    protected_resources = event.get('protected_resources', [])
    targeted_resources = event.get('targeted_resources', [])

    ec2_client = boto3.client('ec2', region_name=event['region'])
    route_tables = ec2_client.describe_route_tables()['RouteTables']

    for route_table in route_tables:
        if route_table['VpcId']
            associations = route_table['Associations']
            for association in associations:
                print(association['RouteTableAssociationId'])
        # response = client.disassociate_route_table(DryRun=False,
        #                                            AssociationId='string')
        #


def protected_resource(protected_resources, resource):
    if resource in protected_resources:
        return True
    return False

if __name__ == '__main__':
    teardown_default_route_tables({'region': 'us-west-2', 'targeted_resouces': ['vpc']}, {})
