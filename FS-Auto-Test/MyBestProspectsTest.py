import unittest
from selenium import webdriver

import main

fs_username = ""                 # change this to valid username (string)
fs_password = ""                 # change this to valid password (string)

class MyBestProspects(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_vancouver_foundation(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateMyBestProspects()
        main.prospectsProjectDefinition("Vancouver Foundation", "2147483647", "British Columbia", "Computer")
        main.searchProspects()
        self.assertEqual("0", main.prospectFindInterestNumber("VANCOUVER FOUNDATION"))

    def test_abundance_canada(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateMyBestProspects()
        main.prospectsProjectDefinition("Abundance Canada", "250", "Manitoba", "School")
        main.addProspectsProvince("Alberta")
        main.addProspectsProvince("British Columbia")
        main.addProspectsInterest("Law")
        main.addProspectsInterest("Food")
        main.searchProspects()
        self.assertEqual("98", main.prospectFindInterestNumber("ABUNDANCE CANADA"))

    def test_hudsons_bay_foundation(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateMyBestProspects()
        main.prospectsProjectDefinition("Hudson's Bay Foundation", "250", "Manitoba", "School")
        main.addProspectsProvince("Alberta")
        main.addProspectsProvince("British Columbia")
        main.addProspectsInterest("Law")
        main.addProspectsInterest("Food")
        main.searchProspects()
        self.assertEqual("79", main.prospectFindInterestNumber("HUDSON'S BAY FOUNDATION"))


    def test_multiple(self):
        driver = self.driver
        main.fsOpen()
        main.fsLogin(fs_username, fs_password)
        main.navigateMyBestProspects()
        main.prospectsProjectDefinition("Multiple", "3000", "Manitoba", "Advocacy")
        main.addProspectsProvince("Alberta")
        main.addProspectsProvince("British Columbia")
        main.addProspectsProvince("Ontario")
        main.addProspectsProvince("Quebec")
        main.addProspectsInterest("Camp")
        main.addProspectsInterest("Artifacts")
        main.searchProspects()
        self.assertEqual("68", main.prospectFindInterestNumber("WINBERG FOUNDATION"))

if __name__ == '__main__':
    unittest.main()