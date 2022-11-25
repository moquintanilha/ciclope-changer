#!/bin/bash

read -p 'What is application name: ' APPNAME
read -p 'What is your application scope (eg. stage or prod): ' APPLICATION_SCOPE
read -p 'What is your pipeline type (eg. build or deploy): ' PIPELINE_TYPE
read -p 'This application have an integration with ciclope-chatops, set a chetops url: ' CHATOPS_URL
read -p 'What is Github username: ' GITHUB_USER
read -sp 'What is GitHub Token: ' GITHUB_TOKEN

REGION="us-east-1"
K8S_NAMESPACE="ciclope"
PIPELINE_FILE_PATH="./environments/${APPLICATION_SCOPE}/${PIPELINE_TYPE}/codepipeline.yml"

if [ $PIPELINE_TYPE == "deploy" ]
then
    aws cloudformation deploy \
    --template ${PIPELINE_FILE_PATH} \
    --stack-name ${APPNAME}-${PIPELINE_TYPE}-${APPLICATION_SCOPE} \
    --region ${REGION} \
    --parameter-overrides \
    GitHubUser=${GITHUB_USER} \
    GitHubToken=${GITHUB_TOKEN} \
    ApplicationName=${APPNAME} \
    NameSpaceName=${K8S_NAMESPACE} \
    ApplicationScope=${APPLICATION_SCOPE} \
    ChatOpsUrl=${CHATOPS_URL} \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
elif [ $PIPELINE_TYPE == "build" ]
then
    aws cloudformation deploy \
    --template ${PIPELINE_FILE_PATH} \
    --stack-name ${APPNAME}-${PIPELINE_TYPE}-${APPLICATION_SCOPE} \
    --region ${REGION} \
    --parameter-overrides \
    GitHubUser=${GITHUB_USER} \
    GitHubToken=${GITHUB_TOKEN} \
    ApplicationName=${APPNAME} \
    ApplicationScope=${APPLICATION_SCOPE} \
    ChatOpsUrl=${CHATOPS_URL} \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
fi
