import time
import main

from web_driver_instance import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Finds and goes to 'My Best Prospects' page
def navigate():
    print("Navigating My Best Prospects page")
    driver.find_element(By.LINK_TEXT, "My Best Prospects").click()


# Creates new project definition
# REQUIRES: 250 <= funding <= 2147483647
def create_project_definition(name, funding, province, interest):
    project_name = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtProjectName")
    project_funding = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_txtGrantAmount")
    benefited_province = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsState_ddlState"))
    giving_interest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_fsTextAutoComplete_txtGIAutocomplete")

    project_name.send_keys(name)
    project_funding.send_keys(funding)
    benefited_province.select_by_visible_text(province)
    giving_interest.send_keys(interest)
    time.sleep(1.5)


# Adds new province to project definition
# REQUIRES: a valid prospect definition already created
def add_province(province):
    benefited_province = Select(driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsState_ddlState"))
    benefited_province.select_by_visible_text(province)
    time.sleep(1.5)


# Adds new giving interest to project definition
# REQUIRES: a valid prospect definition already created
def add_interest(interest):
    giving_interest = driver.find_element(By.ID, "ctl00_ctl00_fnContentBody_ContentFindFundersBody_fsGivingInterest_fsTextAutoComplete_txtGIAutocomplete")
    giving_interest.clear()
    giving_interest.send_keys(interest)
    giving_interest.send_keys(Keys.TAB)
    time.sleep(1.5)


# Clicks the search button
def search():
    driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    driver.find_element(By.CLASS_NAME, "flex-item7").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fsModalPopupBd")))
    driver.find_element(By.CLASS_NAME, "fsModalPopupBd").click()


# Opens narrative page of a prospect from search
def open_narrative_page(prospect):
    target_prospect = driver.find_element(By.LINK_TEXT, prospect)
    prospect_parent = target_prospect.find_element(By.XPATH, "..").find_element(By.XPATH, "..")
    score_element = prospect_parent.find_element(By.XPATH, "following-sibling::*[2]")
    score_element.find_element(By.TAG_NAME, "span").click()


# Finds giving interest number of a prospect from search
def find_interest_number(prospect):
    # finds and opens narrative page for prospect
    main_window_handler = driver.current_window_handle
    open_narrative_page(prospect)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # loop until new window handle is found
    for window_handle in driver.window_handles:
        if main_window_handler != window_handle:
            driver.switch_to.window(window_handle)
            break

    # locates giving and return giving interest score
    giving_interests = driver.find_element(By.XPATH, "//div[b[text()='Giving Interests']]")
    interest_score = giving_interests.text.splitlines()[1][7:]

    driver.close()
    driver.switch_to.window(main_window_handler)

    return interest_score


# Removes all saved projects
def remove_projects():
    main.fs_open()
    main.fs_login(main.fs_username, main.fs_password)
    navigate()
    navigate()

    try:
        driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_SelectAllButton1").click()
        driver.find_element(By.ID, "ctl00_ctl00_TabContentPlaceHolder_FindFundersContentPlaceHolder_RemoveAllButton").click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(1.5)
    except NoSuchElementException:
        print("My Best Prospects: no projects to remove")
