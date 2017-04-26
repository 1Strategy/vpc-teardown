import boto3


ec2_client = []
dry_run = True


def lambda_handler(event, context):
    pass


def teardown_default_route_tables(event, context):

    global ec2_client
    ec2_client = boto3.client('ec2', region_name=event['region'])

    global dry_run
    dry_run = event.get('dry_run', True)

    protected_resources = event.get('protected_resources', [])
    targeted_resources = event.get('targeted_resources', [])

    route_tables = ec2_client.describe_route_tables()['RouteTables']

    for route_table in route_tables:
        vpc_id = route_table['VpcId']
        if protected_resource(protected_resources, vpc_id):
            continue
        if targeted_resource(targeted_resources, vpc_id):
            disassociate_route_table(route_table)
            delete_route_table(route_table)


def disassociate_route_table(associations):
    for association in associations['Associations']:
        print('Disassociating: ' + association['RouteTableAssociationId'])
        try:
            ec2_client.disassociate_route_table(DryRun=dry_run,
                                                AssociationId=association['RouteTableAssociationId'])
        except Exception as e:
            print(e)


def delete_route_table(route_table):
    try:
        ec2_client.delete_route_table(DryRun=dry_run,
                                      RouteTableId=route_table['RouteTableId'])
    except Exception as e:
        print(e)


def protected_resource(protected_resources, resource):
    if resource in protected_resources:
        return True
    return False


def targeted_resource(targeted_resources, resource):
    if targeted_resources == []:
        return True
    if resource in targeted_resources:
        return True
    return False


if __name__ == '__main__':
    teardown_default_route_tables(
        {
            'region': 'us-west-2',
            'targeted_resources': ['vpc-dafffbbe', 'vpc-559b2731'],
            'protected_resources': ['vpc-dafffbbe'],
            'dry_run': True
        }, {})
