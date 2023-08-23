#!/bin/bash
# install_dependencies.sh

# Install any dependencies required by your Docker container
# For example, you might install Docker itself and other dependencies

# Update package repositories
yum update -y

# Install Docker
amazon-linux-extras install docker -y
service docker start

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/e5v7i8q7

docker pull public.ecr.aws/e5v7i8q7/test-deploy-5030
docker run -d -p 80:80 public.ecr.aws/e5v7i8q7/test-deploy-5030


