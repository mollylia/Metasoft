import unittest
import main
import power_search


class PowerSearchTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        power_search.navigate()

    def tearDown(self):
        print("\n")

    def test_all_canadian(self):
        original_result = 361
        power_search.set_search_request("ford")
        power_search.select_all_canadian_databases()
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_all_american(self):
        original_result = 17550
        power_search.set_search_request("ford")
        power_search.select_all_american_databases()
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_all_uk(self):
        original_result = 160
        power_search.set_search_request("ford")
        power_search.select_all_uk_databases()
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_all_australian(self):
        original_result = 1
        power_search.set_search_request("ford")
        power_search.select_all_australian_databases()
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_all_foundation_profiles(self):
        original_result = 475
        power_search.set_search_request("ford")
        power_search.select_canadian_database("Foundation Profiles")
        power_search.select_american_database("Foundation Profiles")
        power_search.select_uk_database("Foundation Profiles")
        power_search.select_australian_database("Foundation Profiles")
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_stemming_search(self):
        original_result = 475
        power_search.set_search_request("ford")
        power_search.select_canadian_database("Foundation Profiles")
        power_search.select_american_database("Foundation Profiles")
        power_search.select_uk_database("Foundation Profiles")
        power_search.select_australian_database("Foundation Profiles")
        power_search.select_search_feature("Stemming")
        power_search.search()
        self.assertTrue(original_result*0.8 <= power_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")


if __name__ == '__main__':
    unittest.main()
