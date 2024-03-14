# s3 with static website + trail and cloudwatch alarm when bucket policy changes+ athena 
create s3 and make it as website host
send logs from s3 bucket mywebsite to s3 access_logs
use athena to query logs 400 and 200
quick sight for dashboard.
create s3 alarm wheneever the bucket policy is changed 
send sns notif
and do system manager automation which will mitigate the changes and reset the s3 bucket policy as it was before

# Event Bridge 

EC2 state + sns topic 
AutoScaling

# cross-Region event routing with Amazon EventBridge

event bus in region A
rules in event B
allow events in region B to be puted in Event buse A

ok 

# Filtering event pattern 
in bellow the filtering schema 
{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": [{
        "prefix": "devopsflow101"
      }]
    }
  },
  "object": {
    "key": [{
      "suffix": ".png"
    }]
  }
}

## Aws health event bridge 

{{************ the event Must be in ## US-east-1 **********}}
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "service": ["RISK"],
    "eventTypeCategory": ["issue"],
    "eventTypeCode": ["AWS_ACCESS_KEY_EXPOSED", "AWS_RISK_IAM_QUARANTINE"]
  }
}

## lambda function which will delete the exposed credentials

ok 


## Asg hooks for scale in events 

 * triger event bridge wich will call system manager automation to send logs to cloudwatch logs
 * another action with automation which creates a snapshot of the volume
 * another action which take an ami of the terminated instance
 * sns notification to Adminitrators 


system manager : run command or automation document

install ssm on ec2 // by default ami is pre-installed on amazon linux ami
permissions within ec2 instance profile
create role ec2 with ssmManagedInstanceCore policy
create event of scale in action  -- then invoke run command whcih will run  script made by you to sennd logs to cloudwatch events
 - first make sure that ssm have permissions to send logs to CW logs


aws ec2 create-snapshot --volume-id vol-1234567890abcdef0 --description "This is my second volume snapshot."
