import unittest
import main
import my_best_prospects


class MyBestProspectsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        my_best_prospects.remove_projects()

    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        my_best_prospects.navigate()

    def tearDown(self):
        print("\n")

    def test_vancouver_foundation(self):
        my_best_prospects.create_project_definition("Vancouver Foundation", "2147483647", "British Columbia", "Computer")
        my_best_prospects.search()
        self.assertEqual("0", my_best_prospects.find_interest_number("VANCOUVER FOUNDATION"))

    def test_abundance_canada(self):
        my_best_prospects.create_project_definition("Abundance Canada", "250", "Manitoba", "School")
        my_best_prospects.add_province("Alberta")
        my_best_prospects.add_province("British Columbia")
        my_best_prospects.add_interest("Law")
        my_best_prospects.add_interest("Food")
        my_best_prospects.search()
        self.assertEqual("98", my_best_prospects.find_interest_number("ABUNDANCE CANADA"))

    def test_hudsons_bay_foundation(self):
        my_best_prospects.create_project_definition("Hudson's Bay Foundation", "250", "Manitoba", "School")
        my_best_prospects.add_province("Alberta")
        my_best_prospects.add_province("British Columbia")
        my_best_prospects.add_interest("Law")
        my_best_prospects.add_interest("Food")
        my_best_prospects.search()
        self.assertEqual("79", my_best_prospects.find_interest_number("HUDSON'S BAY FOUNDATION"))

    def test_multiple(self):
        my_best_prospects.create_project_definition("Multiple", "3000", "Manitoba", "Advocacy")
        my_best_prospects.add_province("Alberta")
        my_best_prospects.add_province("British Columbia")
        my_best_prospects.add_province("Ontario")
        my_best_prospects.add_province("Quebec")
        my_best_prospects.add_interest("Camp")
        my_best_prospects.add_interest("Artifacts")
        my_best_prospects.search()
        self.assertEqual("91", my_best_prospects.find_interest_number("BOLAND"))
        # self.assertEqual("91", my_best_prospects.find_interest_number("BOLAND FOUNDATION"))


if __name__ == '__main__':
    unittest.main()
