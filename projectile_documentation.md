# Github Actions:
**GitHub Actions is used to automate many different tasks in your software development workflow. One way to use GitHub Actions is to run Pytest and Pylint on your code.**

## Unittesting using Pytest:
`pytest` is a unit testing Python framework. It helps ensure that your code is working as expected and show the time it took to run successfully. 

## Pylinting:
It is a linter for Python code. It checks the code for errors or enhancements.

**To use GitHub Actions to run Pytest and Pylint, we will workflow file in your repository that defines the steps that you want to run.** 
## workflow file:
we have created two `yml` files:
1- unittesting:
we used `pytest` action for unit testing. 
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


2- `Pylint.yml` file to lint the code for errors
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
5- long code lines
7- 
```
************* Module projectile_new
57 projectile_new.py:23:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
58 projectile_new.py:24:0: C0303: Trailing whitespace (trailing-whitespace)
59 projectile_new.py:25:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
60 projectile_new.py:26:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
61 projectile_new.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
62 projectile_new.py:28:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
63 projectile_new.py:29:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
64 projectile_new.py:30:0: C0303: Trailing whitespace (trailing-whitespace)
65 projectile_new.py:31:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
66 projectile_new.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
67 projectile_new.py:33:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
68 projectile_new.py:34:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
69 projectile_new.py:35:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
70 projectile_new.py:36:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
71 projectile_new.py:37:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
72 projectile_new.py:38:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
73 projectile_new.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
74 projectile_new.py:41:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
75 projectile_new.py:42:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
76 projectile_new.py:43:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
77 projectile_new.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
78 projectile_new.py:46:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
79 projectile_new.py:47:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
80 projectile_new.py:48:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
81 projectile_new.py:55:0: C0301: Line too long (120/100) (line-too-long)
82 projectile_new.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
83 projectile_new.py:1:0: C0114: Missing module docstring (missing-module-docstring)
84 projectile_new.py:3:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
85 projectile_new.py:6:0: C0103: Constant name "g" doesn't conform to UPPER_CASE naming style (invalid-name)
86 projectile_new.py:7:0: C0103: Constant name "dt" doesn't conform to UPPER_CASE naming style (invalid-name)
87 projectile_new.py:9:0: C0103: Constant name "x_start" doesn't conform to UPPER_CASE naming style (invalid-name)
88 projectile_new.py:10:0: C0103: Constant name "y_start" doesn't conform to UPPER_CASE naming style (invalid-name)
89 projectile_new.py:12:0: C0103: Constant name "const" doesn't conform to UPPER_CASE naming style (invalid-name)
90 projectile_new.py:13:0: C0103: Constant name "v_initial" doesn't conform to UPPER_CASE naming style (invalid-name)
91 projectile_new.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
92 projectile_new.py:22:0: R0913: Too many arguments (6/5) (too-many-arguments)
93 projectile_new.py:22:20: W0621: Redefining name 'x_list' from outer scope (line 19) (redefined-outer-name)
94 projectile_new.py:22:28: W0621: Redefining name 'y_list' from outer scope (line 20) (redefined-outer-name)
95 projectile_new.py:22:48: W0621: Redefining name 'x_start' from outer scope (line 9) (redefined-outer-name)
96 projectile_new.py:22:57: W0621: Redefining name 'y_start' from outer scope (line 10) (redefined-outer-name)
97 projectile_new.py:31:4: W0621: Redefining name 'i' from outer scope (line 54) (redefined-outer-name)
98 projectile_new.py:22:36: W0613: Unused argument 'v_initital' (unused-argument)
99 projectile_new.py:54:0: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
100 projectile_new.py:56:39: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
```

