terraform {
    backend "s3" {
    bucket = "mia-l-function-s3"
    encrypt = true
    key = "state.tfstate"
    region = "eu-west-1"
    profile = "cloudreach-ta-lab" # you have to give the profile name here. not the variable("${var.AWS_PROFILE}")
  }
}