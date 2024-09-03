# Hello-World-Microservices-Application

# Course Enterprise Software Platform

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

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/tasks/tools/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (for local Kubernetes cluster)
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Setup

### 1. Setting Up the Development Environment
1. **Install Necessary Tools**:
   - For Java: Install JDK and Maven.
2. **Create a Git Repository**:
   - Initialize a Git repository in your project directory.

### 2. Creating the Microservices
1. **Create a new project**:
   - For Java: Use Spring Initializr or your preferred IDE(used VSCode in this project) to create a Spring Boot application.
2. **Add Endpoint**:
   - Create an endpoint `/hello` that returns the string "Hello".
   - Create an endpoint `/world` that returns the string "World".
3. **Check the services**
   - open http://localhost:8080/hello to check Hello Service
   - open http://localhost:8083/world to check World service
   (Use the port numbers that you assigned)
   

### 3. Containerizing the Microservices with Docker
1. Create Dockerfiles
- **Hello Service**: Create a `Dockerfile` in the `hello-service` directory.
- **World Service**: Create a `Dockerfile` in the `world-service` directory.

Here are example `Dockerfile` contents:
**Hello Service Dockerfile:**
```Dockerfile
FROM openjdk:22
COPY target/hello-service.jar /app/hello-service.jar
ENTRYPOINT ["java", "-jar", "/app/hello-service.jar"]
```
**World Service Dockerfile:**
```Dockerfile
FROM openjdk:22
COPY target/world-service.jar /app/world-service.jar
ENTRYPOINT ["java", "-jar", "/app/world-service.jar"]
```

2. Build Docker Images:
```bash
docker build -t <your-dockerhub-username>/hello-service:latest -f hello-service/Dockerfile .
docker build -t <your-dockerhub-username>/world-service:latest -f world-service/Dockerfile .
```

3. Push Docker Images to Docker Hub:
```bash
docker push <your-dockerhub-username>/hello-service:latest
docker push <your-dockerhub-username>/world-service:latest
```

### 4. Deploying the Application on Kubernetes
1. Start Minikube:
```bash
minikube start
```
2. Apply Kubernetes Manifests:
```bash
cd ../kubernetes
kubectl apply -f hello-deployment.yaml
kubectl apply -f hello-service.yaml
kubectl apply -f world-deployment.yaml
kubectl apply -f world-service.yaml
```
3. Verify Deployments and Services:
```bash
kubectl get pods
kubectl get services
```

### 5. Testing and Integration
1. Port Forward Services:
   Hello Service:
   ```bash
   kubectl port-forward svc/hello-service 8080:80
   ```
   World Service:
   ```bash
   kubectl port-forward svc/world-service 8083:80
   ```
2. Run the Integration Script:
```bash
cd ..
python integration_test.py
```
Output:
```bash
Hello World
```
## Docker Images

- **Hello Service**: [bhavikasodagum/hello-service](https://hub.docker.com/r/bhavikasodagum/hello-service)
- **World Service**: [bhavikasodagum/world-service](https://hub.docker.com/r/bhavikasodagum/world-service)

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Start Minikube**:
    ```bash
    minikube start
    ```

3. **Deploy Services to Kubernetes**:
    ```bash
    cd kubernetes
    kubectl apply -f hello-deployment.yaml
    kubectl apply -f hello-service.yaml
    kubectl apply -f world-deployment.yaml
    kubectl apply -f world-service.yaml
    ```

4. **Port Forward Services**:
    - **Hello Service**:
        ```bash
        kubectl port-forward svc/hello-service 8080:80
        ```
    - **World Service** (Open a new terminal):
        ```bash
        kubectl port-forward svc/world-service 8083:80
        ```

5. **Run Integration Test**:
    ```bash
    cd ..
    python integration_test.py
    ```

    **Expected Output**:
    ```
    Hello World
    ```





