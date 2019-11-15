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
        koala.analyze_features(['user_id', 'joining_date'])
        self.assertTrue(True)

    def test_intersection_matrix(self):
        koala.intersection_matrix('user_id')

        self.assertTrue(True)

