from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome()


# Opens Foundation Search webpage
def fsOpen():
    print("Opening Foundation Search")
    driver.get("https://www.foundationsearch.ca")

# Logs in with given username and password
def fsLogin(username, password):
    driver.find_element(By.CLASS_NAME, "header--login").click()

    usernameInput = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtUsername")
    passwordInput = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_txtPassword")

    usernameInput.send_keys(fs_username)
    passwordInput.send_keys(fs_password)
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentBody_btnLogin").click()

# Finds and goes to 'Foundation Profile Keyword Search' tab
def navigateProfileKeywordSearch():
    print("Navigating Profile Keyword Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Profile Keyword Search").click()

# Sets 'keyword search' search criteria for Foundation Profile Keyword Search
def setProfileKeyword(keyword):
    keywordInput = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtKeywordSearch")
    keywordInput.send_keys(keyword)

# Sets 'foundation name' search criteria for Foundation Profile Keyword Search
def setProfileFoundationName(foundationName):
    foundationInput = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtFName")
    foundationInput.send_keys(foundationName)

# Searches
def search():
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()

# Returns the number of results found from Foundation Profile Keyword Search
def keywordSearchNumResults():
    summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
    return int(summary[19:])


if __name__ == "__main__":
    fsOpen()

    input("Press Enter to go to login...")
    fsLogin(fs_username, fs_password)

    input("Press Enter to go to the Profile Keyword Search page...")
    navigateProfileKeywordSearch()

    # input("Press Enter to search by keyword...")
    # setProfileKeyword("gates")
    input("Press Enter to search by foundation name...")
    setProfileFoundationName("ford")

    input("Press Enter to search...")
    search()

    input("Press Enter to close the browser...")
    driver.quit()