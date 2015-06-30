[![Build Status](https://travis-ci.org/LandRegistry/register-metadata.svg?branch=master)](https://travis-ci.org/LandRegistry/register-metadata)
# Register Metadata

##How to run unit tests in development

```
Vagrant SSH into repo
Type:
source /tmp/.venv/register-metadata/bin/activate

sudo pip install -r requirements_test.txt

Then to run the tests issue this

py.test --cov application tests/ --cov-report=term --cov-report=html

A htmlcov/ folder will be created at the root of project with a code coverage report.
```

##How to run acceptance tests in development

```
Vagrant SSH into repo
navigate to acceptance test folder in cases-api

Then to run the tests enter either

sh run-tests.sh
./run-tests.sh
```
