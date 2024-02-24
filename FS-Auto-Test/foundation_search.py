from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Foundation Search' page from user dashboard
def navigate():
    print("Navigating Foundation Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Search").click()


# Sets 'foundation name' with words search criteria
def set_foundation_name_with(name):
    print("  Setting foundation name (with words)")
    foundation_name = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtFNameNot")
    foundation_name.send_keys(name)


# Sets 'foundation name' without words search criteria
def set_foundation_name_without(name):
    print("  Setting foundation name (without words)")
    foundation_name = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtFName")
    foundation_name.send_keys(name)


# Sets 'funder designation' search criteria
def set_funder_designation(first, second, third):
    print("  Setting funder designation")
    designation_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstTOGCodeCA"))

    if first:
        designation_selector.deselect_all()                            # deselects the default option
        designation_selector.select_by_visible_text(first)
    if second:
        designation_selector.select_by_visible_text(second)
    if third:
        designation_selector.select_by_visible_text(second)


# Sets 'city' search criteria
# located is one of ["In", "Not In"]
def set_city(located, city):
    print("  Setting city")
    location_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_ddlCitySwitch"))
    city_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtCity")

    location_selector.select_by_visible_text(located)
    city_input.send_keys(city)


# Sets initial 'province' search criteria
def set_province(province):
    print("  Setting province")
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstState"))
    province_selector.deselect_all()                                   # deselects the default option
    province_selector.select_by_visible_text(province)


# Selects additional 'province' search criteria
def add_province(province):
    print("    Selecting an additional province")
    province_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstState"))
    province_selector.select_by_visible_text(province)


# Sets 'postal code' search criteria
def set_postal_code(postal_code):
    print("  Setting postal code")
    code_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtZipCode")
    code_input.send_keys(postal_code)


# Sets 'crn' search criteria
def set_crn(crn):
    print("  Setting CRN")
    crn_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtEIN")
    crn_input.send_keys(crn)


# Sets initial 'assets range' search criteria
def set_assets_range(asset):
    print("  Setting assets range")
    range_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstAssetCode"))
    range_selector.deselect_all()                                      # deselects the default option
    range_selector.select_by_visible_text(asset)


# Selects additional 'assets range' search criteria
def add_assets_range(asset):
    print("    Selecting an additional assets range")
    range_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstAssetCode"))
    range_selector.select_by_visible_text(asset)


# Selects additional 'grants range' search criteria
def set_grant_range(grant):
    print("  Setting grants range")
    grant_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstIncomeCode"))
    grant_selector.deselect_all()                                      # deselects the default option
    grant_selector.select_by_visible_text(grant)


# Selects additional 'grants range' search criteria
def add_grant_range(grant):
    print("    Selecting an additional grants range")
    grant_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstIncomeCode"))
    grant_selector.select_by_visible_text(grant)


# Sets initial 'granting category' search criteria
def set_granting_category(category):
    print("  Setting granting category")
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstGrantCategory"))
    category_selector.deselect_all()                                   # deselects the default option
    category_selector.select_by_visible_text(category)


# Selects additional 'granting category search criteria
def add_granting_category(category):
    print("    Selects an additional granting category")
    category_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstGrantCategory"))
    category_selector.select_by_visible_text(category)


# Sets 'directors' search criteria
def set_directors(directors):
    print("  Setting directors")
    directors_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtDirectorCA")
    directors_input.send_keys(directors)


# Enters given criteria for 'giving interests' search criteria
def set_giving_interest(criteria):
    print("  Setting giving interests")
    giving_interest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_txtGIKeywords")
    giving_interest.send_keys(criteria)


# Sets initial 'geographic scope' search criteria
def set_geographic_scope(scope):
    print("  Setting geographic scope")
    scope_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstAreaOfOperation"))
    scope_selector.deselect_all()                                      # deselects the default option
    scope_selector.select_by_visible_text(scope)


# Selects additional 'geographic scope' search criteria
def add_geographic_scope(scope):
    print("    Adding an additional geographic scope")
    scope_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lstAreaOfOperation"))
    scope_selector.select_by_visible_text(scope)


# Sets 'selection options' search criteria
# type is one of ["All Foundations", "Newly Registered Foundations"]
# foundations_manager, covid_help is one of ["Include", "Exclude", "Include Only"]
def set_selection_options(type, foundations_manager, covid_help):
    print("  Setting selection options")
    type_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_foundationOptions_ddlAllRegNrf"))
    manager_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_ddlFoundationMPM"))
    help_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_ddlCOVID19"))

    type_selector.select_by_visible_text(type)
    manager_selector.select_by_visible_text(foundations_manager)
    help_selector.select_by_visible_text(covid_help)


# Sets 'my tags' search criteria
# inclusion is one of ["Include", "Exclude"]
def set_my_tags(inclusion, tag):
    print("  Setting my tags")
    inclusion_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_ddlMyTag1"))
    tag_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsMyTag_txtMyTag")

    inclusion_selector.select_by_visible_text(inclusion)
    tag_input.send_keys(tag)


# Sets boolean operator for 'my tags' search criteria
def set_my_tags_boolean(operator):
    print("  Setting my tags boolean")
    driver.find_element(By.LINK_TEXT, operator).click()


# Clicks on 'add' for 'my tags' search criteria
def add_my_tags():
    print("  Adding tag")
    driver.find_element(By.LINK_TEXT, "Add").click()


# Sets 'my saved searches' search criteria
def select_saved_search(save):
    print("  Selecting from saved searches")
    save_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBodyHeader_ContentFindFundersBodyHeader_MySearches_ddlMySavedSearch"))
    save_selector.select_by_visible_text(save)


# Sets 'view mode' search criteria
def set_view_mode(view):
    print("  Setting view mode")
    view_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlDisplayMode"))
    view_selector.select_by_visible_text(view)


# Sets 'results per page' search criteria
def results_per_page(number):
    print("  Setting results per page")
    results_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlPageSize"))
    results_selector.select_by_visible_text(number)


# Sets 'sort by' search criteria
def sort_by(sort_property):
    print("  Setting sort by")
    sort_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlViewBy"))
    sort_selector.select_by_visible_text(sort_property)


# Clicks the search button
def search():
    print("  Searching...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Clicks the 'reset' button
def fs_reset():
    print("  Resetting search criteria...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnReset']/span").click()


# Clicks the 'help' button
def fs_help():
    print("  Visiting help...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")

    main_window_handler = driver.current_window_handle
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_fsHelp_lblHelp").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # loop until new window handle is found
    for window_handle in driver.window_handles:
        if main_window_handler != window_handle:
            driver.switch_to.window(window_handle)
            break

    input("    Press ENTER to continue...")
    driver.find_element(By.XPATH, "//*[@id='siteContainerSP']/div[1]/div/a/span[1]")
    driver.close()
    driver.switch_to.window(main_window_handler)


# Returns the number of foundations found from search
def get_number_results():
    print("  Getting number of results")

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
