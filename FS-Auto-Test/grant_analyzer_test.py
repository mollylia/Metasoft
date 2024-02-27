import unittest
import main
import grant_analyzer


class GrantAnalyzerTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        grant_analyzer.navigate()

    def test_category(self):
        original_result = 503377
        grant_analyzer.set_category("Health")
        grant_analyzer.add_category("Environment")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_year(self):
        original_result = 318973
        grant_analyzer.set_year("2020")
        grant_analyzer.add_year("2021")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_size(self):
        original_result = 1958345
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.add_size("$10,000 to $24,999")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_foundation_name_with_AND(self):
        original_result = 6313
        grant_analyzer.set_foundation_name_with("foundation AND hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_foundation_name_with_OR(self):
        original_result = 1296946
        grant_analyzer.set_foundation_name_with("foundation OR hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_foundation_name_without_AND(self):
        original_result = 2278758
        grant_analyzer.set_foundation_name_without("foundation AND hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_foundation_name_without_OR(self):
        original_result = 988125
        grant_analyzer.set_foundation_name_without("foundation OR hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_funder_designation(self):
        original_result = 464893
        grant_analyzer.set_funder_designation("Charitable Organizations", "Community Foundations", "")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_province_in(self):
        original_result = 1571079
        grant_analyzer.set_granting_province("In", "Ontario")
        grant_analyzer.add_granting_province("Quebec")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_province_not_in(self):
        original_result = 114477
        grant_analyzer.set_granting_province("Not In", "Ontario")
        grant_analyzer.add_granting_province("Quebec")
        grant_analyzer.add_granting_province("Alberta")
        grant_analyzer.add_granting_province("British Columbia")
        grant_analyzer.add_granting_province("Manitoba")
        grant_analyzer.add_granting_province("Nunavut")
        grant_analyzer.add_granting_province("Yukon")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_city_in_AND(self):
        original_result = 0
        grant_analyzer.set_granting_city("In", "Vancouver AND Toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_city_in_OR(self):
        original_result = 969200
        grant_analyzer.set_granting_city("In", "Vancouver OR Toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_city_not_in_AND(self):
        original_result = 2285071
        grant_analyzer.set_granting_city("Not In", "Vancouver AND Toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_granting_city_not_in_OR(self):
        original_result = 1315871
        grant_analyzer.set_granting_city("Not In", "Vancouver OR Toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_name_with_AND(self):
        original_result = 53768
        grant_analyzer.set_recipient_name_with("foundation AND hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_name_with_OR(self):
        original_result = 357331
        grant_analyzer.set_recipient_name_with("foundation OR hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_name_without_AND(self):
        original_result = 125715
        grant_analyzer.set_year("2022")
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.set_recipient_name_without("foundation AND hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_name_without_OR(self):
        original_result = 109342
        grant_analyzer.set_year("2022")
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.set_recipient_name_without("foundation OR hospital")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_province_in(self):
        original_result = 1343005
        grant_analyzer.set_recipient_province("In", "British Columbia")
        grant_analyzer.add_recipient_province("Ontario")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_province_not_in(self):
        original_result = 940735
        grant_analyzer.set_recipient_province("Not In", "British Columbia")
        grant_analyzer.add_recipient_province("Ontario")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_city_in_AND(self):
        original_result = 0
        grant_analyzer.set_recipient_city("In", "vancouver AND toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_city_in_OR(self):
        original_result = 497881
        grant_analyzer.set_recipient_city("In", "vancouver OR toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")

    def test_recipient_city_not_in_OR(self):
        original_result = 58134
        grant_analyzer.set_category("Health")
        grant_analyzer.set_funder_designation("Charitable Organizations", "", "")
        grant_analyzer.set_recipient_city("Not In", "vancouver OR toronto")
        grant_analyzer.search()
        self.assertTrue(original_result*0.8 <= grant_analyzer.get_number_results() <= original_result*1.2, "Result is more than 20% off")


if __name__ == '__main__':
    unittest.main()
