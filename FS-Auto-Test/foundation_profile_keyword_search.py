from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Finds and goes to 'Foundation Profile Keyword Search' page from user dashboard
def navigate():
    print("Navigating Profile Keyword Search page")
    driver.find_element(By.LINK_TEXT, "Foundation Profile Keyword Search").click()


# Sets 'foundation name' search criteria
def set_foundation_name(foundation_name):
    print("  Setting foundation name")
    foundation_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtFName")
    foundation_input.send_keys(foundation_name)


# Sets 'grantor city' search criteria
def set_grantor_city(city):
    print("  Setting grantor city")
    city_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtCity")
    city_input.send_keys(city)


# Sets 'grantor province' search criteria
def set_grantor_province(province):
    print("  Setting grantor province")
    province_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtState")
    province_input.send_keys(province)


# Sets 'director/officer' search criteria
def set_director_officer(name):
    print("  Setting director/officer")
    name_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtOfficers")
    name_input.send_keys(name)


# Sets 'keyword search' search criteria
def set_keyword(keyword):
    print("  Setting keyword")
    keyword_input = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_txtKeywordSearch")
    keyword_input.send_keys(keyword)


# Sets 'type of search' search criteria
# Enter empty types as ""
def type_of_search(type_1, type_2, type_3, type_4):
    print("  Setting type of search")

    if "Fuzzy search" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkFuzzy").click()
    if "Stemming" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkStemming").click()
    if "Phonic search" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkPhonic").click()
    if "Thesaurus" in (type_1, type_2, type_3, type_4):
        driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsProfileKeyword_SearchType_chkSynonyms").click()


# Sets 'my saved searches' search criteria
def select_saved_search(save):
    print("  Selecting from saved searches")
    save_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBodyHeader_ContentFindFundersBodyHeader_MySearches_ddlMySavedSearch"))
    save_selector.select_by_visible_text(save)


# Sets 'results per page' search criteria
def results_per_page(number):
    print("  Setting results per page")
    results_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlPageSize"))
    results_selector.select_by_visible_text(number)


# Sets 'sort by' search criteria
def sort_by(sort):
    print("  Setting sort by")
    sort_selector = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_ddlSortBy"))
    sort_selector.select_by_visible_text(sort)


# Clicks the 'search' button
def search():
    print("  Searching...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_btnSearch").click()


# Clicks the 'reset' button
def fs_reset():
    print("  Resetting search criteria...")
    driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_fnContentBody_ContentFindFundersSubBody_pnlFreeTextSearchForm']/div[3]/div[2]/a/span").click()


# Clicks the 'help' button
def fs_help():
    print("  Visiting help...")
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


# Returns the number of documents found from search
def get_number_results():
    print("  Getting number of results")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return int(summary[19:].replace(",", ""))
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Refreshing page...")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary")))
        summary = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_lblSearchSummary").text
        return int(summary[19:].replace(",", ""))


# Clicks the 'modify search' button
def modify_search():
    print("  Modifying search...")
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_fnContentBody_ContentFindFundersBody_btnModifySearch']/span").click()


# Clicks the 'save to my searches' button
# Leave search_name blank to use default name
def save_to_my_searches(search_name):
    print("  Saving search...")
    main_window_handler = driver.current_window_handle
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")

    driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_fnContentBody_ContentFindFundersBody_btnSaveSearch']/span").click()
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


# Clicks the 'export to csv' button
def export_to_csv():
    print("  Exporting to CSV...")
    driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_fnContentBody_ContentFindFundersBody_btnExportExcel']/span").click()
