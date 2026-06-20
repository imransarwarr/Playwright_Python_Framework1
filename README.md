# End-to-End Testing with Playwright Python 
- **Python 3.13.7 and Pytest

# Introduction 
- The goal of this project is to automate End-to-End testing for the "OrangeHRM" projects. It aims to improve the integration, testing, and maintenance processes. This will lead to smoother workflows and better scalability for all connected systems.
- This project demonstrates End-to-End testing & API testing using **Playwright**, **Python** and **Pytest**. It combines Pytest's test framework with Playwright's browser automation for API testing, providing a comprehensive solution for both backend and frontend testing.
- Playwright automates browser interactions, enabling robust web application testing through scripting. 



## Table of Contents
- Prerequisites
- Installation
- Setup
- Folder Structure
- Test Writing
- Running Tests


## Prerequisites
Before getting started, ensure you have the following installed:

- pycharm IDE (Community Edition)


## Setup
- Clone the repository to your local machine:
   git clone https://github.com/imransarwarr/Playwright_Python_Framework1

# Create and activate a virtual environment (recommended):
python -m venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Playwright & Pytest
- 
- 
# Install the required dependencies:
  
- pip install pytest
- pip install pytest-playwright
- playwright install
- pip install pytest-bdd
- pip install pytest-html
- pip install pytest-bdd-html 
- pip freeze >requirements.txt


## Here are the shortest descriptions for each command's purpose and usage:
- pip install pytest: Installs the pytest testing framework for Python.       
- pip install pytest-playwright: Installs the Playwright plugin for pytest to enable browser automation testing.
- playwright install: Installs necessary browser binaries for Playwright automation.      
- pip install pytest-playwright: Same as above, installs Playwright plugin for pytest.       
- pip install pytest-html: Installs the pytest-html plugin to generate HTML test reports for pytest.
- pip install pytest-bdd-html: Installs HTML reporting for pytest-bdd.       
- pip freeze > requirements.txt: Generates a requirements.txt file containing the current environment's Python package versions.
- pytest --html=report.html: Runs pytest and generates an HTML report (report.html) for the test results.
- Install Allure: pip install allure-pytest
- Run Tests with Allure: pytest --alluredir=allure-results
- Generate Report: allure serve allure-results	       


## Write Your Tests
- In the /tests directory, write test functions using the Pytest framework. Test function names should start with test_ to be recognized by Pytest.

##  Run test on different environment
- Set the environment file you want to use by the command:  $env:ENV_FILE = ".env.stage"
- The run test with the command: pytest 
- This will run the tests by using the environment file we have set

## Running Tests
- Running the Tests: pytest The tests are run using the pytest command:
- pytest tests/ui
- $env:ENV_FILE = "env/OrangeHRM/.env.dev"
- pytest tests/api/orangeHRMapis.py -m orangeHRM_critical_apis


- # Run tests from a single file
python -m pytest -v tests/test_sample.py

# Activate browser's headless mode for CI/CD
python -m pytest --headless -v tests/test_sample.py

# Run all tests with a declared environment
python -m pytest --headless --env stage

# Generate report, and parallelize the flow
- python -m pytest --html=reports/result.html --num processes 4
- Run Tests with Allure: pytest --alluredir=allure-results
- Generate Report: allure serve allure-results	

# Use tag notation (@smoke-test) to limit the scope
python -m pytest --headless --env stage -m smoke-test
pytest --headed tests/e2e/OrangeHRM/test_login_steps.py
pytest Playwright_Core/tests/test_registrationPage.py -headed slo-mo 1000 -s

## Check Test Results
- Pytest will show the test results in your terminal or command prompt. If all tests pass, you'll see an output similar to:
- ============================= test session starts ==============================
     collected 3 items

     test_your_module.py::test_your_function PASSED                           [100%]

 ============================== 3 passed in 0.01 seconds ==============================

- If there are failures, Pytest will provide details about where the tests failed.

##  Create GUI Reporting.
- To add dependency: poetry add --dev pytest-html
- pytest --html=reports/test_report.html
- pytest --html=report.html
- python -m pytest --html=reports/result.html --num processes 4

- Run Tests with Allure: pytest --alluredir=allure-results
- Generate Report: allure serve allure-results	

##  Debug the run test using tracer

- playwright show-trace  trace.zip


## References
- https://playwright.dev/python/docs/intro
- https://playwright.dev/python/docs/api/class-playwright (Official API Reference:)

## Author
-Imran Sarwar 

## Current Designation
- Senior Test Automation Architect

## Company names
- SQA Trainings
- web: https://www.sqatrainings.net/

