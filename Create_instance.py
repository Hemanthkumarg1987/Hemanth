#!/usr/bin/python
import boto3

ec2 = boto3.resource('ec2')

#define your instance
instances = ec2.create_instances(
     ImageId='ami-0d8f6eb4f641ef691',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='python-key'
     region_name='us-east-2'
 )
