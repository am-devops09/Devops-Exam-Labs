import json
import boto3
import time

#https://stackoverflow.com/questions/68927782/is-it-possible-to-extract-instanceid-from-eventbridge-event-data-and-use-it-a
# https://shishirkh.medium.com/sending-ec2-logs-to-s3-via-lifecycle-hooks-66d4d059596e
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
        
        print(event)
        account_id = event['account']
        print(account_id)
        ec2_instance = event['detail']['instance-id']
        print(ec2_instance)
        

        # CReating Snapshot
        print(' Looking up for Volume_id of the Instance ...')
        volumes=ec2.Instance(ec2_instance).volumes.all()
        for volume in volumes:
            volume_id= volume.id
            print('Volume ID: '+volume_id)
            #Create snapshot of every volume attached to instance
            snapshot=volume.create_snapshot(Description='Snapshot Created by Lambda')
            print(snapshot)
        

      
        #Lets create now an ami snapshot
        instance=ec2.Instance(ec2_instance)
        image=instance.create_image(Name='AMI Created by lambda',Description='AMI Created by lambda')
        print('AMI ID : ' +image.id)






