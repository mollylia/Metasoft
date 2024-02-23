from web_driver_instance import driver
from selenium.webdriver.common.by import By

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)


# Opens Foundation Search webpage
def fs_open():
    print("Opening Foundation Search")
    driver.get("https://www.foundationsearch.ca")


# Logs in with given username and password
def fs_login(username, password):
    print("  Logging in")
    driver.find_element(By.CLASS_NAME, "header--login").click()

    username_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtUsername")
    password_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtPassword")

    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_btnLogin").click()


# Closes Foundation Search webpage
def fs_close():
    print("Closing Foundation Search")
    driver.close()


if __name__ == "__main__":
    fs_open()
    input("Press Enter to close the browser...")
    fs_close()
