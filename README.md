# Task Manager DevOps Project

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com)
[![Kubernetes](https://img.shields.io/badge/kubernetes-1.25+-326CE5)](https://kubernetes.io)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**A complete, production-ready DevOps project demonstrating the full CI/CD lifecycle with infrastructure automation, monitoring, and security best practices.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Local Development](#local-development)
- [CI/CD Pipeline](#cicd-pipeline)
- [Infrastructure Provisioning](#infrastructure-provisioning)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Monitoring & Observability](#monitoring--observability)
- [Security](#security)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Overview

This project showcases a **complete DevOps implementation** for a Task Manager REST API built with Python Flask. It demonstrates industry-standard practices for:

- **Application Development**: RESTful API with database persistence
- **Containerization**: Docker and Docker Compose for local development
- **Orchestration**: Kubernetes manifests for production deployment
- **Infrastructure as Code**: Terraform for AWS resource provisioning
- **Configuration Management**: Ansible for server setup
- **CI/CD**: Automated pipelines with Jenkins and GitHub Actions
- **Monitoring**: Prometheus metrics and Grafana dashboards
- **Security**: Vulnerability scanning and code quality analysis
- **Testing**: Unit tests with pytest and coverage reporting

### Key Features

✅ Production-ready Flask microservice with PostgreSQL  
✅ Complete Docker and Kubernetes configurations  
✅ Terraform scripts for AWS infrastructure (VPC, EC2, RDS, S3)  
✅ Ansible playbooks for automated server configuration  
✅ Jenkins and GitHub Actions CI/CD pipelines  
✅ Prometheus + Grafana monitoring stack  
✅ Trivy security scanning and SonarQube integration  
✅ Comprehensive unit tests with 90%+ coverage  
✅ Health checks, readiness probes, and metrics endpoints  
✅ Blue-green deployment strategy support  

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          Load Balancer                          │
│                         (AWS ALB / Nginx)                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    Kubernetes Cluster                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Pod 1      │  │   Pod 2      │  │   Pod 3      │         │
│  │ Flask App    │  │ Flask App    │  │ Flask App    │         │
│  │ Port: 5000   │  │ Port: 5000   │  │ Port: 5000   │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                  │                  │                  │
│         └──────────────────┼──────────────────┘                  │
│                            │                                     │
└────────────────────────────┼─────────────────────────────────────┘
                             │
                   ┌─────────▼──────────┐
                   │   PostgreSQL RDS   │
                   │   (AWS Managed)    │
                   └────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     Monitoring Stack                            │
│  ┌──────────────┐        ┌──────────────┐                      │
│  │  Prometheus  │──────▶ │   Grafana    │                      │
│  │ Port: 9090   │        │  Port: 3000  │                      │
│  └──────────────┘        └──────────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Request** → Load Balancer → Kubernetes Service → Flask Pod
2. **Flask App** → PostgreSQL Database (read/write operations)
3. **Metrics Export** → Prometheus scrapes `/metrics` endpoint
4. **Visualization** → Grafana queries Prometheus for dashboards
5. **CI/CD** → GitHub → Jenkins/GitHub Actions → Docker Build → Kubernetes Deploy

---

## 🛠️ Technology Stack

### Application Layer
- **Language**: Python 3.9
- **Framework**: Flask 2.3.0
- **Database**: PostgreSQL 14
- **ORM**: SQLAlchemy
- **WSGI Server**: Gunicorn

### Infrastructure & DevOps
- **Containerization**: Docker 20.10+, Docker Compose
- **Orchestration**: Kubernetes 1.25+
- **IaC**: Terraform 1.5+
- **Configuration**: Ansible 4.0+
- **Cloud Provider**: AWS (EC2, RDS, VPC, S3, ALB)

### CI/CD
- **Primary**: Jenkins 2.400+
- **Secondary**: GitHub Actions
- **Container Registry**: Docker Hub / AWS ECR

### Monitoring & Logging
- **Metrics**: Prometheus
- **Visualization**: Grafana
- **Logs**: Structured logging to stdout (ELK Stack compatible)

### Security & Quality
- **Vulnerability Scanning**: Trivy
- **Code Quality**: SonarQube
- **Secrets Management**: GitHub Secrets, AWS Secrets Manager

### Testing
- **Framework**: pytest
- **Coverage**: pytest-cov
- **Mocking**: pytest-flask

---

## 📁 Project Structure

```
task-manager-devops/
│
├── app/                          # Application source code
│   ├── app.py                    # Main Flask application
│   ├── requirements.txt          # Python dependencies
│   └── __init__.py
│
├── tests/                        # Unit and integration tests
│   ├── test_app.py              # Application tests
│   ├── test_api.py              # API endpoint tests
│   └── conftest.py              # Test fixtures
│
├── infrastructure/               # Infrastructure as Code
│   ├── terraform/               # AWS infrastructure
│   │   ├── main.tf             # Main Terraform configuration
│   │   ├── variables.tf        # Input variables
│   │   ├── outputs.tf          # Output values
│   │   ├── vpc.tf              # VPC configuration
│   │   ├── ec2.tf              # EC2 instances
│   │   ├── rds.tf              # RDS PostgreSQL
│   │   └── s3.tf               # S3 buckets
│   │
│   └── ansible/                 # Configuration management
│       ├── playbook.yml        # Main playbook
│       ├── inventory/          # Host inventory
│       └── roles/              # Ansible roles
│
├── kubernetes/                   # Kubernetes manifests
│   ├── namespace.yaml           # Namespace definition
│   ├── deployment.yaml          # Application deployment
│   ├── service.yaml             # Kubernetes service
│   ├── configmap.yaml           # Configuration
│   ├── secret.yaml              # Secrets (base64 encoded)
│   ├── hpa.yaml                 # Horizontal Pod Autoscaler
│   └── ingress.yaml             # Ingress rules
│
├── monitoring/                   # Monitoring configuration
│   ├── prometheus/
│   │   ├── prometheus.yml      # Prometheus config
│   │   └── alerts.yml          # Alert rules
│   │
│   └── grafana/
│       ├── dashboards/         # Dashboard JSON files
│       │   └── app-dashboard.json
│       └── provisioning/       # Datasource config
│
├── scripts/                      # Utility scripts
│   ├── deploy.sh                # Deployment script
│   ├── setup.sh                 # Initial setup
│   ├── test.sh                  # Run all tests
│   └── cleanup.sh               # Cleanup resources
│
├── .github/                      # GitHub configuration
│   └── workflows/
│       ├── ci-cd.yml            # CI/CD workflow
│       └── security-scan.yml    # Security scanning
│
├── Dockerfile                    # Multi-stage Docker build
├── docker-compose.yml            # Local development stack
├── Jenkinsfile                   # Jenkins pipeline
├── .dockerignore                 # Docker ignore file
├── .gitignore                    # Git ignore file
├── sonar-project.properties      # SonarQube config
├── .trivyignore                  # Trivy ignore patterns
├── README.md                     # This file
└── LICENSE                       # MIT License
```

---

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:

- **Docker** 20.10+ ([Install](https://docs.docker.com/get-docker/))
- **Docker Compose** ([Install](https://docs.docker.com/compose/install/))
- **Python** 3.9+ (for local development)
- **Git** ([Install](https://git-scm.com/downloads))

### Clone the Repository

```bash
git clone https://github.com/yourusername/task-manager-devops.git
cd task-manager-devops
```

### Start the Application (Docker Compose)

```bash
# Start all services (app + PostgreSQL + Prometheus + Grafana)
docker-compose up -d

# Check running containers
docker-compose ps

# View logs
docker-compose logs -f app
```

### Verify the Application

```bash
# Health check
curl http://localhost:5000/health

# Create a task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Task", "description": "Test task"}'

# Get all tasks
curl http://localhost:5000/api/tasks

# Access Grafana dashboard
open http://localhost:3000
# Login: admin / admin

# Access Prometheus
open http://localhost:9090
```

**🎉 Congratulations! Your application is running.**

---

## 💻 Local Development

### Setup Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r app/requirements.txt
```

### Run PostgreSQL Locally

```bash
# Using Docker
docker run -d \
  --name postgres-dev \
  -e POSTGRES_USER=taskuser \
  -e POSTGRES_PASSWORD=taskpass \
  -e POSTGRES_DB=taskdb \
  -p 5432:5432 \
  postgres:14
```

### Run the Application

```bash
# Set environment variables
export DATABASE_URL=postgresql://taskuser:taskpass@localhost:5432/taskdb

# Run Flask app
python app/app.py

# Or use Gunicorn for production-like environment
gunicorn --bind 0.0.0.0:5000 app.app:app
```

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Code Quality Checks

```bash
# Run flake8 linting
flake8 app/ tests/

# Run black formatting
black app/ tests/

# Type checking with mypy
mypy app/
```

---

## 🔄 CI/CD Pipeline

### Jenkins Pipeline

The `Jenkinsfile` defines a complete CI/CD pipeline with the following stages:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            // Clone repository
        }
        
        stage('Test') {
            // Run unit tests
            // Generate coverage report
        }
        
        stage('Code Quality') {
            // SonarQube analysis
            // Quality gate check
        }
        
        stage('Security Scan') {
            // Trivy vulnerability scan
            // OWASP dependency check
        }
        
        stage('Build') {
            // Build Docker image
            // Tag with build number
        }
        
        stage('Push') {
            // Push to Docker Hub
        }
        
        stage('Deploy to Staging') {
            // Deploy to Kubernetes staging
            // Run smoke tests
        }
        
        stage('Manual Approval') {
            // Wait for approval
        }
        
        stage('Deploy to Production') {
            // Blue-green deployment
            // Health check verification
        }
    }
    
    post {
        always {
            // Cleanup
            // Send notifications
        }
    }
}
```

### GitHub Actions Workflow

The `.github/workflows/ci-cd.yml` provides automated CI/CD:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r app/requirements.txt
      - name: Run tests
        run: pytest tests/ --cov=app
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t task-manager:${{ github.sha }} .
      - name: Push to Docker Hub
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push task-manager:${{ github.sha }}
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/task-manager task-manager=task-manager:${{ github.sha }}
```

### Triggering the Pipeline

```bash
# Make changes and commit
git add .
git commit -m "Add new feature"
git push origin main

# Pipeline triggers automatically
# Monitor in Jenkins: http://jenkins-url:8080
# Or GitHub Actions tab
```

---

## 🏗️ Infrastructure Provisioning

### AWS Infrastructure with Terraform

#### Initialize Terraform

```bash
cd infrastructure/terraform

# Initialize Terraform
terraform init

# Validate configuration
terraform validate
```

#### Plan Infrastructure

```bash
# Create execution plan
terraform plan -out=tfplan

# Review the plan carefully
```

#### Apply Infrastructure

```bash
# Apply the plan
terraform apply tfplan

# Or apply directly (with confirmation)
terraform apply

# Save outputs
terraform output > outputs.txt
```

#### Infrastructure Components Created

- **VPC** with public and private subnets across 2 AZs
- **Internet Gateway** and **NAT Gateways**
- **Security Groups** for app and database
- **EC2 instances** for Kubernetes worker nodes
- **RDS PostgreSQL** database (Multi-AZ)
- **Application Load Balancer**
- **S3 buckets** for artifacts and backups
- **IAM roles** and policies

### Configuration with Ansible

```bash
cd infrastructure/ansible

# Test connectivity
ansible all -i inventory/hosts -m ping

# Run playbook
ansible-playbook -i inventory/hosts playbook.yml

# Specific tasks
ansible-playbook -i inventory/hosts playbook.yml --tags "docker,kubernetes"
```

### Cleanup Infrastructure

```bash
# Destroy all resources
terraform destroy

# Or selectively destroy
terraform destroy -target=aws_instance.app_server
```

---

## ☸️ Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (EKS, GKE, AKS, or Minikube)
- `kubectl` configured
- `helm` installed (optional)

### Deploy to Kubernetes

```bash
# Create namespace
kubectl create namespace task-manager

# Apply all manifests
kubectl apply -f kubernetes/ -n task-manager

# Or apply individually
kubectl apply -f kubernetes/configmap.yaml -n task-manager
kubectl apply -f kubernetes/secret.yaml -n task-manager
kubectl apply -f kubernetes/deployment.yaml -n task-manager
kubectl apply -f kubernetes/service.yaml -n task-manager
kubectl apply -f kubernetes/hpa.yaml -n task-manager
kubectl apply -f kubernetes/ingress.yaml -n task-manager
```

### Verify Deployment

```bash
# Check pod status
kubectl get pods -n task-manager

# Check deployment
kubectl get deployment task-manager -n task-manager

# Check service
kubectl get svc task-manager -n task-manager

# View logs
kubectl logs -f deployment/task-manager -n task-manager

# Describe pod for troubleshooting
kubectl describe pod <pod-name> -n task-manager
```

### Scaling

```bash
# Manual scaling
kubectl scale deployment task-manager --replicas=5 -n task-manager

# Horizontal Pod Autoscaler is already configured
# It will automatically scale between 2-10 replicas based on CPU usage
kubectl get hpa -n task-manager
```

### Update Deployment

```bash
# Update image
kubectl set image deployment/task-manager \
  task-manager=yourusername/task-manager:v2.0 \
  -n task-manager

# Rollout status
kubectl rollout status deployment/task-manager -n task-manager

# Rollback if needed
kubectl rollout undo deployment/task-manager -n task-manager
```

---

## 📊 Monitoring & Observability

### Prometheus Metrics

The Flask application exposes metrics at `/metrics`:

```bash
# View metrics
curl http://localhost:5000/metrics
```

**Available Metrics:**
- `http_requests_total` - Total HTTP requests
- `http_request_duration_seconds` - Request duration
- `flask_exporter_info` - Application info
- `task_created_total` - Total tasks created
- `task_deleted_total` - Total tasks deleted

### Prometheus Configuration

Prometheus scrapes metrics every 15 seconds:

```yaml
# monitoring/prometheus/prometheus.yml
scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['app:5000']
```

### Grafana Dashboards

Access Grafana: `http://localhost:3000`
- **Username**: admin
- **Password**: admin

**Pre-configured Dashboards:**
1. **Application Overview**
   - Request rate
   - Response time (p50, p95, p99)
   - Error rate
   - Active tasks

2. **Infrastructure Health**
   - CPU usage
   - Memory usage
   - Disk I/O
   - Network traffic

3. **Database Metrics**
   - Connection pool
   - Query performance
   - Transaction rate

### Setting Up Alerts

```yaml
# monitoring/prometheus/alerts.yml
groups:
  - name: application_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
```

---

## 🔒 Security

### Vulnerability Scanning with Trivy

```bash
# Scan Docker image
trivy image task-manager:latest

# Scan with severity filter
trivy image --severity HIGH,CRITICAL task-manager:latest

# Generate report
trivy image --format json --output report.json task-manager:latest
```

### Code Quality with SonarQube

```bash
# Run SonarQube analysis
sonar-scanner \
  -Dsonar.projectKey=task-manager \
  -Dsonar.sources=./app \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<your-token>
```

### Secrets Management

#### Using GitHub Secrets (CI/CD)

```bash
# Set secrets in GitHub repository
# Settings → Secrets → Actions → New repository secret

DOCKER_USERNAME=your-username
DOCKER_PASSWORD=your-password
KUBE_CONFIG=<base64-encoded-kubeconfig>
DATABASE_URL=postgresql://user:pass@host:5432/db
```

#### Using Kubernetes Secrets

```bash
# Create secret from literal
kubectl create secret generic db-secret \
  --from-literal=username=taskuser \
  --from-literal=password=taskpass \
  -n task-manager

# Create secret from file
kubectl create secret generic app-secret \
  --from-file=config.json \
  -n task-manager

# View secret (base64 encoded)
kubectl get secret db-secret -o yaml -n task-manager
```

### Security Best Practices Implemented

✅ Multi-stage Docker builds (reduced attack surface)  
✅ Non-root user in containers  
✅ Read-only root filesystem where possible  
✅ Security context in Kubernetes pods  
✅ Network policies for pod-to-pod communication  
✅ TLS/SSL for all external communication  
✅ Input validation and SQL injection prevention  
✅ Secrets stored securely (never in code)  
✅ Regular vulnerability scanning in CI/CD  
✅ Least privilege IAM roles  

---

## 🧪 Testing

### Unit Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_app.py -v

# Run specific test
pytest tests/test_app.py::test_create_task -v
```

### Test Coverage

```bash
# Generate coverage report
pytest tests/ --cov=app --cov-report=html --cov-report=term

# View HTML report
open htmlcov/index.html

# Coverage should be > 90%
```

### Integration Tests

```bash
# Run integration tests
pytest tests/test_integration.py -v

# These test actual API endpoints with database
```

### Load Testing (Optional)

```bash
# Install locust
pip install locust

# Run load test
locust -f tests/locustfile.py --host=http://localhost:5000

# Open browser to http://localhost:8089
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy"
}
```

#### Readiness Check
```http
GET /ready
```
**Response:**
```json
{
  "status": "ready"
}
```

#### Get All Tasks
```http
GET /api/tasks
```
**Response:**
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish DevOps project",
    "completed": false
  }
]
```

#### Create Task
```http
POST /api/tasks
Content-Type: application/json

{
  "title": "New Task",
  "description": "Task description",
  "completed": false
}
```
**Response:** `201 Created`

#### Get Task by ID
```http
GET /api/tasks/{id}
```

#### Update Task
```http
PUT /api/tasks/{id}
Content-Type: application/json

{
  "title": "Updated Task",
  "completed": true
}
```

#### Delete Task
```http
DELETE /api/tasks/{id}
```
**Response:** `204 No Content`

#### Prometheus Metrics
```http
GET /metrics
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Connection Error

**Error:** `could not connect to server: Connection refused`

**Solution:**
```bash
# Check PostgreSQL is running
docker-compose ps postgres

# Check connection string
echo $DATABASE_URL

# Restart database
docker-compose restart postgres
```

#### 2. Port Already in Use

**Error:** `port 5000: bind: address already in use`

**Solution:**
```bash
# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>

# Or use different port
docker-compose up -d --scale app=1 -p 5001:5000
```

#### 3. Kubernetes Pod Not Starting

**Error:** `CrashLoopBackOff`

**Solution:**
```bash
# Check pod logs
kubectl logs <pod-name> -n task-manager

# Describe pod
kubectl describe pod <pod-name> -n task-manager

# Check events
kubectl get events -n task-manager --sort-by='.lastTimestamp'
```

#### 4. Image Pull Error

**Error:** `ImagePullBackOff`

**Solution:**
```bash
# Check image exists
docker pull task-manager:latest

# Verify secret
kubectl get secret regcred -n task-manager

# Recreate secret
kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<username> \
  --docker-password=<password> \
  -n task-manager
```

### Debug Mode

Enable debug logging:

```bash
# In docker-compose.yml
environment:
  - FLASK_ENV=development
  - LOG_LEVEL=DEBUG

# Restart
docker-compose restart app
```

### Health Checks

```bash
# Application health
curl http://localhost:5000/health

# Database health
curl http://localhost:5000/ready

# Prometheus health
curl http://localhost:9090/-/healthy

# Grafana health
curl http://localhost:3000/api/health
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: `pytest tests/`
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Code Standards

- Follow PEP 8 style guide
- Write unit tests for new features
- Update documentation
- Ensure all tests pass
- Run linting before committing

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Flask framework and community
- Kubernetes project
- Prometheus and Grafana teams
- HashiCorp for Terraform
- All open-source contributors

---

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/task-manager-devops/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/task-manager-devops/discussions)
- **Email**: your.email@example.com

---

**Built with ❤️ for the DevOps Community**

**Made by**: [Your Name]  
**Last Updated**: October 2025

---

## 📈 Project Roadmap

- [x] Complete Flask REST API
- [x] Docker containerization
- [x] Kubernetes manifests
- [x] Terraform AWS infrastructure
- [x] Jenkins CI/CD pipeline
- [x] GitHub Actions workflow
- [x] Prometheus monitoring
- [x] Grafana dashboards
- [ ] Helm charts
- [ ] ELK Stack logging
- [ ] Service mesh (Istio)
- [ ] GitOps with ArgoCD
- [ ] Multi-cloud support

---

## 🎓 Learning Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Terraform Tutorials](https://learn.hashicorp.com/terraform)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Prometheus Docs](https://prometheus.io/docs/)
- [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)

---

**⭐ If you find this project helpful, please give it a star!**