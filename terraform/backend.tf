terraform {
  backend "s3" {
    bucket         = "healthcare-platform-terraform-state"
    key            = "applications/${var.application_name}/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
