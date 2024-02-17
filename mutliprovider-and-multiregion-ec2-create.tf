provider "aws" {
    alias = "nv"
    region = "us-east-1"
}
provider "aws" {
    alias = "ohio"
    region = "us-east-2"
}

resource "aws_instance" "in1" {
    ami = "ami-06aa3f7caf3a30282"
    instance_type = "t2.micro"
    key_name = "terraform-aws-key"
    provider = "aws.nv"
}

resource "aws_instance" "in2" {
    ami = "ami-07b36ea9852e986ad"
    instance_type = "t2.micro"
    key_name = "terraform-key-ohio"
    provider = "aws.ohio"
}