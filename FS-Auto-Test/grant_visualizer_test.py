import unittest
import main
import grant_visualizer


class GrantVisualizerTest(unittest.TestCase):
    def setUp(self):
        main.fs_open()
        main.fs_login(main.fs_username, main.fs_password)
        grant_visualizer.navigate()

    # def test_no_criteria(self):
    #     self.assertEqual("2,172,407", grant_visualizer.get_number_results())
    #
    # def test_multiple_criteria(self):
    #     grant_visualizer.set_to_province("Alberta")
    #     grant_visualizer.add_to_province("Manitoba")
    #     grant_visualizer.set_year("2020")
    #     grant_visualizer.add_year("2021")
    #     grant_visualizer.set_category("Health")
    #     grant_visualizer.add_category("Environment")
    #     grant_visualizer.set_size("$1 to $9,999")
    #     grant_visualizer.add_size("$10,000 to $24,999")
    #     grant_visualizer.set_funder_designation("Private Foundations", "Charitable Organizations", "")
    #     grant_visualizer.search()
    #     self.assertEqual("2,271", grant_visualizer.get_number_results())

    def test_map(self):
        grant_visualizer.view_mode("Map")
        self.assertEqual("2,172,407", grant_visualizer.get_number_results())

    def test_map_first_selector(self):
        grant_visualizer.view_mode("Map")
        grant_visualizer.mode_set_dependent_variable("Number of Grants")
        self.assertEqual("2,172,407", grant_visualizer.get_number_results())

    def test_map_second_selector(self):
        grant_visualizer.view_mode("Map")
        grant_visualizer.map_set_grant_direction("Grants Given")
        self.assertEqual("2,277,385", grant_visualizer.get_number_results())

    def test_map_all_selectors(self):
        grant_visualizer.view_mode("Map")
        grant_visualizer.mode_set_dependent_variable("Number of Grants")
        grant_visualizer.map_set_grant_direction("Grants Given")
        self.assertEqual("2,277,385", grant_visualizer.get_number_results())

    # def test_chart(self):
    #     grant_visualizer.view_mode("Chart")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_chart_first_selector(self):
    #     grant_visualizer.view_mode("Chart")
    #     grant_visualizer.chart_set_independent_variable("Category")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_chart_second_selector(self):
    #     grant_visualizer.view_mode("Chart")
    #     grant_visualizer.mode_set_dependent_variable("Number of Grants")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_chart_third_selector(self):
    #     grant_visualizer.view_mode("Chart")
    #     grant_visualizer.chart_type("Horizontal Bar (3D)")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_chart_fourth_selector(self):
    #     grant_visualizer.view_mode("Chart")
    #     grant_visualizer.mode_set_dependent_variable("Grant Amount / Number of Grants")
    #     grant_visualizer.chart_set_bubble("Bubble size = Grant Amount")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_chart_all_selectors(self):
    #     grant_visualizer.view_mode("Chart")
    #     grant_visualizer.chart_set_independent_variable("Category")
    #     grant_visualizer.mode_set_dependent_variable("Number of Grants")
    #     grant_visualizer.chart_type("Horizontal Bar (3D)")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_summary(self):
    #     grant_visualizer.view_mode("Summary")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_summary_all_selectors(self):
    #     grant_visualizer.view_mode("Summary")
    #     grant_visualizer.summary_group_by("Grant Size")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_list(self):
    #     grant_visualizer.view_mode("List")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())
    #
    # def test_list_all_selectors(self):
    #     grant_visualizer.view_mode("List")
    #     grant_visualizer.list_group_by("By Recipients")
    #     self.assertEqual("2,285,071", grant_visualizer.get_number_results())


if __name__ == '__main__':
    unittest.main()
