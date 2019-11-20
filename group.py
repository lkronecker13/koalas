import pandas as pd
from itertools import groupby


class Group():
    name = 'group name'
    secondary_feature = 'secondary_feature'
    dataframe = pd.DataFrame()
    cardinality = 0
    repetitions = {}
    cardinality_of_unique = 0

    def __init__(self, dataframe, name, secondary_feature):
        self.secondary_feature = secondary_feature
        self.name = name
        self.dataframe = dataframe

        all_records = sorted(list(dataframe[secondary_feature].values), reverse=True)
        if all_records:
            self.cardinality = len(all_records)
            self.repetitions = {key: len(list(group)) for key, group in groupby(all_records)}
            self.cardinality_of_unique = len(set(all_records))
        else:
            print('No values found')

    def __str__(self):
        sorted_list_max = sorted(self.repetitions.items(), key=lambda x: x[1], reverse=True)
        sorted_list_min = sorted(self.repetitions.items(), key=lambda x: x[1], reverse=False)
        return 'name: {}' \
               '\ncardinality: {}' \
               '\nMost repeted elements: {}' \
               '\nLeast repeted elements: {}' \
               '\nUnique records {}'\
            .format(self.name, self.cardinality, sorted_list_max[:5], sorted_list_min[:5], self.cardinality_of_unique)
