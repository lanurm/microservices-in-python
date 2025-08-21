# Scalable Microservices Architecture Using Python & Kubernetes

## Overview
This project demonstrates a scalable microservices application built using Python Flask. The app is containerized using Docker, managed locally with Docker Compose, and deployed to a Kubernetes cluster using Helm charts. It showcases best practices for microservices deployment, orchestration, and scaling on Kubernetes.

## Features
- Modular Flask microservices architecture  
- Containerization with Docker  
- Local orchestration using Docker Compose  
- Kubernetes deployment with Helm charts for easy scaling and management  
- Real-time service interaction and scalability

## Tech Stack
- Python 3.x (Flask)  
- Docker & Docker Compose  
- Kubernetes  
- Helm  
- Helm Charts for deployment automation

## Project Structure
- /app      # Flask microservices source code
- /docker   # Dockerfiles and Compose files
- /helm     # Helm chart for Kubernetes deployment
- README.md # This documentation file


## Setup and Deployment

### Prerequisites
- Python 3.x installed  
- Docker installed and running  
- Kubernetes cluster up and running (e.g., Minikube, Docker Desktop Kubernetes)  
- Helm installed

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lanurm/microservices-in-python.git
   cd microservices

2.**Build and run locally using Docker Compose:**
    ```bash
    
    docker-compose up --build
    Access the app at http://localhost:<port> as configured.

3. **Deploy to Kubernetes with Helm:**

   - Create the Kubernetes cluster or start Minikube:
      ```bash
      minikube start

    - Deploy using Helm:
      ```bash
      helm install webapp ./helm/webapp
      
    - To check the service URL:
      ```bash
      minikube service web-service --url

     Access the app by opening the URL printed by the above command in your browser.
   
5. **Cleanup:**
  - To uninstall the Helm deployment:
    ```bash
    helm uninstall webapp
    
  - To stop Minikube:
    ```bash
    minikube stop
