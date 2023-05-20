# API to Provide patients care record

## v0.0.1
### Flask API 
* Read JSON files from local file system .
* GET the records `/data/<filename>` .
* API exposed at port `localhost:5000` .

## v0.0.2
### Flask API 
* Read JSON files from postgresql database
* GET the records `/data/<filename>` .
* API exposed at port `localhost:5000` .
* In v0.0.2 once both the containers are up and running, run `python load_json_to_postgresql.py` to laod the data to the database.

## v0.0.4
### Flask API 
* Read JSON files from local filessytem
* test case using pytest mocking is added to test /data/<filename>. To run tests run `pytest tests`
* GET the records `/data/<filename>` .
* API exposed at port `localhost:5000` .

### Infrastructure
* Added terraform scripts required to delpoy the backend application to ecs fargate.
* Service is available at `http://test-lb-tf-199678478.us-west-2.elb.amazonaws.com/data/<filename>`
* Example : [Link](http://test-lb-tf-199678478.us-west-2.elb.amazonaws.com/data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json)



## v0.0.5
### Flask API 
* Service is available at `http://test-lb-tf-199678478.us-west-2.elb.amazonaws.com/data/<filename>`
* Example : [Link](http://test-lb-tf-199678478.us-west-2.elb.amazonaws.com/data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json)

# Infra
* CI/CD pipeline is implemented using GIthub actions and terraform
* terraform scrips in `/tf-aws` used to build the infrastructure
* Application is hosted using ECS Fargate.
* GIthub Actions pipeline workflow
    * Git checkout -> test using pytest -> Build docker image -> Push image to ECR -> Deploy with Terraform 
## Docker Compose 
* Run `docker-compose up` .
* API service is exposed at `localhost:5000` .


