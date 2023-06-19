import boto3
import os

def search_sg_with_no_interfaces():
    # Create a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('AWS_DEFAULT_REGION')
    )

    # Session for EC2 Client
    ec2_client = session.client('ec2')

    # Getting the network interfaces in user account
    response = ec2_client.describe_network_interfaces()

    # Extract the security group IDs from the network interfaces
    interface_sg_ids = [interface['Groups'][0]['GroupId'] for interface in response['NetworkInterfaces']]

    # Getting  security groups (SGs) in user account
    response = ec2_client.describe_security_groups()

    # Filter sg with no network interfaces
    security_groups = []
    for group in response['SecurityGroups']:
        if group['GroupId'] not in interface_sg_ids:
            security_groups.append(group)

    return security_groups

# Calling the function to find SGs with no network interfaces
result = search_sg_with_no_interfaces()

# Print the SG details
for group in result:
    print("Security Group ID:", group['GroupId'])
    print("Security Group Name:", group['GroupName'])
    print("Security Group Description:", group['Description'])
    print("---")
