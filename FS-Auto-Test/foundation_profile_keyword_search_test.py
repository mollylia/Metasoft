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
        self.assertEqual("4", foundation_profile_keyword_search.get_number_results())

    def test_foundation_search_ford(self):
        foundation_profile_keyword_search.set_foundation_name("ford")
        foundation_profile_keyword_search.search()
        self.assertEqual("1", foundation_profile_keyword_search.get_number_results())

    def test_foundation_search_foundation(self):
        foundation_profile_keyword_search.set_foundation_name("foundation")
        foundation_profile_keyword_search.search()
        self.assertEqual("6,955", foundation_profile_keyword_search.get_number_results())

    def test_keyword_and_foundation(self):
        foundation_profile_keyword_search.set_foundation_name("foundation")
        foundation_profile_keyword_search.set_keyword("law")
        foundation_profile_keyword_search.search()
        self.assertEqual("29", foundation_profile_keyword_search.get_number_results())


if __name__ == '__main__':
    print("TESTING: foundation profile keyword search")
    unittest.main()
