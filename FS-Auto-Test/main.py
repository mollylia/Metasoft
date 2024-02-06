import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


# Finds and goes to 'Foundation Profile Keyword Search' page
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


# Finds and goes to 'Foundation Search' page
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


# Searches for Foundation Profile Keyword Search and Foundation Search pages
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Finds and goes to 'My Best Prospects' page
def navigateMyBestProspects():
    print("Navigating My Best Prospects page")
    driver.find_element(By.LINK_TEXT, "My Best Prospects").click()


# Creates a new project definition for My Best Prospects
# REQUIRES: 250 <= funding <= 2147483647
def prospectsProjectDefinition(name, funding, province, interest):
    projectName = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtProjectName")
    projectFunding = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtGrantAmount")
    benefitedProvince = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsState_ddlState"))
    givingInterest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_fsTextAutoComplete_txtGIAutocomplete")

    projectName.send_keys(name)
    projectFunding.send_keys(funding)
    benefitedProvince.select_by_visible_text(province)
    givingInterest.send_keys(interest)
    time.sleep(1.5)


# Adds new province to project definition for My Best Prospects
# REQUIRES: a valid prospect definition created with prospectsProjectDefinition
def addProspectsProvince(province):
    benefitedProvince = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsState_ddlState"))
    benefitedProvince.select_by_visible_text(province)
    time.sleep(1.5)


# Adds new giving interest to project definition for My Best Prospects
# REQUIRES: a valid prospect definition created with prospectsProjectDefinition
def addProspectsInterest(interest):
    givingInterest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_fsTextAutoComplete_txtGIAutocomplete")
    givingInterest.clear()
    givingInterest.send_keys(interest)
    givingInterest.send_keys(Keys.TAB)
    time.sleep(1.5)


# Searches for My Prospects
def searchProspects():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.CLASS_NAME, "flex-item7").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fsModalPopupBd")))
    driver.find_element(By.CLASS_NAME, "fsModalPopupBd").click()


# Opens the narrative page of a prospect from the results of searchProspects()
def prospectsOpenNarrativePage(prospect):
    targetProspect = driver.find_element(By.LINK_TEXT, prospect)
    parentElement = targetProspect.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
    scoreElement = parentElement.find_element(By.XPATH, "following-sibling::*[2]")
    scoreElement.find_element(By.TAG_NAME, "span").click()


# Finds giving interest number on narrative page
def prospectFindInterestNumber(prospect):
    # finds and opens narrative page for prospect
    mainWindowHandler = driver.current_window_handle
    targetProspect = driver.find_element(By.LINK_TEXT, prospect)
    parentElement = targetProspect.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
    scoreElement = parentElement.find_element(By.XPATH, "following-sibling::*[2]")
    scoreElement.find_element(By.TAG_NAME, "span").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # loop until new window handle is found
    for window_handle in driver.window_handles:
        if mainWindowHandler != window_handle:
            driver.switch_to.window(window_handle)
            break

    # locates giving and return giving interest score
    givingInterests = driver.find_element(By.XPATH, "//div[b[text()='Giving Interests']]")
    interestScore = givingInterests.text.splitlines()[1][7:]

    driver.close()
    driver.switch_to.window(mainWindowHandler)

    return interestScore


# Finds and goes to 'Power Search' page
def navigatePowerSearch():
    print("Navigating Power Search page")
    driver.find_element(By.LINK_TEXT, "POWER SEARCH").click()


# Sets 'search request' search criteria for Power Search
def setSearchRequest(keyword):
    searchRequest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_txtRequest")
    searchRequest.send_keys(keyword)


# Selects all Candian databases
def selectAllCanadianDatabases():
    print("Selecting Canadian databases")
    driver.find_element(By.LINK_TEXT, "Canada:").click()


# Selects all American databases
def selectAllAmericanDatabases():
    print("Selecting American databases")
    driver.find_element(By.LINK_TEXT, "US:").click()


# Selects all UK databases
def selectAllUKDatabases():
    print("Selecting UK databases")
    driver.find_element(By.LINK_TEXT, "The UK:").click()


# Selects all Australian databases
def selectAllAustralianDatabases():
    print("Selecting Australian databases")
    driver.find_element(By.LINK_TEXT, "Australia:").click()


# Selects specified Canadian database
def selectCanDatabase(database):
    id = ""

    if (database == "Foundation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCFPKS"
    elif (database == "Foundation Grants"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCGrants"
    elif (database == "Foundation Director Biographies"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCFoundationBio"
    elif (database == "News"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCNews"
    elif (database == "Corporation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCCorp"
    elif (database == "Corporate Director Biographies"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCCorpBio"
    elif (database == "Government Programs"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCGov"
    else:
        sys.exit("Please select a valid Canadian database")

    driver.find_element(By.ID, id).click()


# Selects specified American database
def selectUsaDatabase(database):
    id = ""

    if (database == "Foundation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkFPKS"
    elif (database == "Foundation Grants"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkGrants"
    elif (database == "Foundation Director Biographies"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkFoundationBio"
    elif (database == "Charity Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCharityProfiles"
    elif (database == "News"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkNews"
    elif (database == "Charity News"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCharityNews"
    elif (database == "990PFs"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chk990PF"
    elif (database == "Corporation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCorp"
    elif (database == "Corporate Director Biographies"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCorpBio"
    elif (database == "Government Programs"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkGov"
    else:
        sys.exit("Please select a valid American database")

    driver.find_element(By.ID, id).click()


# Selects specified UK database
def selectUkDatabase(database):
    id = ""

    if (database == "Foundation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkUFPKS"
    elif (database == "News"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkUNews"
    else:
        sys.exit("Please select a valid UK database")

    driver.find_element(By.ID, id).click()


# Selects specified Australian database
def selectAusDatabase(database):
    id = ""

    if (database == "Foundation Profiles"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkAUFPKS"
    elif (database == "News"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkAUNews"
    else:
        sys.exit("Please select a valid Australian database")

    driver.find_element(By.ID, id).click()


# Selects search features
def selectSearchFeatures(feature):
    id = ""

    if (feature == "Fuzzy search"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkFuzzy"
    elif (feature == "Stemming"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkStemming"
    elif (feature == "Stemming"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkPhonic"
    elif (feature == "Stemming"):
        id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkSynonyms"
    else:
        sys.exit("Please select a valid search feature")

    driver.find_element(By.ID, id).click()


if __name__ == "__main__":
    fsOpen()
    input("Press Enter to close the browser...")
    driver.quit()