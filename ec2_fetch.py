import boto3

# Initialize a session with the specific region (us-east-1)
session = boto3.Session(region_name="us-east-1")

# Initialize the EC2 client
ec2_client = session.client("ec2")

# Retrieve information about all EC2 instances in us-east-1
response = ec2_client.describe_instances()

# Parse and display the instance information
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Instance State: {instance['State']['Name']}")
        print(f"Public IP Address: {instance.get('PublicIpAddress', 'No Public IP')}")
        print(f"Private IP Address: {instance['PrivateIpAddress']}")
        print("-" * 60)

