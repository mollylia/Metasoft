import time

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
def modify_search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.XPATH, "//span[text()='Modify Search']").click()


# Clicks the modify search button
# Leave search_name blank to use default name
def save_to_my_searches(search_name):
    main_window_handler = driver.current_window_handle
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.XPATH, "//span[text()='Save to My Searches']").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # loop until new window handle is found
    for window_handle in driver.window_handles:
        if main_window_handler != window_handle:
            driver.switch_to.window(window_handle)
            break

    # set name for saved search
    if search_name != "":
        name_input = driver.find_element(By.ID, "txtSearchName")
        name_input.clear()
        name_input.send_keys(search_name)

    driver.find_element(By.XPATH, "//span[text()='Save to My Searches']").click()
    driver.switch_to.window(main_window_handler)


# Clicks the help button
def fs_help():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_fsHelp_lblSmallHelp").click()


# Sets the view mode
def view_mode(mode):
    print("  Setting view mode")

    try:
        view_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayMode"))
        view_selector.select_by_visible_text(mode)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        driver.refresh()
        view_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayMode"))
        view_selector.select_by_visible_text(mode)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets dependent variable for map view (second dropdown menu) and chart view (third dropdown menu)
# REQUIRES: map view or chart view to be selected
def mode_set_dependent_variable(display):
    print("  Map/chart: setting dependent variable")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        display_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayField"))
        display_selector.select_by_visible_text(display)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        display_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlDisplayField"))
        display_selector.select_by_visible_text(display)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets grant direction for map view (third dropdown menu)
# REQUIRES: map view to be selected
def map_set_grant_direction(direction):
    print("  Map: setting grant direction")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        direction_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlMapGrantsDirection"))
        direction_selector.select_by_visible_text(direction)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        direction_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlMapGrantsDirection"))
        direction_selector.select_by_visible_text(direction)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets independent variable for chart view (second dropdown menu)
# REQUIRES: chart view to be selected
def chart_set_independent_variable(variable):
    print("  Chart: setting independent variable")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        variable_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartFacet"))
        variable_selector.select_by_visible_text(variable)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        variable_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartFacet"))
        variable_selector.select_by_visible_text(variable)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets chart type for chart view (fourth dropdown menu)
# REQUIRES: chart view to be selected
def chart_type(chart):
    print("  Chart: setting chart type")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        type_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartType_SingleSeries"))
        type_selector.select_by_visible_text(chart)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        type_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlChartType_SingleSeries"))
        type_selector.select_by_visible_text(chart)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets bubble size value for chart view (fifth dropdown menu)
# REQUIRES: chart view to be selected
#           'grant amount / number of grants' selected for dependent variable
def chart_set_bubble(value):
    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        bubble_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlBubbleAxis"))
        bubble_selector.select_by_visible_text(value)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        bubble_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlBubbleAxis"))
        bubble_selector.select_by_visible_text(value)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets group by for summary view (second dropdown menu)
# REQUIRES: summary view to be selected
def summary_group_by(grouping):
    print("  Summary: setting group by")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        grouping_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlSummaryFacet"))
        grouping_selector.select_by_visible_text(grouping)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        grouping_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlSummaryFacet"))
        grouping_selector.select_by_visible_text(grouping)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


# Sets group by for list view (second dropdown menu)
# REQUIRES: list view to be selected
def list_group_by(grouping):
    print("  List: setting group by")

    try:
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  # starts script
        grouping_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlGrantListBy"))
        grouping_selector.select_by_visible_text(grouping)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script
    except:
        print("    Can't find element. Refreshing!")
        driver.refresh()
        grouping_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_ddlGrantListBy"))
        grouping_selector.select_by_visible_text(grouping)
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})   # stops script


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
    element_into_view = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_Panel1")
    driver.execute_script("arguments[0].scrollIntoView();", element_into_view)
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnSearch").click()


# Clicks the reset button at the bottom of page
def fs_reset():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_btnReset").click()


# Returns the number of grants found from search
def get_number_results():
    print("  Getting number of results")
    time.sleep(5)

    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})
        return summary
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})
        return summary
