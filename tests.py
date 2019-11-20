from unittest import TestCase
from koalas import *
import pandas as pd
import koala as ko

dataframe = pd.read_csv('df_modeling.csv')
base_feature = 'country'
base_feature_unique = dataframe[base_feature].unique()
koala = ko.Koala(dataframe, base_feature)


class Tests(TestCase):
    def test_koala_constructor(self):
        print(koala.base_feature)
        print(koala.base_groups)
        self.assertTrue(koala)


    def test_analyze_groups(self):
        list_of_features = ['user_id', 'joining_date']
        feature_in_groups_dict = koala.analyze_features(list_of_features, False)
        self.assertTrue(list(feature_in_groups_dict.keys()) == list_of_features)
        print(feature_in_groups_dict)

    def test_intersection_matrix(self):
        df_repetitions = koala.intersection_matrix('user_id')
        print(df_repetitions.head(7))
        self.assertTrue(df_repetitions.columns.all(base_feature_unique))


