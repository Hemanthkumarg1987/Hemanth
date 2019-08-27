#!/usr/bin/python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2', aws_access_key_id="AKIAQ4DXDKQAR3DBWOFO", aws_secret_access_key="DJTLhjGYX7ZKNBXAQ0UH9YnfzxvOsRvyVsKUKyOu")

#define your instance
instances = ec2.create_instances(
     ImageId='ami-0d8f6eb4f641ef691',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro'
     
 )
