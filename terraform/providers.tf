terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-west-1"
  shared_credentials_file = "/Users/mia.thomas/.aws/credentials"
  profile                 = "cloudreach-ta-lab"
}