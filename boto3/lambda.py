import boto3





# Here a simple example of s3 with attribute create_date and name 

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     state = (bucket.creation_date)
#     bucket = (bucket.name)
#     print("The bucket {} is created {}".format(bucket, state))


# Here we will try to get all Security Groups with our Aws Account

ec2 = boto3.resource('ec2')
# Identifiers (only 'id')

security_group = ec2.SecurityGroup('id')

# response = ec2.describe_vpcs()
# print (response)


for security_group in ec2.security_groups.all():
    try: 
       tag = security_group.create_tags(Tags=[{'Key': 'env3', 'Value': 'dev3'}])
       print('Tags Successfully Set %s' % tag)
       
    except:
       print ('Something went wrong !!! ')

snapshot = ec2.Snapshot('id')
for snap in ec2.snapshots.all():
   print(snap)

