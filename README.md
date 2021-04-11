# S3 Cross  Region Replication 

This project is under active development. The main aim of this project is to implement the s3 cross region replication

### Prerequisties ##

- **Cloud:** In the project is mainly for on `aws` cloud and the services which used for this cross region replication are `s3`, `kms`, `Iam`. 

- **IaaC:** Terraform is used for provising the infratsructure. You can use the terraform tools from [.devcontainer](./.devcontainer/devcontainer.json) 

- **Development Enviorment:** Vscode dev container. For the installtion of [`Remote - Containers`](https://code.visualstudio.com/docs/remote/containers-tutorial) extension for your Visual Studio Code, Please refer the link

- **CI/CD:** [workflow](./.circleci/config.yml) for the Terraform is mantaining in the circleci 
- **Scripting language** Python is used for uploading the files to the s3 bucket

### Steps to follow to provision the infrastructure:

1. Clone the project in your workspace 

```
git clone https://github.com/Venkateshg07/s3crossreplication.git
```
2. Select the reopen in the container option from the remote comand pallete in the vscode  [Refer](https://www.youtube.com/watch?v=mi8kpAgHYFo) 

3. Build the docker images with the help of Remote-Container Extension(https://code.visualstudio.com/docs/remote/containers-tutorial) and deploy Containers to get access to the development env

4. you have all the necessary tools in this dev container to start the contribution and test the scripts. All the necessary tools for the development are adding in the dockerfile.You can extend the deve env by adding more toold to the [Dockerfile](./.devcontainer/Dockerfile)

5. Export the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in the dev container to start using the terraform scripts. Note: You need create these two env variables in the circleci with the help of project setting to start using the CI/CD workflow 

6. Now you can plan and apply the terraform

7. Run the python script under `hack` directory to upload the sample files to the S3 buckets

```
$python s3upload.py
```

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