# S3 Cross  Region Replication 

This project is under active development. The main aim of this project is to implement the s3 cross region replication

## Prerequisties ##

- **Cloud:** In the project is mainly for on `aws` cloud and the services which used for this cross region replication are `s3`, `kms`, `Iam`. 

- **IaaC:** Terraform is used for provising the infratsructure. You can use the terraform tools from [.devcontainer](./.devcontainer/devcontainer.json) 

- **Development Enviorment:** Vscode dev container. For the installtion of [`Remote - Containers`](https://code.visualstudio.com/docs/remote/containers-tutorial) extension for your Visual Studio Code, Please refer the link

- **CI/CD:** [workflow](./.circleci/config.yml) for the Terraform is mantaining in the circleci 
- **Scripting language** Python is used for uploading the files to the s3 bucket

## Steps to follow to provision the infrastructure:


### Reference
- [aws_s3_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) is used for managing S3

- [Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) for generating the policy used by the S3 buckets 
- [Cross Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Dev container](https://code.visualstudio.com/docs/remote/containers-tutorial) for setting up the development env
- [Circleci](https://circleci.com/docs/2.0/hello-world/?section=getting-started) for CI/CD workflow

### Future Enhancement:

- Changing the buckets creation using custom module
- Getting the bucket  name and kms key details form the terraform state 
- Storing the state file in the S3
- Extend the logic to make more generic  