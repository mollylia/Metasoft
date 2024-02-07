from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
driver = webdriver.Chrome()
