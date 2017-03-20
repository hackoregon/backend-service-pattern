
[![Build Status](https://travis-ci.org/hackoregon/backend-service-pattern.svg?branch=master)](https://travis-ci.org/hackoregon/backend-service-pattern)

## Hack Oregon Exemplar Backend Service

NOTE: this is based on the Homelessness team's backend repo, and as such still includes many hardcoded references to "homeless" and/or "homelessness". You will want to update all such app-specific references when implementing this pattern for your project's application.  

## Purpose

Demonstrates CI/CD for HackOregon Django Service

## Dependencies

* Docker or Docker toolkit
* Travis-CI
* Cluster deployment keys  - Contact the DevOps team
* ECR Password - Contact the DevOps Team
* ECS Service Name - See Section 5


## How to build

### 1.  Create Your Environment file

* Create `env.sh` in the project with the following contents:

```bash
#! /bin/bash
# Setup Project Specfics - Make sure env.sh is in the .gitignore and .dockerignore
export DOCKER_IMAGE= #see section 5 for conventions
export PROJ_SETTINGS_DIR= #see section 5 for conventions
export DEPLOY_TARGET=dev # it's always dev on your local machine
echo "##############################"
echo  Your Local Project Environement
echo "##############################"
echo DOCKER_IMAGE $DOCKER_IMAGE
echo PROJ_SETTINGS_DIR $PROJ_SETTINGS_DIR
echo DEPLOY_TARGET $DEPLOY_TARGET
```
### 2. Setup your local environment

* Run `source env.sh` to setup your environment

### 3. Build & Test the container

* Run `./bin/build-test-proj -l` to build your container locally

**Note:** For this to work correctly you will need to get your DBA to run the following SQL as the postgres user:

```SQL
GRANT CONNECT ON database postgres TO <your_db_user>;
GRANT USAGE ON SCHEMA public to <your_db_user>;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO <your_db_user>;
```

### 4. Start the project

* Make sure you've got a local copy of your projects's `project_config.py`
* Run `./bin/start-proj -l` to view your service's swaggerized API

### 5. Setup your project in travis

* Set up the following environment variables

```bash
 ECS_SERVICE_NAME       #Your service name as defined on the ECS Cluster. Valid values for the integration cluster are:
                        # - civiclab            "hacko-integration-CivicLabService-SHCQWODY5CF4-Service-5R2TN149GD71"
                        # - budget              "hacko-integration-BudgetService-16MVULLFXXIDZ-Service-1BKKDDHBU8RU4"
                        # - emergency response  "hacko-integration-EmerreponseService-1LC4181KR6KN5-Service-1WR6VWC6KKIEP"
                        # - homelessness        "hacko-integration-HomelessService-1MT93S2GQTJZ4-Service-15OXS2BV07GN0"
                        # - housing             "hacko-integration-HousingService-1LLLKFJR36AJ5-Service-15AO7849OUCYV"
                        # - transportation      "hacko-integration-transportService-67KME5SFWBJO-Service-12UZIOOA2FNIK"
                        #
 ECS_CLUSTER            # Use "hacko-integration"
                        #
 DOCKER_REPO            # Use "845828040396.dkr.ecr.us-west-2.amazonaws.com"
                        #
 DOCKER_IMAGE           # The name of your service. Valid values are:
                        # - civiclab            "civic-lab-service"
                        # - budget              "budget-service"
                        # - emergency response  "emergency-service"
                        # - homelessness        "homeless-service"
                        # - housing             "housing-service"
                        # - transportation      "transport-service"
                        #
 DOCKER_USERNAME        # use "AWS"
                        #
 DOCKER_PASSWORD        # Contact the DevOps team to get this and help with setup
                        #
 DEPLOY_TARGET          # What environment you are deploying to. Valid values are:
                        # - For travis integration deploys: "integration"
                        #
 PROJ_SETTINGS_DIR      # the directory (relative to your top-level) where your configuration files are found. Valid values are:
                        # - civiclab            "civiclabSettings"
                        # - budget              "budgetAPI"
                        # - emergency response  "emerresponseAPI"
                        # - homelessness        "homelessAPI"
                        # - housing             "housingAPI"
                        # - transportation      "transportationAPI"

                        #
 CONFIG_BUCKET          # The s3 configuration bucket. Valid values:
                        # - civiclab            "hacko-civiclab-config"
                        # - budget              "hacko-budget-config"
                        # - emergency response  "emerresponse-config"
                        # - homelessness        "hacko-homeless-config"
                        # - housing             "hacko-housing-config"
                        # - transportation      "hacko-transportation-config"
 AWS_DEFAULT_REGION     # Use "us-west-2"
                        #
 AWS_ACCESS_KEY_ID      # The service deployer keyid for your service (Always hide in travis)                
                        #
 AWS_SECRET_ACCESS_KEY  # The service deployer secret key for your service (Always hide in travis)
```

**IMPORTANT:** Make sure that you don't store AWS or Docker repository credentials in your github repo or expose them in travis

### 7. Commit  
* Commit and push your code and ensure travis builds and deploys correctly
