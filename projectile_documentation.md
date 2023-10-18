# GITHUB ACTIONS:
**GitHub Actions is used to automate many different tasks in your software development workflow. One way to use GitHub Actions is to run Pytest and Pylint on your code.**

## Unittesting using Pytest:
pytest is a unit testing Python framework. It helps ensure that your code is working as expected and show the time it took to run successfully. 

## Pylinting:
it is a linter for Python code. It checks the code for errors or enhancements.

**To use GitHub Actions to run Pytest and Pylint, we will workflow file in your repository that defines the steps that you want to run.** 
## workflow file:
we have created two yml files:
1- unittesting:
we used pytest action for unit testing. 
```yaml
name: Projectile motion with air resistance unit test
 #the workfolw action will run if any push was done to the main repository
on:
  push:
    branches: 
      - main  # Branch to trigger the workflow on
# use the latest ubuntu Operating system to run the workflow action
jobs:
  test:
    runs-on: ubuntu-latest

# checks out the code from the repository to the runner machine.
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
#set up a Python 3.11 environment on the runner machine
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11  #Python version

#install the dependencies for the project using 'pip install' to install dependencies we need from "requirements.txt" file
    - name: Install dependencies
      run: |
        pip install -r requirements.txt  

#run the unit tests for the project using pytest and save the output as a log file named "pytest_projectile.log"
    - name: Run unit tests and save output as log file
      run: pytest projectile_unit_test.py > pytest_projectile.log

#This step lists the contents of the current directory. This is just for debugging purposes.
    - name: list directory
      run: ls -al

#uploads the log file "pytest_projectile.log" to the GitHub artifact repository.
    - name: Upload log file
      uses: actions/upload-artifact@v2
      with:
        name: pytest_output
        path: pytest_projectile.log
```


2- Pylint.yml file to lint the code for errors
**This YAML file defines a GitHub Actions workflow that runs Pylint on all Python files in the repository. The workflow is triggered whenever a push is made to the repository.**

```yaml

name: Pylint

#the workfolw action will run if any push was done anywhere in the directory
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}

#This step installs the dependencies for the project, including Pylint.
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint

#This step runs Pylint on all Python files in the repository. The output of Pylint is logged to the console.
    - name: Analysing the code with pylint
      run: |
        pylint $(git ls-files '*.py')

```
## Projectile Motion Unittest:
``` python
import math
import unittest

# Import the function you want to test
from projectile_new import calc_xy

#add a class including 2 functions to test
class TestProjectileMotion(unittest.TestCase):
    def test_calc_xy(self):
        # Test the calc_xy function with specific inputs and expected outputs
        angles = [int(math.radians(30)), int(math.radians(45))]
        x_list, y_list = calc_xy(angles, [], [], 700, 0, 0)

        # Check if the returned x and y lists have the expected length
        self.assertEqual(len(x_list), len(angles))
        self.assertEqual(len(y_list), len(angles))

        # Check if the calculated values are reasonable (e.g., not empty)
        self.assertTrue(all(x) for x in x_list)
        self.assertTrue(all(y) for y in y_list)

    def test_degrees_to_radians_conversion(self):
        # Test the degrees to radians conversion function
        angle_degrees = [30, 45, 60]
        angle_radians = [math.radians(deg) for deg in angle_degrees]

        self.assertEqual(angle_radians, [math.radians(30), math.radians(45), math.radians(60)])

if __name__ == '__main__':
    unittest.main()
```

# Results:

## For the Pytest we got the result of pytesting as pytest_periodic.log:

**This shows that the unittest code is running properly and the run time for 2 runs is 0.78 s as indicated below in the output log file
```
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: /home/runner/work/23-Homework4G3/23-Homework4G3
collected 2 items

projectile_unit_test.py ..                                               [100%]

============================== 2 passed in 0.78s ===============================

```
## pylint results:

The result of pylint included errors about:
1- bad identation
2- blank or white spaces
3- blank lines
4- missing docstrings
```
************* Module projectile_unit_test
8 projectile_unit_test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
9 projectile_unit_test.py:7:0: C0115: Missing class docstring (missing-class-docstring)
10 projectile_unit_test.py:9:4: C0116: Missing function or method docstring (missing-function-docstring)
11 projectile_unit_test.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
12
13
-----------------------------------
14 Your code has been rated at 7.65/10

```

