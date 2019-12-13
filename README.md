# AWS CI/CD Docker

Test repository for CI/CD of docker images on AWS. For more info on the purpose of this repo, visit the [AWS CI/CD CDK](https://github.com/avanderm/aws-cicd-cdk) repo, which is used in conjunction with this repo. The setup of the Docker image is simple and only serves to illustrate how CDK and Docker interact in an AWS CI/CD setup. The [jsonschema](https://pypi.org/project/jsonschema/) is installed and Python code is installed to check some JSON data with a schema.

## Position in CI/CD

The CDK will deploy a simple CI/CD pipeline using this repo as the source action. The Docker image is built and pushed to an ECR repo.
