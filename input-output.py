provider "aws" {
    alias = "nv"
    region = "us-east-1"
}
provider "aws" {
    alias = "ohio"
    region = "us-east-2"
}
variable "ami_1" {
    description = "ec2-1 AMI id"
    type = string
    default = "ami-06aa3f7caf3a30282"
}
variable "ami_2" {
    description = "ec2-1 AMI id"
    type = string
    default = "ami-07b36ea9852e986ad"
}
variable "instance_type" {
    description = "ec2 instance type"
    type = string
    default = "t2.micro"
}
variable "key_1" {
    description = "ec2-1 key"
    type = string
    default = "terraform-aws-key"
}
variable "key_2" {
    description = "ec2-2 key"
    type = string
    default = "terraform-key-ohio"
}
resource "aws_instance" "ec21" {
    ami = var.ami_1
    instance_type = var.instance_type
    key_name = var.key_1
    provider = "aws.nv"
}

resource "aws_instance" "ec22" {
    ami = var.ami_2
    instance_type = var.instance_type
    key_name = var.key_2
    provider = "aws.ohio"
}
output "pub-ip1" {
    description = "Please print the public ip of ec2 instance"
    value = aws_instance.ec21.public_ip
}
output "pub-ip2" {
    description = "Please print the public ip of ec2 instance"
    value = aws_instance.ec22.public_ip
}