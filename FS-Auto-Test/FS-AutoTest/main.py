from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome()
driver.get("https://www.foundationsearch.ca")


if __name__ == "__main__":
    print("Opening FoundationSearch")
    input("Press Enter to close the browser...")
    driver.quit()