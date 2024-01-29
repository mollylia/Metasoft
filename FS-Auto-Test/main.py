from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome()
driver.get("https://www.foundationsearch.ca")

def fsLogin(username, password):
    driver.find_element(By.CLASS_NAME, "header--login").click()

    input("Press Enter to input username...")
    inputUsername = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtUsername")
    inputUsername.send_keys(fs_username)

    input("Press Enter to input password...")
    inputPassword = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtPassword")
    inputPassword.send_keys(fs_password)

    input("Press Enter to login...")
    loginButton = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_btnLogin")
    loginButton.click()

if __name__ == "__main__":
    print("opening Foundation Search")
    input("Press Enter to go to the login page...")
    fsLogin(fs_username, fs_password)
    input("Press Enter to close the browser...")
    driver.quit()