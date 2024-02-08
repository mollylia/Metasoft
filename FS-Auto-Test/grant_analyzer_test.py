import unittest
import main
import grant_analyzer


class GrantAnalyzerTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        grant_analyzer.navigate()

    def test_category(self):
        grant_analyzer.set_category("Health")
        grant_analyzer.add_category("Environment")
        grant_analyzer.search()
        self.assertEqual("491,292", grant_analyzer.get_number_results())

    def test_year(self):
        grant_analyzer.set_year("2020")
        grant_analyzer.add_year("2021")
        grant_analyzer.search()
        self.assertEqual("321,514", grant_analyzer.get_number_results())

    def test_size(self):
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.add_size("$10,000 to $24,999")
        grant_analyzer.search()
        self.assertEqual("1,914,400", grant_analyzer.get_number_results())

    def test_foundation_name_with_AND(self):
        grant_analyzer.set_foundation_name_with("foundation AND hospital")
        grant_analyzer.search()
        self.assertEqual("6,093", grant_analyzer.get_number_results())

    def test_foundation_name_with_OR(self):
        grant_analyzer.set_foundation_name_with("foundation OR hospital")
        grant_analyzer.search()
        self.assertEqual("1,245,616", grant_analyzer.get_number_results())

    def test_foundation_name_without_AND(self):
        grant_analyzer.set_foundation_name_without("foundation AND hospital")
        grant_analyzer.search()
        self.assertEqual("2,219,703", grant_analyzer.get_number_results())

    def test_foundation_name_without_OR(self):
        grant_analyzer.set_foundation_name_without("foundation OR hospital")
        grant_analyzer.search()
        self.assertEqual("980,180", grant_analyzer.get_number_results())

    def test_funder_designation(self):
        grant_analyzer.set_funder_designation("Charitable Organizations", "Community Foundations", "")
        grant_analyzer.search()
        self.assertEqual("447,206", grant_analyzer.get_number_results())

    def test_granting_province_in(self):
        grant_analyzer.set_granting_province("In", "Ontario")
        grant_analyzer.add_granting_province("Quebec")
        grant_analyzer.search()
        self.assertEqual("1,535,446", grant_analyzer.get_number_results())

    def test_granting_province_not_in(self):
        grant_analyzer.set_granting_province("Not In", "Ontario")
        grant_analyzer.add_granting_province("Quebec")
        grant_analyzer.add_granting_province("Alberta")
        grant_analyzer.add_granting_province("British Columbia")
        grant_analyzer.add_granting_province("Manitoba")
        grant_analyzer.add_granting_province("Nunavut")
        grant_analyzer.add_granting_province("Yukon")
        grant_analyzer.search()
        self.assertEqual("111,543", grant_analyzer.get_number_results())

    def test_granting_city_in_AND(self):
        grant_analyzer.set_granting_city("In", "Vancouver AND Toronto")
        grant_analyzer.search()
        self.assertEqual("0", grant_analyzer.get_number_results())

    def test_granting_city_in_OR(self):
        grant_analyzer.set_granting_city("In", "Vancouver OR Toronto")
        grant_analyzer.search()
        self.assertEqual("959,427", grant_analyzer.get_number_results())

    def test_granting_city_not_in_AND(self):
        grant_analyzer.set_granting_city("Not In", "Vancouver AND Toronto")
        grant_analyzer.search()
        self.assertEqual("2,225,796", grant_analyzer.get_number_results())

    def test_granting_city_not_in_OR(self):
        grant_analyzer.set_granting_city("Not In", "Vancouver OR Toronto")
        grant_analyzer.search()
        self.assertEqual("1,266,369", grant_analyzer.get_number_results())

    def test_recipient_name_with_AND(self):
        grant_analyzer.set_recipient_name_with("foundation AND hospital")
        grant_analyzer.search()
        self.assertEqual("52,891", grant_analyzer.get_number_results())

    def test_recipient_name_with_OR(self):
        grant_analyzer.set_recipient_name_with("foundation OR hospital")
        grant_analyzer.search()
        self.assertEqual("346,976", grant_analyzer.get_number_results())

    def test_recipient_name_without_AND(self):
        grant_analyzer.set_year("2022")
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.set_recipient_name_without("foundation AND hospital")
        grant_analyzer.search()
        self.assertEqual("86,407", grant_analyzer.get_number_results())

    def test_recipient_name_without_OR(self):
        grant_analyzer.set_year("2022")
        grant_analyzer.set_size("$1 to $9,999")
        grant_analyzer.set_recipient_name_without("foundation OR hospital")
        grant_analyzer.search()
        self.assertEqual("75,438", grant_analyzer.get_number_results())

    def test_recipient_province_in(self):
        grant_analyzer.set_recipient_province("In", "British Columbia")
        grant_analyzer.add_recipient_province("Ontario")
        grant_analyzer.search()
        self.assertEqual("1,321,391", grant_analyzer.get_number_results())

    def test_recipient_province_not_in(self):
        grant_analyzer.set_recipient_province("Not In", "British Columbia")
        grant_analyzer.add_recipient_province("Ontario")
        grant_analyzer.search()
        self.assertEqual("903,071", grant_analyzer.get_number_results())

    def test_recipient_city_in_AND(self):
        grant_analyzer.set_recipient_city("In", "vancouver AND toronto")
        grant_analyzer.search()
        self.assertEqual("0", grant_analyzer.get_number_results())

    def test_recipient_city_in_OR(self):
        grant_analyzer.set_recipient_city("In", "vancouver OR toronto")
        grant_analyzer.search()
        self.assertEqual("486,095", grant_analyzer.get_number_results())

    def test_recipient_city_not_in_OR(self):
        grant_analyzer.set_category("Health")
        grant_analyzer.set_funder_designation("Charitable Organizations", "", "")
        grant_analyzer.set_recipient_city("Not In", "vancouver OR toronto")
        grant_analyzer.search()
        self.assertEqual("56,271", grant_analyzer.get_number_results())


if __name__ == '__main__':
    unittest.main()
