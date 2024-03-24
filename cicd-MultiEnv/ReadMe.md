# create 2 env dev and prod

code commit for files repo
code deploy to deploy app to dev and prod Autoscaling group {
    First deploy to env envi
    Then
    Manual approuval
    and 
    deploy to prod
}

#


infra As code 
Deployement Group Dev Prod
Pipeline commit dev deploy dev test MAnual approval Deploy Prod


# infra  (DEV and PROD)
Multi env ( 2 alb and two tg and asgs)

# Roles: 
    Ec2 instance Profile Role (policy ec2AwsCodedeployrole)
    codeDeploy role : AwsCodeDeployrole  (add it to cloudformation now :::!!!!)


# CodeDeploy

 APplication : DevopsBlogApp
 DeployementGroup : DEv and PRod

# Pipeline

push to dev :
   Pipeline  : [ code build : zip file and send it to s3 ,  CodeDeploy Deploy file from s3 to ec2DevENV , test: codebuild ,  pull request to prod , Manual Approval , Deploy to Prod]
   