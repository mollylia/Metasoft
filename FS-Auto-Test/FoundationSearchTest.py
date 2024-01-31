import unittest
from selenium import webdriver

import main

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)

class FoundationSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_foundation_search_ford(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.setFoundationFoundationName("ford")
        main.search()
        self.assertEqual("1", main.foundationSearchNumResults())


    def test_designation_private_sort_asset(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.setFoundationFunderDesignationOne("Private Foundations")
        main.setFoundationSortBy("Total Assets")
        main.search()
        self.assertEqual("6,661", main.foundationSearchNumResults())


    def test_giving_interest_school(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.enterFoundationGivingInterest("School")
        main.search()
        self.assertEqual("2,860", main.foundationSearchNumResults())


    def test_giving_interest_school_OR_house(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.enterFoundationGivingInterest("\"School\" OR \"House\"")
        main.search()
        self.assertEqual("2,860", main.foundationSearchNumResults())


    def test_giving_interest_school_OR_athletes(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.enterFoundationGivingInterest("\"School\" OR \"Athletes\"")
        main.search()
        self.assertEqual("2,879", main.foundationSearchNumResults())


    def test_giving_interest_school_AND_athletes(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.enterFoundationGivingInterest("\"School\" AND \"Athletes\"")
        main.search()
        self.assertEqual("77", main.foundationSearchNumResults())


    def test_multiple_criteria(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateFoundationSearch()
        main.setFoundationFoundationName("foundation")
        main.setFoundationFunderDesignationOne("Private Foundations")
        main.setFoundationSortBy("Total Assets")
        main.enterFoundationGivingInterest("School")
        main.search()
        self.assertEqual("1,509", main.foundationSearchNumResults())


if __name__ == '__main__':
    unittest.main()
