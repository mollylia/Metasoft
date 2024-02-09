import unittest
import main
import power_search


class PowerSearchTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        power_search.navigate()

    def test_all_canadian(self):
        power_search.set_search_request("ford")
        power_search.select_all_canadian_databases()
        power_search.search()
        self.assertEqual("361", power_search.get_number_results())

    def test_all_american(self):
        power_search.set_search_request("ford")
        power_search.select_all_american_databases()
        power_search.search()
        self.assertEqual("17,385", power_search.get_number_results())

    def test_all_uk(self):
        power_search.set_search_request("ford")
        power_search.select_all_uk_databases()
        power_search.search()
        self.assertEqual("160", power_search.get_number_results())

    def test_all_australian(self):
        power_search.set_search_request("ford")
        power_search.select_all_australian_databases()
        power_search.search()
        self.assertEqual("1", power_search.get_number_results())

    def test_all_foundation_profiles(self):
        power_search.set_search_request("ford")
        power_search.select_canadian_database("Foundation Profiles")
        power_search.select_american_database("Foundation Profiles")
        power_search.select_uk_database("Foundation Profiles")
        power_search.select_australian_database("Foundation Profiles")
        power_search.search()
        self.assertEqual("477", power_search.get_number_results())

    def test_stemming_search(self):
        power_search.set_search_request("ford")
        power_search.select_canadian_database("Foundation Profiles")
        power_search.select_american_database("Foundation Profiles")
        power_search.select_uk_database("Foundation Profiles")
        power_search.select_australian_database("Foundation Profiles")
        power_search.search()
        self.assertEqual("477", power_search.get_number_results())

if __name__ == '__main__':
    unittest.main()
