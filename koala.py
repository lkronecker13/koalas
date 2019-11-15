import pandas as pd
from itertools import groupby


class Koala():

    dataframe = pd.DataFrame()
    base_feature = 'base_feature'
    base_groups = []

    def __init__(self, dataframe, base_feature):
        self.dataframe = dataframe
        self.base_feature = base_feature
        self.base_groups = list(dataframe[base_feature].unique())

    def count_ocurrence_of_one_feature_into_another(self, secondary_feature):
        # List of countries with the unknown one as the first one
        unique_countries = self.dataframe[self.base_feature].unique()
        df_grouped = self.dataframe.groupby([self.base_feature, secondary_feature])

        key_list = list(df_grouped.groups.keys())
        # Group the secondary_feature values that belong to each value in base_feature
        user_ids_per_country = {c: set() for c in unique_countries}

        for key in key_list:
            user_ids_per_country[key[0]].add(key[1])

        return user_ids_per_country

    def intersection_matrix(self, secondary_feature):
        user_ids_per_country = self.count_ocurrence_of_one_feature_into_another(secondary_feature)
        userids_per_country_counts = [(k, len(val)) for k, val in user_ids_per_country.items()]

        print('Different user ids per country: ' + str(userids_per_country_counts))
        print('Unique *{}* per *{}*'.format(secondary_feature, self.base_feature))

        print('-------------')

        print('Intersection matrix')
        print(self.base_groups)
        for country in self.base_groups:
            print(str([len(user_ids_per_country[country].intersection(user_ids_per_country[c])) for c in
                       self.dataframe['country'].unique()]) + str(country))

    def analyze_features(self, feature_names):
        for name in feature_names:
            self.analize_feature(name)

    def analize_feature(self, feature):
        df_grouped_country = self.dataframe.groupby(self.base_feature)
        # See how secondary feature distributes over base_feature by taking each value in the later.
        for key, group in df_grouped_country:
            all_records = sorted(list(group[feature].values), reverse=True)
            if all_records:
                print('Using *{}* to group.'.format(key))
                # Create dictionary of repetitions of each element keyd by the feature value
                repetitions_dict = {key: len(list(group)) for key, group in groupby(all_records)}
                sorted_list_max = sorted(repetitions_dict.items(), key=lambda x: x[1], reverse=True)
                sorted_list_min = sorted(repetitions_dict.items(), key=lambda x: x[1], reverse=False)
                unique_records = set(all_records)

                print('Total records {}'.format(len(all_records)))
                print('Most repeted elements: {}'.format(sorted_list_max[:5]))
                print('Least repeted elements: {}'.format(sorted_list_min[:5]))
                print('Unique records {}'.format(len(unique_records)))

            else:
                print('No records found')
            print('-------------')

