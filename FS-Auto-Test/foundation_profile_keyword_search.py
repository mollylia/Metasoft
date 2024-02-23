from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Foundation Profile Keyword Search' page from user dashboard
def navigate():
    print("Navigating Profile Keyword Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Profile Keyword Search").click()


# Sets 'foundation name' search criteria
def set_foundation_name(foundation_name):
    foundation_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtFName")
    foundation_input.send_keys(foundation_name)


# Sets 'grantor city' search criteria
def set_grantor_city(city):
    city_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtCity")
    city_input.send_keys(city)


# Sets 'grantor province' search criteria
def set_grantor_province(province):
    province_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtState")
    province_input.send_keys(province)


# Sets 'director/officer' search criteria
def set_director_officer(name):
    name_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtOfficers")
    name_input.send_keys(name)


# Sets 'keyword search' search criteria
def set_keyword(keyword):
    keyword_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtKeywordSearch")
    keyword_input.send_keys(keyword)


# Sets 'type of search' search criteria
# Enter empty types as ""
def type_of_search(type_1, type_2, type_3, type_4):
    if "Fuzzy search" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkFuzzy").click()
    if "Stemming" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkStemming").click()
    if "Phonic search" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkPhonic").click()
    if "Thesaurus" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkSynonyms").click()


# Clicks the search button
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Returns the number of documents found from search
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
