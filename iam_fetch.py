import boto3

# Create a session with the default profile
session = boto3.Session(profile_name="default")

# Create an IAM resource
iam_console = session.resource('iam')

# Loop through and print the name of each IAM user
for each_user in iam_console.users.all():
    print(each_user.name)
