import unittest
import main
import foundation_profile_keyword_search


class FoundationProfileKeywordSearchTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        foundation_profile_keyword_search.navigate()

    def tearDown(self):
        print("\n")

    def test_keyword_search_gates(self):
        foundation_profile_keyword_search.set_keyword("gates")
        foundation_profile_keyword_search.search()
        self.assertTrue(4*0.8 <= foundation_profile_keyword_search.get_number_results() <= 4*1.2, "Result is more than 20% off")

    def test_foundation_search_ford(self):
        foundation_profile_keyword_search.set_foundation_name("ford")
        foundation_profile_keyword_search.search()
        self.assertTrue(1*0.8 <= foundation_profile_keyword_search.get_number_results() <= 1*1.2, "Result is more than 20% off")

    def test_foundation_search_foundation(self):
        foundation_profile_keyword_search.set_foundation_name("foundation")
        foundation_profile_keyword_search.search()
        self.assertTrue(6955*0.8 <= foundation_profile_keyword_search.get_number_results() <= 6955*1.2, "Result is more than 20% off")

    def test_keyword_and_foundation(self):
        foundation_profile_keyword_search.set_foundation_name("foundation")
        foundation_profile_keyword_search.set_keyword("law")
        foundation_profile_keyword_search.search()
        self.assertTrue(29*0.8 <= foundation_profile_keyword_search.get_number_results() <= 29*1.2, "Result is more than 20% off")


if __name__ == '__main__':
    unittest.main()
