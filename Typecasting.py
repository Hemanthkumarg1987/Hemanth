'''
#!/usr/bin/python
x=1
y=type(x)
print(y)
'''

def demo_func(x,y=5):
  z=x+y
  return z

print(demo_func(4))
