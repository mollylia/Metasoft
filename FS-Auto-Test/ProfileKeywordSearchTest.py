import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import main

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)

class ProfileKeywordSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_keyword_search_gates(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateProfileKeywordSearch()
        main.setProfileKeyword("gates")
        main.search()
        self.assertEqual(main.keywordSearchNumResults(), 3)


    def test_foundation_search_ford(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateProfileKeywordSearch()
        main.setProfileFoundationName("ford")
        main.search()
        self.assertEqual(main.keywordSearchNumResults(), 1)

if __name__ == '__main__':
    unittest.main()
