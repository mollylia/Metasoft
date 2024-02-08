import sys

from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Power Search' page
def navigate():
    print("Navigating Power Search page")
    driver.find_element(By.LINK_TEXT, "POWER SEARCH").click()


# Sets 'search request' search criteria
def set_search_request(keyword):
    search_request = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_txtRequest")
    search_request.send_keys(keyword)


# Selects all Canadian databases
def select_all_canadian_databases():
    print("Selecting Canadian databases")
    driver.find_element(By.LINK_TEXT, "Canada:").click()


# Selects all American databases
def select_all_american_databases():
    print("Selecting American databases")
    driver.find_element(By.LINK_TEXT, "US:").click()


# Selects all UK databases
def select_all_uk_databases():
    print("Selecting UK databases")
    driver.find_element(By.LINK_TEXT, "The UK:").click()


# Selects all Australian databases
def select_all_australian_databases():
    print("Selecting Australian databases")
    driver.find_element(By.LINK_TEXT, "Australia:").click()


# Selects specified Canadian database
def select_canadian_database(database):
    if database == "Foundation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCFPKS"
    elif database == "Foundation Grants":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCGrants"
    elif database == "Foundation Director Biographies":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCFoundationBio"
    elif database == "News":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCNews"
    elif database == "Corporation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCCorp"
    elif database == "Corporate Director Biographies":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCCorpBio"
    elif database == "Government Programs":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchCA1_chkCGov"
    else:
        sys.exit("Power search: please select a valid Canadian database")

    driver.find_element(By.ID, input_id).click()


# Selects specified American database
def select_american_database(database):
    if database == "Foundation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkFPKS"
    elif database == "Foundation Grants":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkGrants"
    elif database == "Foundation Director Biographies":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkFoundationBio"
    elif database == "Charity Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCharityProfiles"
    elif database == "News":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkNews"
    elif database == "Charity News":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCharityNews"
    elif database == "990PFs":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chk990PF"
    elif database == "Corporation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCorp"
    elif database == "Corporate Director Biographies":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkCorpBio"
    elif database == "Government Programs":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_fsSubGlobalSearchUS1_chkGov"
    else:
        sys.exit("Power search: please select a valid American database")

    driver.find_element(By.ID, input_id).click()


# Selects specified UK database
def select_uk_database(database):
    if database == "Foundation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkUFPKS"
    elif database == "News":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkUNews"
    else:
        sys.exit("Power search: please select a valid UK database")

    driver.find_element(By.ID, input_id).click()


# Selects specified Australian database
def select_australian_database(database):
    if database == "Foundation Profiles":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkAUFPKS"
    elif database == "News":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_chkAUNews"
    else:
        sys.exit("Power search: please select a valid Australian database")

    driver.find_element(By.ID, input_id).click()


# Selects search features
def select_search_features(feature):
    if feature == "Fuzzy search":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkFuzzy"
    elif feature == "Stemming":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkStemming"
    elif feature == "Stemming":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkPhonic"
    elif feature == "Stemming":
        input_id = "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGlobal_SearchType_chkSynonyms"
    else:
        sys.exit("Power search: please select a valid search feature")

    driver.find_element(By.ID, input_id).click()


# Clicks the search button
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Returns the number of documents found from Power Search visualizer
def get_number_results():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return summary[19:]
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return summary[19:]
