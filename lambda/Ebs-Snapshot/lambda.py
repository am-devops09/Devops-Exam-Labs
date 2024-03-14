import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes()['Volumes']

    for volume in volumes:
        snapshot = ec2.create_snapshot(VolumeId=volume['VolumeId'])
        ec2.create_tags(Resources=[snapshot['SnapshotId']], Tags=[{'Key': 'Name', 'Value': 'Lambda Snapshot '+datetime.datetime.now().strftime('%Y-%m-%d')}])

    return 'Snapshots created successfully!'


