from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Grant Analyzer' page from user dashboard
def navigate():
    print("Navigating Grant Visualizer page")
    driver.find_element(By.LINK_TEXT, "Grant Visualizer").click()


# Clicks the modify search button
# TODO: element not interactable
def modify_search():
    print("Clicking the modify search button")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    modify_search_button = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnUpdateSearch")


# Clicks the modify search button
# TODO: element not interactable
def save_to_my_searches():
    print("Clicking the save to my searches button")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    save_button = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnSaveSearch")


# Clicks the help button
def fs_help():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_fsHelp_lblSmallHelp").click()


# Sets initial 'from province' search criteria
def set_from_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateFromCA"))
    province_selector.deselect_all()                                     # deselects the initial 'all provinces' option
    province_selector.select_by_visible_text(province)


# Selects additional 'from province' search criteria
def add_from_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateFromCA"))
    province_selector.select_by_visible_text(province)


# Sets initial 'to province' search criteria
def set_to_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateToCA"))
    province_selector.deselect_all()                                     # deselects the initial 'all provinces' option
    province_selector.select_by_visible_text(province)


# Selects additional 'to province' search criteria
def add_to_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateToCA"))
    province_selector.select_by_visible_text(province)


# Sets initial 'granting year' search criteria
def set_year(year):
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstYear"))
    year_selector.deselect_all()                                         # deselects the initial 'all years' option
    year_selector.select_by_visible_text(year)


# Selects additional 'granting year' search criteria
def add_year(year):
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstYear"))
    year_selector.select_by_visible_text(year)


# Sets initial 'granting category' search criteria
def set_category(category):
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstCategory"))
    category_selector.deselect_all()                                     # deselects the initial 'all categories' option
    category_selector.select_by_visible_text(category)


# Selects additional 'granting category' search criteria
def add_category(category):
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstCategory"))
    category_selector.select_by_visible_text(category)


# Sets initial 'grant size' search criteria
def set_size(size):
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstRangeCA"))
    size_selector.deselect_all()                                         # deselects the initial 'all grant sizes' option
    size_selector.select_by_visible_text(size)


# Selects additional 'grant size' search criteria
def add_size(size):
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstRangeCA"))
    size_selector.select_by_visible_text(size)


# Sets 'funder designation' search criteria
def set_funder_designation(first, second, third):
    designation_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstFunderDesignation"))

    if first:
        designation_selector.deselect_all()                              # deselects the initial 'all foundations' option
        designation_selector.select_by_visible_text(first)
    if second:
        designation_selector.select_by_visible_text(second)
    if third:
        designation_selector.select_by_visible_text(second)


# Clicks the search button
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnSearch").click()


# Clicks the reset button
def fs_reset():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnReset").click()
