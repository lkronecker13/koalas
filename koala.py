import pandas as pd
from itertools import groupby
import group as gp


class Koala():

    dataframe = pd.DataFrame()
    base_feature = 'base_feature'
    base_groups = []

    def __init__(self, dataframe, base_feature):
        self.dataframe = dataframe
        self.base_feature = base_feature
        self.base_groups = list(dataframe[base_feature].unique())

    def unique_elements_group(self, secondary_feature):
        df_grouped = self.dataframe.groupby([self.base_feature, secondary_feature])
        key_list = list(df_grouped.groups.keys())
        # Group the secondary_feature values that belong to each value in base_feature
        user_ids_per_country = {c: set() for c in self.base_groups}

        for key in key_list:
            user_ids_per_country[key[0]].add(key[1])

        return user_ids_per_country

    def intersection_matrix(self, secondary_feature):
        user_ids_per_country = self.unique_elements_group(secondary_feature)
        userids_per_country_counts = [(k, len(val)) for k, val in user_ids_per_country.items()]

        print('Different user ids per country: ' + str(userids_per_country_counts))

        df_repetitions = pd.DataFrame()
        for country in self.base_groups:
            ids_per_country = user_ids_per_country[country]
            intersect = [len(ids_per_country.intersection(user_ids_per_country[country])) for country in self.base_groups]
            df_repetitions[country] = intersect
            print(str(intersect) + str(country))

        df_repetitions['index'] = self.base_groups
        df_repetitions = df_repetitions.set_index('index')
        return df_repetitions

    def analyze_features(self, feature_names, verbose=True):
        feature_in_groups_dict = {}
        for name in feature_names:
            if verbose:
                print('------------')
                print('Spliting {} into groups given by the unique elements of {}'.format(name, self.base_feature))
                print('------------')
            feature_in_groups_dict[name] = self.analyze_feature(name, verbose)

        return feature_in_groups_dict

    def analyze_feature(self, feature, verbose=True):
        df_grouped_country = self.dataframe.groupby(self.base_feature)
        # See how secondary feature distributes over base_feature by taking each value in the later.
        groups = []
        for key, group in df_grouped_country:
            all_records = sorted(list(group[feature].values), reverse=True)
            if all_records:
                group = gp.Group(group, key, feature)
                groups.append(group)
                if verbose:
                    print('Group details for : *{}*.'.format(key))
                    print(group)


            else:
                print('Features are exclusive')
                groups.append(gp.Group())

            print('-------------')

        return groups
