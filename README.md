# Bulgarian Electricity Distributors API / HomeAssistant Integration

A script that parses the website of Bulgarian electricity providers. Currently supporting only Chez, now renamed to Electrohold(.bg).

Fetches current electricity prices and outages for specified client id.

## How to use scripts:

### 1. make sure you have python3 and pip installed

### 2. pip install -r requirements.txt

### 3. Set your client id in run.py

### 4. python3 run.py

## CICD:

### Using GitLab Workflow with feature branch approach

### Create branch based on develop, named based on developed feature, push, create Pull Request

### On PR for verification, the source code is ran with different versions of Python (3.8, 3.9, 3.10) and linted with flake8.

### Develop -> Main branch merges are done when the develop branch is stable and after a version/state tag on the develop branch state.
