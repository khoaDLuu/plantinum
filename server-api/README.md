# Flask server for plantinum

## Installation

### For Linux / Ubuntu

* Install [Python 3.8](https://www.python.org/downloads/)
  ```
  sudo apt update
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  [Enter]
  sudo apt install python3.8
  python3.8 --version
  ```

* Install pip (3.8)
  ```
  sudo apt install python3-pip
  ```

* Install venv (3.8)
  ```
  sudo apt install python3.8-venv
  ```

* Download the datasets
  * for plant type classifier: [plants](https://github.com/khoaDLuu/plantinum/releases/download/v1.0-beta/planttype.model)
  * for leave problem detector: [leaveproblems](https://github.com/khoaDLuu/plantinum/releases/download/v1.0-beta/leaveproblem.model)

* Set up virtual evironment
  * Make sure the current location is `server-api`, if it's the root directory:
    ```
    cd server-api
    ```
  * Create a virtual environment:
    ```
    python3.8 -m venv venv
    ```
  * Activate the virtual environment
    ```
    source venv/bin/activate
    ```

* Install necessary packages for Python
  ```
  pip install -r requirements.txt
  ```

### For Windows

* Install [Python 3.8](https://www.python.org/downloads/)

* Download the datasets
  * for plant type classifier: [plants](https://github.com/khoaDLuu/plantinum/releases/download/v1.0-beta/planttype.model)
  * for leave problem detector: [plantproblems](https://github.com/khoaDLuu/plantinum/releases/download/v1.0-beta/leaveproblem.model)

* Set up virtual evironment
  * Make sure the current location is `server-api`. If it's the root directory:
    ```
    cd server-api
    ```
  * Create a virtual environment:
    ```
    python -m venv venv
    ```
  * Activate the virtual environment
    ```
    source venv/Scripts/activate
    ```

* Install necessary packages for Python
  ```
  pip install -r requirements.txt
  ```

