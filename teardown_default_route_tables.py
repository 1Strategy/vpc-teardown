import boto3


ec2_client = []


def lambda_handler(event, context):
    global ec2_client
    ec2_client = boto3.client('ec2', region_name=event['region'])
    route_tables = ec2_client.describe_route_tables()['RouteTables']

    for route_table in route_tables:
        print(route_table['Associations'])
        response = client.disassociate_route_table(DryRun=False,
                                                   AssociationId='string')
        

lambda_handler({'region': 'us-west-2'}, {})
