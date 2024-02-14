import unittest
import main
import grant_visualizer


class GrantVisualizerTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        grant_visualizer.navigate()

    def test_no_criteria(self):
        self.assertEqual("2,116,165", grant_visualizer.get_number_results())

    def test_multiple_criteria(self):
        grant_visualizer.set_to_province("Alberta")
        grant_visualizer.add_to_province("Manitoba")
        grant_visualizer.set_year("2020")
        grant_visualizer.add_year("2021")
        grant_visualizer.set_category("Health")
        grant_visualizer.add_category("Environment")
        grant_visualizer.set_size("$1 to $9,999")
        grant_visualizer.add_size("$10,000 to $24,999")
        grant_visualizer.set_funder_designation("Private Foundations", "Charitable Organizations", "")
        grant_visualizer.search()
        self.assertEqual("2,283", grant_visualizer.get_number_results())

    # def test_summary(self):
    #     grant_visualizer.view_mode("Summary")
    #     self.assertEqual("2,225,796", grant_visualizer.get_number_results())
    #
    # def test_chart(self):
    #     grant_visualizer.view_mode("Chart")
    #     self.assertEqual("2,225,796", grant_visualizer.get_number_results())
    #
    # def test_list(self):
    #     grant_visualizer.view_mode("List")
    #     self.assertEqual("2,225,796", grant_visualizer.get_number_results())
    #
    # def test_map_selectors(self):
    #     grant_visualizer.mode_set_dependent_variable("Number of Grants")
    #     self.assertEqual("2,116,165", grant_visualizer.get_number_results())


if __name__ == '__main__':
    unittest.main()
