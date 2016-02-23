#/usr/bin/python
from boto.ec2.connection import EC2Connection 
import boto.ec2
conn = boto.ec2.connect_to_region("eu-west-1")
conn.run_instances(
      'ami-e1398992',
       key_name='access',
       instance_type='t2.micro',
       security_groups=['ForAll']
)
