import unittest
import main
import foundation_search


class FoundationSearchTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        foundation_search.navigate()

    def tearDown(self):
        print("\n")

    def test_foundation_search_ford(self):
        original_result = 1
        foundation_search.set_foundation_name_with("ford")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_designation_private_sort_asset(self):
        original_result = 6785
        foundation_search.set_funder_designation("Private Foundations", "", "")
        foundation_search.sort_by("Total Assets")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_two_designations(self):
        original_result = 204
        foundation_search.set_foundation_name_with("foundation")
        foundation_search.set_funder_designation("Charitable Organizations", "Community Foundations", "")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_giving_interest_school(self):
        original_result = 2890
        foundation_search.set_giving_interest("School")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_giving_interest_school_OR_house(self):
        original_result = 2890
        foundation_search.set_giving_interest("School OR House")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_giving_interest_school_OR_athletes(self):
        original_result = 2911
        foundation_search.set_giving_interest("School OR Athletes")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_giving_interest_school_AND_athletes(self):
        original_result = 80
        foundation_search.set_giving_interest("School AND Athletes")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_multiple_criteria(self):
        original_result = 1539
        foundation_search.set_foundation_name_with("foundation")
        foundation_search.set_funder_designation("Private Foundations", "", "")
        foundation_search.sort_by("Total Assets")
        foundation_search.set_giving_interest("School")
        foundation_search.search()
        self.assertTrue(original_result*0.8 <= foundation_search.get_number_results() <= original_result*1.2, "Result is more than 20% off")


if __name__ == '__main__':
    unittest.main()
