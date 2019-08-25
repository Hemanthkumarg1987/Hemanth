'''
#!/usr/bin/python
x=1
y=type(x)
print(y)


def demo_func(x,y=5):
  z=x+y
  return z

print(demo_func(4))
'''
import json

ec2 = '{ "region":"us-east1", "count":3, "type":"t2.micro"}'

data = json.loads(ec2)

print(data["region"])

data["region"] = "eu-west2"

ec2 = json.dumps(data)

print(ec2)


'''
x=2
y=2
z=2
if (x==y) and (x==z):
	print("Condition matched")
else:
	print("No Matches")

'''
