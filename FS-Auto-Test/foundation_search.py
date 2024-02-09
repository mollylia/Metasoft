from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Foundation Search' page from user dashboard
def navigate():
    print("Navigating Foundation Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Search").click()


# Sets 'foundation name' search criteria
def set_foundation_name(name):
    foundation_name = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtFName")
    foundation_name.send_keys(name)


# Sets 'funder designation' search criteria
def set_funder_designation(first, second, third):
    designation_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstTOGCodeCA"))

    if first:
        designation_selector.deselect_all()                            # deselects the initial 'all foundations' option
        designation_selector.select_by_visible_text(first)
    if second:
        designation_selector.select_by_visible_text(second)
    if third:
        designation_selector.select_by_visible_text(second)


# Sets 'category' search criteria for giving interests
def set_giving_category(category):
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_ddlCategory"))
    category_selector.select_by_visible_text(category)


# Adds 'giving interests' search criteria for giving interests
# REQUIRES: the appropriate giving interest 'category' to already be selected
def add_foundation_giving_interest(interest):
    giving_interest = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_ddlGivingInterest"))
    giving_interest.select_by_value(interest)


# Enters given criteria for 'giving interests' search criteria for Foundation Search
# REQUIRES: keywords are entered with double quotation marks (e.g., "School")
#           multiple keywords are separated with AND or OR (e.g., "School" OR "House")
def set_giving_interest(criteria):
    giving_interest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_txtGIKeywords")
    giving_interest.send_keys(criteria)


# Sets 'sort by' search criteria for Foundation Search
def sort_by(sort_property):
    sort_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlViewBy"))
    sort_selector.select_by_visible_text(sort_property)


# Clicks the search button
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Returns the number of foundations found from search
def get_number_results():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber").text
        return summary
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblTotalNumber").text
        return summary
