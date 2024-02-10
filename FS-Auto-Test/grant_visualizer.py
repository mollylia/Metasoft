from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


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


# Sets the view mode
def view_mode(mode):
    view_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayMode"))
    view_selector.select_by_visible_text(mode)


# Sets display field for map view (second dropdown menu)
# REQUIRES: map view to be selected
def map_set_display_field(display):
    try:
        display_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayField"))
        display_selector.select_by_visible_text(display)
    except NoSuchElementException:
        print("Grant Visualizer: map_set_display_field is only available for MAP view")


# Sets grant direction for map view (third dropdown menu)
# REQUIRES: map view to be selected
def map_set_grant_direction(direction):
    try:
        direction_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlMapGrantsDirection"))
        direction_selector.select_by_visible_text(direction)
    except NoSuchElementException:
        print("Grant Visualizer: map_set_grant_direction is only available for MAP view")


# Sets independent variable for chart view (second dropdown menu)
# REQUIRES: chart view to be selected
def chart_set_independent_variable(variable):
    try:
        variable_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartFacet"))
        variable_selector.select_by_visible_text(variable)
    except NoSuchElementException:
        print("Grant Visualizer: chart_set_independent_variable is only available for CHART view")


# Sets dependent variable for chart view (third dropdown menu)
# REQUIRES: chart view to be selected
def chart_set_dependent_variable(variable):
    variable_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayField"))
    variable_selector.select_by_visible_text(variable)


# Sets chart type for chart view (fourth dropdown menu)
def chart_type(type):
    try:
        type_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartType_SingleSeries"))
        type_selector.select_by_visible_text(type)
    except NoSuchElementException:
        print("Grant Visualizer: chart_type is only available for CHART view")


# Sets initial 'from province' search criteria at the bottom of page
def set_from_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateFromCA"))
    province_selector.deselect_all()                                     # deselects the initial 'all provinces' option
    province_selector.select_by_visible_text(province)


# Selects additional 'from province' search criteria at the bottom of page
def add_from_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateFromCA"))
    province_selector.select_by_visible_text(province)


# Sets initial 'to province' search criteria at the bottom of page
def set_to_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateToCA"))
    province_selector.deselect_all()                                     # deselects the initial 'all provinces' option
    province_selector.select_by_visible_text(province)


# Selects additional 'to province' search criteria at the bottom of page
def add_to_province(province):
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstStateToCA"))
    province_selector.select_by_visible_text(province)


# Sets initial 'granting year' search criteria at the bottom of page
def set_year(year):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstYear")))
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstYear"))
    year_selector.deselect_all()                                         # deselects the initial 'all years' option
    year_selector.select_by_visible_text(year)


# Selects additional 'granting year' search criteria at the bottom of page
def add_year(year):
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstYear"))
    year_selector.select_by_visible_text(year)


# Sets initial 'granting category' search criteria at the bottom of page
def set_category(category):
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstCategory"))
    category_selector.deselect_all()                                     # deselects the initial 'all categories' option
    category_selector.select_by_visible_text(category)


# Selects additional 'granting category' search criteria at the bottom of page
def add_category(category):
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstCategory"))
    category_selector.select_by_visible_text(category)


# Sets initial 'grant size' search criteria at the bottom of page
def set_size(size):
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstRangeCA"))
    size_selector.deselect_all()                                         # deselects the initial 'all grant sizes' option
    size_selector.select_by_visible_text(size)


# Selects additional 'grant size' search criteria at the bottom of page
def add_size(size):
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstRangeCA"))
    size_selector.select_by_visible_text(size)


# Sets 'funder designation' search criteria at the bottom of page
def set_funder_designation(first, second, third):
    designation_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lstFunderDesignation"))

    if first:
        designation_selector.deselect_all()                              # deselects the initial 'all foundations' option
        designation_selector.select_by_visible_text(first)
    if second:
        designation_selector.select_by_visible_text(second)
    if third:
        designation_selector.select_by_visible_text(second)


# Clicks the search button at the bottom of page
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnSearch").click()


# Clicks the reset button at the bottom of page
def fs_reset():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnReset").click()


# Returns the number of grants found from search
def get_number_results():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        return summary
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        return summary
