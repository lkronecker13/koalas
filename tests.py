from unittest import TestCase
from koalas import *
import pandas as pd

dataframe = pd.read_csv('df_modeling.csv')
base_feature = 'country'
base_feature_unique = dataframe[base_feature].unique()

class Tests(TestCase):
    def test_analyze_groups(self):
        print('-----------------------------------------------------------------')
        print('Base feature *{}* with {} unique values: {}'.format(base_feature,
                                                                   len(base_feature_unique),
                                                                   base_feature_unique))
        print('-----------------------------------------------------------------')

        # Create quantitative statistics of each group
        analyze_groups(dataframe, base_feature)
        self.assertTrue(True)

    def test_ocurrence(self):
        secondary_feature = 'user_id'  # We'll loop here
        user_ids_per_country = count_ocurrence_of_one_feature_into_another(dataframe, base_feature, secondary_feature)
        userids_per_country_counts = [(k, len(val)) for k, val in user_ids_per_country.items()]

        print('Different user ids per country: ' + str(userids_per_country_counts))
        print('Unique *{}* per *{}*'.format(secondary_feature, base_feature))

        print('-------------')

        print('Intersection matrix')
        print(base_feature_unique)
        for country in base_feature_unique:
            print(str([len(user_ids_per_country[country].intersection(user_ids_per_country[c])) for c in
                       dataframe['country'].unique()]) + str(country))

        self.assertTrue(True)

