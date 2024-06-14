import unittest
import pandas as pd
from pfisheries import of_country_codes, of_species_codes, of_landings
from plotting import fish_plot
import matplotlib.pyplot as plt

class TestPFisheriesFunctions(unittest.TestCase):

    def test_main_functions_return_dataframes(self):
        cc = of_country_codes()
        sp = of_species_codes()
        landings = of_landings(country='CAN')
        lbysp = of_landings(species='SKJ')

        self.assertIsInstance(cc, pd.DataFrame)
        self.assertIsInstance(sp, pd.DataFrame)
        self.assertIsInstance(landings, pd.DataFrame)
        self.assertIsInstance(lbysp, pd.DataFrame)
        self.assertEqual(sp.shape[1], 5)
        self.assertEqual(cc.shape[1], 2)
        self.assertEqual(landings.shape[1], 3)

    def test_functions_fail_with_bad_arguments(self):
        # Test invalid species code
        result_species = of_landings(species='foo')
        self.assertIsNone(result_species)  # Expecting None for invalid species

        # Test invalid country code
        result_country = of_landings(country='foo')
        self.assertIsNone(result_country)  # Expecting None for invalid country

        # Test both invalid species and country codes
        result_both =  of_landings(species='foo', country='foo')
        self.assertIsNone(result_both)

    def test_visualizations_are_of_right_class(self):
        species_code_data = pd.read_csv('species_code_data.csv')
        country_code_data = pd.read_csv('country_code_data.csv')
        test_plot = fish_plot(of_landings(species='COD'), species_code_data=species_code_data, country_code_data=country_code_data)
        self.assertIsInstance(test_plot, plt.Axes)
        
        # Add a print statement to check if this test method is being executed
        print("Test test_visualizations_are_of_right_class executed.")

if __name__ == '__main__':
    unittest.main()

