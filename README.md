# README #

### What is this repository for? ###

* Practice

### How do I get set up? ###

* Prerequisites
** pip3
** python3

* Set up
** Clone the repo
```git clone git@github.com:OmorFarukMashuk/python-ci-cd.git```
** Go to repo dir
```cd python-ci-cd``` 
** Create python virtual environment named ```penv```(or any other name) 
```python3 -m venv penv```
** Activate the environment
```source penv/bin/activate```
** Install project requirements
```pip3 install -r requirements.txt```
** Setting the path environment variable
```export PYTHONPATH=src```
** Run app (will be running on ```http://127.0.0.1:5000```)
```python3 src/app.py```
* Testing
** Run tests
```coverage run -m pytest```
** Get report
```coverage report -m```
** Exit python virtual environment (need to activate and export ```$PYTHONGPATH=src``` again for re-run)
```deactivate```

### Contribution guidelines ###

* flask-api, unnitest, CI, python

### Who do I talk to? ###

* Repo owner or admin