# Hello-World-Microservices-Application

## Description
This project demonstrates a simple "Hello World" microservices application using Spring Boot (Java), Docker, and Kubernetes. It consists of two microservices:
- **Hello Service**: Returns a message ("Hello").
- **World Service**: Returns a message ("World").

These services are containerized using Docker and deployed on a Kubernetes cluster. An integration script combines their responses to display "Hello World".

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [1. Setting Up the Development Environment](#1-setting-up-the-development-environment)
  - [2. Creating the Microservices](#2-creating-the-microservices)
  - [3. Containerizing the Microservices with Docker](#3-containerizing-the-microservices-with-docker)
  - [4. Deploying the Application on Kubernetes](#4-deploying-the-application-on-kubernetes)
  - [5. Testing and Integration](#5-testing-and-integration)
- [Docker Images](#docker-images)
- [Usage](#usage)
- [License](#license)

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/tasks/tools/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (for local Kubernetes cluster)
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Setup

1. Setting Up the Development Environment

### Clone the Repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
###Install Dependencies:

For Node.js services, ensure you run npm install inside each service directory if applicable.

2. Creating the Microservices


