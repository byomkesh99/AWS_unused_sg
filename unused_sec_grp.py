import boto3

def find_security_groups_without_network_interfaces():
    # Create a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_DEFAULT_REGION  # Replace with your desired region
    )

    # Create an EC2 client
    ec2_client = session.client('ec2')

    # Retrieve a list of all security groups
    response = ec2_client.describe_security_groups()
    security_groups = response['SecurityGroups']

    # Find security groups without network interfaces
    security_groups_without_interfaces = []
    for group in security_groups:
        if len(group['IpPermissionsEgress']) == 0 and len(group['IpPermissions']) == 0:
            security_group_info = {
                'GroupId': group['GroupId'],
                'Name': group['GroupName'],
                'Description': group['Description']
            }
            security_groups_without_interfaces.append(security_group_info)

    # Print the security groups without network interfaces
    print("Security Groups without Network Interfaces:")
    for group_info in security_groups_without_interfaces:
        print(f"ID: {group_info['GroupId']}")
        print(f"Name: {group_info['Name']}")
        print(f"Description: {group_info['Description']}")
        print("---")

# Call the function to find security groups without network interfaces
find_security_groups_without_network_interfaces()
