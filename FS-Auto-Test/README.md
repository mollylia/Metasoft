# FoundationSearch Auto Test
## How to deploy
### Prerequisites
1. Install python
    * Visit the official [Python website](https://www.python.org) to download Python.
    * Ensure to check the option that says "Add Python to PATH" during installation.
    * Verify the installation by opening command prompt or terminal and typing ```python --version``` or ```python3 --version```.
    * Verify **pip** is installed by typing ```pip --version``` or ```pip3 --version``` in the command prompt or terminal.

 2. Install Selenium
    * Open terminal in the project's root directory.
    * Install Selenium with ```pip install selenium``` or ```pip3 install selenium```.

### Deployment steps
1. Set username and password
    * Set your FoundationSearch username and password by updating the ```fs_username``` and ```fs_password``` variables.

2. Run the script
    * Execute the script by running the Python file containing the provided code.
    * This can be done in terminal or a preferred IDE.

### Troubleshooting
You may encounter the error ```ModuleNotFoundError: No module named 'selenium'``` for multiple reasons:
1. Not having selenium package installed by running ```pip install selenium``` or ```pip3 install selenium```.
2. Having an outdated version of **pip**.
3. Installing the selenium package in a different Python version than the one you are using.
4. Installing the selenium package globally and not in your virtual environment.
5. Running an incorrect version of Python in your IDE.