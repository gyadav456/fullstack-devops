variable "aws_region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster"
  default     = "task-manager-cluster"
}

variable "db_name" {
  description = "Database name"
  default     = "taskdb"
}

variable "db_username" {
  description = "Database username"
  default     = "taskuser"
}

variable "db_password" {
  description = "Database password"
  sensitive   = true
}
