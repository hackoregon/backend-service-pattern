## Hack Oregon Exemplar Backend Service

## Purpose

Demonstrates CI/CD for HackOregon Django Service

## Dependencies

* Docker or Docker toolkit
* Travis-CI
* Cluster deployment keys  - Contact the DevOps team
* ECS Service Name - Contact the DevOps team

## How to build

### 1.  Create Your Environment file

* Create `env.sh` in the project with the following contents:

```bash
#! /bin/bash
# Setup Project Specfics - Make sure env.sh is in the .gitignore and .dockerignore
export DOCKER_REPO=<YOUR REPO>
export DOCKER_IMAGE=<the name of your service>
export DOCKER_USERNAME=<YOUR DOCKER Repository USER NAME>
export DOCKER_PASSWORD=<YOUR DOCKER Repository PASSWORD>
export ECS_CLUSTER=<THE NAME OF YOUR ECS CLUSTER>
export ECS_SERVICE_NAME=<THE NAME OF THE SERVICE YOUR DEPLOYING TO>
echo "##############################"
echo  Your Local Project Environment
echo "##############################"
echo DOCKER_REPO: $DOCKER_REPO
echo DOCKER_IMAGE: $DOCKER_IMAGE
echo DOCKER_USERNAME: $DOCKER_USERNAME
echo DOCKER_PASWORD: $DOCKER_PASSWORD
echo ECS_CLUSTER: $ECS_CLUSTER
echo ECS_SERVICE_NAME: $ECS_SERVICE_NAME
```
### 2. Setup your local environment

* Run `source env.sh` to setup your environment

### 3. Build the container

* Run `build-proj.sh` to build the Container

### 4. Start the project

* Run `start-proj.sh` to view your service's catalog page

### 5. Setup your project in travis

* Set the following environment variables

```bash
 DOCKER_REPO            # Your docker repository
 DOCKER_IMAGE           # endpoint-service
 DOCKER_USERNAME        # Your Docker Repository user name
 DOCKER_PASSWORD        # Your Docker Repository password
 ECS_CLUSTER            # The name of your ECS cluster
 ECS_SERVICE_NAME       # The name of the ECS service your deploying to
 DEPLOY_TARGET          # The deployment environment. Valid values: integration,production
 PROJ_SETTINGS_DIR      # the directory where we will place configuration files(s)
 CONFIG_BUCKET          # The s3 configuration bucket
 AWS_DEFAULT_REGION     # THE AWS region where your cluster is located
 AWS_ACCESS_KEY_ID      # The service deployer keyid for your service
 AWS_SECRET_ACCESS_KEY  # The service deployer secret key for your service
```
**Note:** If you were running this in a more real-world scenario you want your deployer user to have a role with the following policy documents attached

* Access to the configuration bucket

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::assign9-config/*"
        }
    ]
}
```
* Permissions to deploy to the ECS cluster

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecs:DescribeServices",
                "ecs:DescribeTaskDefinition",
                "ecs:DescribeTasks",
                "ecs:ListTaskDefinitions",
                "ecs:ListTasks",
                "ecs:RegisterTaskDefinition",
                "ecs:DeregisterTaskDefinition",
                "ecs:UpdateService"
            ],
            "Resource": "*"
        }
    ]
}
```

**IMPORTANT:** Make sure that you don't store AWS or Docker repository credentials in your github repo or expose them in travis

### 6. Commit  
* Commit and push your code and ensure travis builds and deploys correctly
