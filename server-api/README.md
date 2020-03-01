## Installation

* Install [Python 3.8](https://www.python.org/downloads/)
* Install [pip (3.8)]() if not available
* Install [venv (3.8)]() if not available
* Clone the project
```
git clone ...
```
* Download the datasets
  * for plant type classifier
  * for leave problem detector
* Set up virtual evironment
  * Make sure the current location is `server-api`, if it's the root directory:
  ```
  cd server-api
  ```
  * Create a virtual environment:
  ```
  python3.8 -m venv venv
  ```
  or on Windows
  ```
  python -m venv venv
  ```
  * Activate the virtual environment
  ```
  source venv/bin/activate
  ```
  or on Windows
  ```
  source venv/Scripts/activate
  ```
  * Install necessary packages for Python
  ```
  pip install -r requirements.txt
  ```
