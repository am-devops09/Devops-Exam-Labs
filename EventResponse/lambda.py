import boto3
import json
import time

ec2 = boto3.resource('ec2')
ssm_client= boto3.client('ssm')

def lambda_handler(event, context):

    ## Send EC2 logs to s3
    ec2_instance = event['detail']['EC2InstanceId']
    asg_name = event['detail']['AutoScalingGroupName']
    hook_name=event['detail']['LifecycleHookName']
    document_name='ssm-poc'
    document_version = '1'

    response = ssm_client.send_command(InstanceIds=[ec2_instance],DocumentName=document_name,DocumentVersion=document_version,TimeoutSeconds=300,Parameters={'hookname':[hook_name],'asgname':[asg_name],'instanceid':[ec2_instance]})
    command_id= response['Command']['CommandId']
    time.sleep(5)
    

    output= ssm_client.get_command_invocation(
        CommandId=command_id,
        InstanceId=ec2_instance
    )
    print(output)
    return {
        'statusCode': 200,
        'body': json.dump(output)
    }

    ## Create Snapshot of Terminated instance
    volume = ec2_instance.volumes.all()
    for volume in volumes:
        volume_id=(volume.id)
        snapshot = volume.create_snapshot(VolumeId=('volume_id'))
        print(volume_id)