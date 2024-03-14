#get volume of an ec2 instance

# 1 - event : get instance_id
import boto3

ec2 = boto3.resource('ec2')
# Instance_ID=('')
# for instance in ec2.instances.all():
#     instance_id = (instance.instance_id)
#     image_id= (instance.image_id)
#     print(instance)
#     print("instance id is ",instance_id)
#     print("image id is ", image_id)
# # 2- get volume id from instance_id
#     vols = instance.volumes.all()
#     for v in vols:
#         Volume_id=(v.id)
#         print(Volume_id)

# 3- create snapshot of the volume_id
# snapshot = ec2.create_snapshot(
#     Description='Creating snapshot',
#     VolumeId=(Volume_id)
# )

instance_id=('i-0aaadf20b274dd62a')
vols =ec2.Instance(instance_id).volumes.all()
for v in vols:
    volume_id=(v.id)
    print(volume_id)
    snapshot = ec2.create_snapshot(VolumeId=(volume_id))

    
    




