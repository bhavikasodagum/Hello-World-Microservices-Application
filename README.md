# Hello World Microservices Application

## Course: Enterprise Software Platform

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

## Setup

### 1. Setting Up the Development Environment
1. Install Necessary Tools:
   - For Java: Install JDK and Maven.
   - For integration script: Python.
     
### 2. Creating the Microservices
1. Create a Spring Boot Project:
Go to Spring Initializr and choose the following options:
- Project: Maven Project
- Language: Java
- Spring Boot: (Use the latest stable version)
- Group: com.example
- Artifact: hello-service 
- Dependencies: Web

Download and Extract the generated ZIP file and open the project in your IDE(VScode has been used for this project)

2. Implement Hello Service:
  - Create a Controller in src/main/java/com/example/hello_service,
   create a new class HelloController.java:
   ```bash
   package com.example.helloservice;
   import org.springframework.web.bind.annotation.GetMapping;
   import org.springframework.web.bind.annotation.RequestMapping;
   import org.springframework.web.bind.annotation.RestController;

   @RestController
   @RequestMapping("/hello")
   public class HelloController {
    @GetMapping
    public String sayHello() {
        return "Hello";
    }
   }
   ```
   in src/main/resources/application.properties add:
   ```
   server.port=8080
   ```
  - Run the application by executing mvn spring-boot:run 
  - Verify: Open your browser or use curl to test: http://localhost:8080/hello

3. Create a Spring Boot Project:
Go to Spring Initializr and choose the following options:
- Project: Maven Project
- Language: Java
- Spring Boot: (Use the latest stable version)
- Group: com.example
- Artifact: world-service  
- Dependencies: Web
  
Download and Extract the generated ZIP file and open the project in your IDE(VScode has been used for this project)

4. Implement World Service:
  - Create a Controller in src/main/java/com/example/world_service
    create a new class WorldController.java:
    ```bash
    package com.example.worldservice;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @RequestMapping("/world")
    public class WorldController {
    @GetMapping
    public String sayWorld() {
        return "World";
    }
    }
    ```
    in src/main/resources/application.properties add:
    ```
    server.port=8083
    ```
  - Run the application by executing mvn spring-boot:run 
  - Verify: Open your browser or use curl to test: http://localhost:8083/world

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
docker build -t hello-service .
docker build -t world-service .
```

3. Push Docker Images to Docker Hub:
 
  Tag :
```bash
docker tag hello-service bhavikasodagum/hello-service:latest
docker tag world-service bhavikasodagum/world-service:latest
```
  Push:
```bash
docker push bhavikasodagum/hello-service:latest
docker push bhavikasodagum/world-service:latest
```

4. Run the Hello Service Container:
```bash
docker run -d -p 8080:8080 hello-service
```

5. Run the World Service Container:
```bash
docker run -d -p 8083:8083 world-service
```

6. Test the Services Locally:
Open Your Browser and visit these URLs:
http://localhost:8080/hello to test the Hello service.
http://localhost:8083/world to test the World service.

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
2. Write script for integration
   example:
   ```bash
   import requests

   # Define the endpoints
   hello_url = "http://localhost:8080/hello"
   world_url = "http://localhost:8083/world"

   try:
    # Make requests to the services
    hello_response = requests.get(hello_url)
    world_response = requests.get(world_url)

    # Check if both requests were successful
    if hello_response.status_code == 200 and world_response.status_code == 200:
        # Combine and print the responses
        combined_message = f"{hello_response.text} {world_response.text}"
        print(combined_message)
    else:
        print("Failed to retrieve responses from one or both services.")
        print(f"Hello Service Status Code: {hello_response.status_code}")
        print(f"World Service Status Code: {world_response.status_code}")

    except requests.RequestException as e:
    print(f"An error occurred: {e}")
   ```
4. Run the Integration Script:
```bash
cd ..
python3 integration_test.py
```
Output:
```bash
Hello World
```
## Docker Images

- **Hello Service**: [bhavikasodagum/hello-service](https://hub.docker.com/r/bhavikasodagum/hello-service)
- **World Service**: [bhavikasodagum/world-service](https://hub.docker.com/r/bhavikasodagum/world-service)

## Usage

1. **Start Minikube**:
    ```bash
    minikube start
    ```

2. **Deploy Services to Kubernetes**:
    ```bash
    cd kubernetes
    kubectl apply -f hello-deployment.yaml
    kubectl apply -f hello-service.yaml
    kubectl apply -f world-deployment.yaml
    kubectl apply -f world-service.yaml
    ```

3. **Port Forward Services**:
    - **Hello Service**:
        ```bash
        kubectl port-forward svc/hello-service 8080:80
        ```
    - **World Service** (Open a new terminal):
        ```bash
        kubectl port-forward svc/world-service 8083:80
        ```

4. **Run Integration Test**:
    ```bash
    python3 integration_test.py
    ```

    **Expected Output**:
    ```
    Hello World
    ```





