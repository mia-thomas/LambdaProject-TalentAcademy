terraform {
  backend "s3" {
    bucket = "mia-l-function-s3"
    key    = "sprint1/week2/training-terraform/terraform.tfstates"
  }
}