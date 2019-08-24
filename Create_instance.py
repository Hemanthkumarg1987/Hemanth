import boto3

ec2 = boto3.resource('ec2')

#define your instance
instances = ec2.create_instances(
     ImageId='ami-0009a33f033d8b7b6',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='python-key'
 )
