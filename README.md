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

## Docker Compose 
* Run `docker-compose up` .
* API service is exposed at `localhost:5000` .



Needs to be done:
[ ] Test cases for the API.
[ ] Integrating with CI/CD piplene.
[ ] Deployment to AWS environment.