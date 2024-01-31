import unittest
from selenium import webdriver

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
        self.assertEqual("3", main.profileSearchNumResults())


    def test_foundation_search_ford(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateProfileKeywordSearch()
        main.setProfileFoundationName("ford")
        main.search()
        self.assertEqual("1", main.profileSearchNumResults())


    def test_foundation_search_foundation(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateProfileKeywordSearch()
        main.setProfileFoundationName("foundation")
        main.search()
        self.assertEqual("6,920", main.profileSearchNumResults())


    def test_keyword_and_foundation(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateProfileKeywordSearch()
        main.setProfileFoundationName("foundation")
        main.setProfileKeyword("law")
        main.search()
        self.assertEqual("30", main.profileSearchNumResults())


if __name__ == '__main__':
    unittest.main()