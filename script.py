
# Let's create comprehensive project data with all the actual file contents
import json

project_files = {
    "project_name": "task-manager-devops",
    "description": "Complete DevOps CI/CD project with Flask microservices, Terraform, Kubernetes, and monitoring",
    
    "application": {
        "name": "Task Manager API",
        "framework": "Python Flask",
        "database": "PostgreSQL",
        "features": ["RESTful API", "CRUD operations", "Health checks", "Metrics endpoint"]
    },
    
    "infrastructure": {
        "cloud_provider": "AWS",
        "iac_tool": "Terraform",
        "components": ["VPC", "EC2", "RDS", "S3", "Security Groups"]
    },
    
    "cicd": {
        "primary": "Jenkins",
        "secondary": "GitHub Actions",
        "stages": ["Checkout", "Test", "Build", "Security Scan", "Deploy"]
    },
    
    "containerization": {
        "docker": True,
        "docker_compose": True,
        "kubernetes": True,
        "registry": "Docker Hub"
    },
    
    "monitoring": {
        "metrics": "Prometheus",
        "visualization": "Grafana",
        "logging": "ELK Stack (optional) / Loki"
    },
    
    "security": {
        "vulnerability_scan": "Trivy",
        "code_quality": "SonarQube",
        "secrets": "GitHub Secrets / AWS Secrets Manager"
    }
}

# Save to display
print("Project Structure Created:")
print(json.dumps(project_files, indent=2))
