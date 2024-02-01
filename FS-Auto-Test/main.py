from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
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


# Returns the number of documents found from Foundation Profile Keyword Search visualizer
def profileSearchNumResults():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return summary[19:]
    except Exception as e:
        print(f"An errror has occured: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return summary[19:]


# Finds and goes to 'Foundation Search' tab
def navigateFoundationSearch():
    print("Navigating Foundation Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Search").click()


# Sets 'foundation name' search criteria for Foundation Search
def setFoundationFoundationName(foundationName):
    foundationInput = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtFName")
    foundationInput.send_keys(foundationName)


# Sets 'funder designation' search criteria for Foundation Search
def setFoundationFunderDesignationOne(designation1):
    designationSelector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstTOGCodeCA"))
    designationSelector.deselect_all()                             # deselects the inital 'all foundations' option
    designationSelector.select_by_visible_text(designation1)


# Sets 'funder designation' search criteria for Foundation Search
def setFoundationFunderDesignationTwo(designation1, designation2):
    designationSelector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstTOGCodeCA"))
    designationSelector.deselect_all()                             # deselects the inital 'all foundations' option

    designationSelector.select_by_visible_text(designation1)
    designationSelector.select_by_visible_text(designation2)


# Sets 'funder designation' search criteria for Foundation Search
def setFoundationFunderDesignationThree(designation1, designation2, designation3):
    designationSelector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstTOGCodeCA"))
    designationSelector.deselect_all()                             # deselects the inital 'all foundations' option

    designationSelector.select_by_visible_text(designation1)
    designationSelector.select_by_visible_text(designation2)
    designationSelector.select_by_visible_text(designation3)


# Sets 'category' search criteria for Foundation Search's 'giving interests'
def setFoundationGivingCategory(category):
    categorySelector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_ddlCategory"))
    categorySelector.select_by_visible_text(category)


# Adds 'giving interests' search criteria for Foundation Search's 'giving interests'
# REQUIRES: the appropriate giving interest 'category' to already be selected
def addFoundationGivingInterest(interest):
    givingInterest = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_ddlGivingInterest"))
    givingInterest.select_by_value(interest)


# Enters given criteria for 'giving interests' search criteria for Foundation Search
# REQUIRES: keywords are entered with double quotation marks (e.g., "School")
#           multiple keywords are separated with AND or OR (e.g., "School" OR "House")
def enterFoundationGivingInterest(criteria):
    givingInterest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_txtGIKeywords")
    givingInterest.send_keys(criteria)


# Sets 'sort by' search criteria for Foundation Search
def setFoundationSortBy(property):
    sortSelector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlViewBy"))
    sortSelector.select_by_visible_text(property)


# Returns the number of foundations found from Foundation Search visualizer
def foundationSearchNumResults():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber").text
        return summary
    except Exception as e:
        print(f"An errror has occured: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber").text
        return summary


# Searches
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()



if __name__ == "__main__":
    fsOpen()
    input("Press Enter to close the browser...")
    driver.quit()