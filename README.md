# README #

### What is this repository for? ###

* Refurnish skills on flask REST API (Python), Unittest, CI/CD, Docker

### How do I get set up? ###

* Prerequisites
  * pip3
  * python3

* Set up *[Skip and move to **Docker Support / Direct Run in Docker Container** for run-only]*
  * Clone the repo
```git clone git@github.com:OmorFarukMashuk/python-ci-cd.git```
  * Go to repo dir
```cd python-ci-cd``` 
  * Create python virtual environment named ```penv```(or any other name) 
```python3 -m venv penv```
  * Activate the environment
```source penv/bin/activate```
  * Install project requirements
```pip3 install -r requirements.txt```
  * Setting the path environment variable
```export PYTHONPATH=src```
  * Run app (will be running on ```http://localhost:3000/```)
```python3 src/app.py```
* Testing
  * Run tests
```coverage run --source=src -m pytest -v tests```
  * Get report
```coverage report -m```
  * Exit python virtual environment ```deactivate```
* Docker Set Up (local machine build and run)
  * Install docker engine from https://docs.docker.com/engine/install/ and launch the app.
  * Use ```buildx``` to enable multi platform support ```docker buildx create --use```
  * Build docker image and push to docker hub (required docker hub account)\
    ```docker buildx build --push --platform linux/amd64,linux/arm64 -t <docker_hub_user_name>/<image_file_name>:<tag_name> .```
  * Pull a version (if any) from docker hub ```docker pull <docker_hub_user_name>/<image_file_name>:<tag_name>```
  * Run docker in container \
    ```docker container run -d -p <desired_local_machine_port>:<in_project_exposed_port> <docker_hub_user_name>/<image_file_name>:<tag_name>```
  * List all active docker containers ```docker ps```
  * Start docker container ```docker start <first_3_char_of_container_id> or <container_name>```
  * Start docker container ```docker stop <first_3_char_of_container_id> or <container_name>```
* Docker Support / Direct Run in Docker Container 
  * Install docker engine
  * Get the preferred version from docker hub ```docker pull ofarmash/handsensor-flask:<tag_name>```
  * Run docker in container \
    ```docker container run -d -p <desired_local_machine_port>:<in_project_exposed_port> ofarmash/handsensor-flask:<tag_name>```    
* Continuous Integration (CI)
  * ```workflows/python-app.yml``` - To automatically check build set up and run test cases upon a new ```push```
  * ```workflows/docker-image.yml``` - To automatically build and push docker image to docker hub upon completion of ```python-app.yml``` workflow 
* Continuous Delivery (CD)
  * TBA

### Contribution guidelines ###

* flask-api, unnitest, CI/CD, python

### Who do I talk to? ###

* Repo owner or admin
