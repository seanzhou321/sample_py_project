# Sample Python Project 
- To show the project structure
- To show how the packages can be referred with each other
- To run tests

## Setup and Test
### Step 1: Create virtual environment
```$ sample_project> python -m venv venv```
This creates sample_project/venv which holds a python virtual enviornment
- To activate this enviornment
```$ sample_project> venv/Script/activate```
The command prompt should be
```(venv) $ sample_project>```
- To deactivate
```(venv) $ sample_project>deactivate```

### Step 2: Install setup.py to the virtual environment
```(venv) $ sample_project> pip install -e .```
Changes will automatically reflected in the installed package in the virtual environment. 

### Step 3: Install requirements
- install from requirements.txt
```(venv) $ sample_project> pip install -r requirements.txt```
- breaking down the requirements for different stages, such as dev, test, prod etc.
file structure
```
requirements/
├── base.txt        # Core dependencies
├── dev.txt         # Development tools
├── test.txt        # Testing dependencies
└── prod.txt        # Production-specific dependencies
```
For development requirements
```
# requirements/dev.txt
-r base.txt         # Include base requirements
pytest==7.4.3
pylint==3.0.2
```

### Step 4: Test the project
```(venv) $ sample_project> python repl-script.py```
returns
```{'username': 'alice', 'email': 'alice@example.com', 'status': 'active'}```

### Step 5. Run tests in tes_user_service.py
- Single test
```(venv) $ sample_project> pytest tests/test_user_service.py -v```
- or to run all tests
```(venv) $ sample_project> pytest```
- run coverage reporting
```(venv) $ sample_project> pytest --cov=sample_project tests/```
- get detailed test output and print statements
```(venv) $ sample_project> pytest -v -s tests/test_user_service.py```
- run tests matching a pattern
```(venv) $ sample_project> pytest -v -k "email"```
- Run test automatically when files change
```(venv) $ sample_project> ptw```
- Generate a coverage report
```(venv) $ sample_project> pytest --cov=sample_project --cov-report=html tests/```

## Project structure
### 1. __init__.py files enable python package imports. Check the files for details. 
### 2. src/ layout prevents import conflicts

## Testing Package Resources
- Build your package
```python setup.py sdist bdist_wheel```

- Install in development mode
```pip install -e .```

- List included files
```python setup.py sdist --manifest-only```