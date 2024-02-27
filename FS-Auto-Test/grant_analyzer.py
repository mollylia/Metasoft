from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Grant Analyzer' page from user dashboard
def navigate():
    print("Navigating Grant Analyzer page")
    driver.find_element(By.LINK_TEXT, "Grant Analyzer").click()


# Sets initial 'granting category' search criteria
def set_category(category):
    print("  Setting category")
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstCategory"))
    category_selector.deselect_all()                                   # deselects the initial 'all categories' option
    category_selector.select_by_visible_text(category)


# Selects additional 'granting category' search criteria
def add_category(category):
    print("    Adding an additional category")
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstCategory"))
    category_selector.select_by_visible_text(category)


# Sets initial 'granting year' search criteria
def set_year(year):
    print("  Setting year")
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstYear"))
    year_selector.deselect_all()                                       # deselects the initial 'all years' option
    year_selector.select_by_visible_text(year)


# Selects additional 'granting year' search criteria
def add_year(year):
    print("    Adding an additional year")
    year_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstYear"))
    year_selector.select_by_visible_text(year)


# Sets initial 'granting size' search criteria
def set_size(size):
    print("  Setting size")
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstRangeCA"))
    size_selector.deselect_all()                                       # deselects the initial 'all grant sizes' option
    size_selector.select_by_visible_text(size)


# Selects additional 'granting size' search criteria
def add_size(size):
    print("  Adding an additional size")
    size_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstRangeCA"))
    size_selector.select_by_visible_text(size)


# Sets 'granting foundation' with words search criteria
def set_granting_name_with(keyword):
    print("  Setting granting foundation name (with)")
    foundation_name = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtGFoundation")
    foundation_name.send_keys(keyword)


# Sets 'granting foundation' without words search criteria
def set_granting_name_without(keyword):
    print("  Setting granting foundation name (without)")
    foundation_name = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtGFoundationNot")
    foundation_name.send_keys(keyword)


# Sets 'funder designation' search criteria
def set_funder_designation(first, second, third):
    print("  Setting funder designation")
    designation_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstFunderDesignation"))

    if first:
        designation_selector.deselect_all()                            # deselects the initial 'all foundations' option
        designation_selector.select_by_visible_text(first)
    if second:
        designation_selector.select_by_visible_text(second)
    if third:
        designation_selector.select_by_visible_text(second)


# Sets 'granting foundation CRN' search criteria
def set_granting_crn(crn):
    print("  Setting granting foundation CRN")
    foundation_crn = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtEINCA")
    foundation_crn.send_keys(crn)


# Sets initial 'granting province' search criteria
def set_granting_province(located, province):
    print("  Setting granting province")
    location_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_ddlStateFromSwitch"))
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstStateFromCA"))
    province_selector.deselect_all()                                   # deselects the initial 'all provinces' option

    location_selector.select_by_visible_text(located)
    province_selector.select_by_visible_text(province)


# Selects additional province for 'granting province' search criteria
def add_granting_province(province):
    print("    Adding an additional granting province")
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstStateFromCA"))
    province_selector.select_by_visible_text(province)


# Sets 'granting city' search criteria
def set_granting_city(located, city):
    print("  Setting granting city")
    location_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_ddlGCitySwitch"))
    granting_city = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtGCity")

    location_selector.select_by_visible_text(located)
    granting_city.send_keys(city)


# Sets 'recipient CRN' search criteria
def set_recipient_crn(crn):
    print("  Setting recipient CRN")
    recipient_crn = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtRecEINCA")
    recipient_crn.send_keys(crn)


# Sets 'recipient name' with search criteria
def set_recipient_name_with(keyword):
    print("  Setting recipient foundation name (with)")
    recipient_name = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtRName")
    recipient_name.send_keys(keyword)


# Sets 'recipient name' without search criteria
def set_recipient_name_without(keyword):
    print("  Setting recipient foundation name (without)")
    recipient_name = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtRNameNot")
    recipient_name.send_keys(keyword)


# Sets initial 'recipient province' search criteria
def set_recipient_province(located, province):
    print("  Setting recipient province")
    location_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_ddlStateToSwitch"))
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstStateToCA"))
    province_selector.deselect_all()                                   # deselects the initial 'all provinces' option

    location_selector.select_by_visible_text(located)
    province_selector.select_by_visible_text(province)


# Selects additional province for 'recipient province' search criteria
def add_recipient_province(province):
    print("    Adding an additional recipient province")
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_lstStateToCA"))
    province_selector.select_by_visible_text(province)


# Sets 'recipient city' search criteria
def set_recipient_city(located, city):
    print("  Setting recipient city")
    location_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_ddlRCitySwitch"))
    recipient_city = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_txtRCity")

    location_selector.select_by_visible_text(located)
    recipient_city.send_keys(city)


# Sets 'my tag' search criteria
def set_my_tags(inclusion, tag):
    print("  Setting my tags")
    inclusion_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_ddlMyTag1"))
    input_tag = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder1_fsMyTag_txtMyTag")

    inclusion_selector.select_by_visible_text(inclusion)
    input_tag.send_keys(tag)


# Sets boolean operator for 'my tags' search criteria
def set_my_tags_boolean(operator):
    print("  Setting my tags boolean")
    driver.find_element(By.LINK_TEXT, operator).click()


# Clicks on 'add' for 'my tags' search criteria
def add_my_tags():
    print("  Adding tag")
    driver.find_element(By.LINK_TEXT, "Add").click()


# Clicks on 'my saved searches'
def view_saved_searches():
    print("  Viewing all saved searches")
    saved_searches = driver.find_element(By.LINK_TEXT, "My Saved Searches")
    saved_searches.find_element("..").click()


# Sets 'saved search' search criteria
def select_saved_search(saved_search):
    print("  Selecting from saved searches")
    search_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentHeaderHolder_ddlMySavedSearch"))
    search_selector.select_by_visible_text(saved_search)


# Sets 'view mode' search criteria
def view_mode(view):
    print("  Setting view mode")
    view_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_ddlDisplayMode"))
    view_selector.select_by_visible_text(view)


# Sets 'grouping' search criteria
def group_by(grouping):
    print("  Setting group by")
    grouping_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_ddlGrantListBy"))
    grouping_selector.select_by_visible_text(grouping)


# Sets 'results per page' search criteria
def results_per_page(number):
    print("  Setting results per page")
    results_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_ddlPageSize"))
    results_selector.select_by_visible_text(number)


# Sets 'sort by' search criteria
def sort_by(sort):
    print("  Setting sort by")
    sort_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_ddlViewBy"))
    sort_selector.select_by_visible_text(sort)


# Clicks the search button
def search():
    print("  Searching...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_btnSearch").click()


# Clicks the reset button
def fs_reset():
    print("  Resetting search criteria...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_btnReset").click()


# Clicks the help button
def fs_help():
    print("  Visiting help...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder2_fsHelp_pnlHelp").click()


# Returns the number of grants found from search
def get_number_results():
    print("  Getting number of results")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        return int(summary.replace(",", ""))
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_lblTotalGrants").text
        return int(summary.replace(",", ""))
