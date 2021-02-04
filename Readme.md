[![<ORG_NAME>](https://circleci.com/gh/andtlopez/devops-capstone.svg?style=svg)](https://circleci.com/gh/andtlopez/devops-capstone)

# Devops-Capstone
CI/CD Pipeline for a microservices Hello World Python application using CircleCI, Docker, Kubernetes and AWS

## Project Overview

Develop a CI/CD Pipeline that builds, lints (typographical code checking), creates updated Dockerized application, and rollout updates to an existing Kubernetes cluster with the updated Dockerized application.

### Project Tasks

* Test your project code using linting
* Create a Dockerfile to containerize this application
* Deploy your containerized application using Docker
* Build infrastructure on AWS with EKS and Managed Node Group
* Configure EKS Cluster
* Update EKS Cluster with the updated Docker image

---
## Build AWS EKS Infrastructure

* Create network
`./create-eks-network.sh capstone-network eks-network.yml network-params.json`

* Create EKS Cluster
`./create-eks-cluster.sh capstone-cluster eks-cluster.yml cluster-params.json`

* Create EKS Node Group
`./create-eks-nodes.sh capstone-nodes eks-nodegroup.yml node-params.json`

## Setup the Environment

* Create a virtualenv and activate it
python3 -m venv ~/.devops
source ~/.devops/bin/activate

* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Docker Steps
* Build Image: `docker build --tag=andtlopez/devops-capstone .`
* Run via docker: `docker run -p 8080:8888 andtlopez/devops-capstone`
* Upload image: `./upload_docker.sh`

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
    1. Install minikube
    2. Run minikube: `minikube start`
* Create Flask app in Container
* Run via kubectl
    1. `kubectl run devops --image=andtlopez/devops-capstone --port=8888 --labels app=devops`
    2. `kubectl port-forward devops 8080:8888`

### List of Files
* app.py: Python web application
* Cloudformation/: Contains Cloudformation scripts to build the AWS infrastructure
* Cloudformation/create-eks-network.sh: Helper script that creates the AWS Network
* Cloudformation/eks-network.yml: Cloudformation script that creates the AWS Network
* Cloudformation/network-params.json: JSON file that contains the network parameters
* Cloudformation/create-eks-cluster.sh: Helper script that creates the AWS EKS cluster
* Cloudformation/eks-cluster.yml: Cloudformation script that creates the AWS EKS cluster
* Cloudformation/cluster-params.json: JSON file that contains the EKS cluster parameters
* Cloudformation/create-eks-nodes.sh: Helper script that creates the AWS Node group
* Cloudformation/eks-nodegroup.yml: Cloudformation script that creates the AWS Node group
* Cloudformation/node-params.json: JSON file that contains the AWS Node group parameters
* kubernetes/k8s.yml: Deployment file for a Kubernetes cluster
* Makefile: install, test, and lint
* requirements.txt: app dependencies
* Dockerfile: Docker config
* run_docker.sh: Script that builds Docker image
* upload_docker.sh: Uploads image to Docker Hub
* run_kubernetes.sh: Script that builds a Kubernetes pod
* .circleci/config.yml: CircleCI config file