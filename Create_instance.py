#!/usr/bin/python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-2', aws_access_key_id='AKIAQ4DXDKQA7TB5JBYY', aws_secret_access_key='FQY56hQAo8v9z12KV1iw64HuWSKpHZX3xkfFu+JJ')

#define your instance
instances = ec2.create_instances(
     ImageId='ami-0d8f6eb4f641ef691',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro'
     
 )
