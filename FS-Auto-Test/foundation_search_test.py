import unittest
import main
import foundation_search


class FoundationSearchTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        foundation_search.navigate()

    def test_foundation_search_ford(self):
        foundation_search.set_foundation_name("ford")
        foundation_search.search()
        self.assertEqual("1", foundation_search.get_number_results())

    def test_designation_private_sort_asset(self):
        foundation_search.set_funder_designation("Private Foundations", "", "")
        foundation_search.sort_by("Total Assets")
        foundation_search.search()
        self.assertEqual("6,661", foundation_search.get_number_results())

    def test_two_designations(self):
        foundation_search.set_foundation_name("foundation")
        foundation_search.set_funder_designation("Charitable Organizations", "Community Foundations", "")
        foundation_search.search()
        self.assertEqual("205", foundation_search.get_number_results())

    def test_giving_interest_school(self):
        foundation_search.set_giving_interest("School")
        foundation_search.search()
        self.assertEqual("2,860", foundation_search.get_number_results())

    def test_giving_interest_school_OR_house(self):
        foundation_search.set_giving_interest("\"School\" OR \"House\"")
        foundation_search.search()
        self.assertEqual("2,860", foundation_search.get_number_results())

    def test_giving_interest_school_OR_athletes(self):
        foundation_search.set_giving_interest("\"School\" OR \"Athletes\"")
        foundation_search.search()
        self.assertEqual("2,879", foundation_search.get_number_results())

    def test_giving_interest_school_AND_athletes(self):
        foundation_search.set_giving_interest("\"School\" AND \"Athletes\"")
        foundation_search.search()
        self.assertEqual("77", foundation_search.get_number_results())

    def test_multiple_criteria(self):
        foundation_search.set_foundation_name("foundation")
        foundation_search.set_funder_designation("Private Foundations", "", "")
        foundation_search.sort_by("Total Assets")
        foundation_search.set_giving_interest("School")
        foundation_search.search()
        self.assertEqual("1,509", foundation_search.get_number_results())


if __name__ == '__main__':
    unittest.main()
