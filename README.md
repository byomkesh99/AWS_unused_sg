# How to find un used security group for EC2 or other services in AWS.

### Using [Amazon EC2 API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html) how to find unused security groups within your AWS account. if there is no network interfaces are associated with it then you need to display name, description & Id of found unused security groups.

There are 3 files to build the docker image, and after that to get the output for un used security group we need to run the following command. The 3 files are 1) Dockerfile 2) entrypoint.sh 3) fine_unused_sec_grps.py

        docker build -t <username/appname:version> .
        docker run -e AWS_ACCESS_KEY_ID=AKIA... -e AWS_SECRET_ACCESS_KEY=... -e AWS_DEFAULT_REGION=us-east-1 your-image-id


Or I have uploaded the built image to my DockerHub repo, the output can be get from the following command
       docker run -e AWS_ACCESS_KEY_ID=<AKIA...> -e AWS_SECRET_ACCESS_KEY=<...> -e AWS_DEFAULT_REGION=us-east-1 byomkesh99/aws_bdas_usg:0.01

