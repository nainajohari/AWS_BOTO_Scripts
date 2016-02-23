import boto.ec2
conn = boto.ec2.connect_to_region("eu-west-1")
conn.stop_instances(
instance_ids=['$instance_id'])
