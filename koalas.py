from itertools import groupby

def count_ocurrence_of_one_feature_into_another(dataframe, base_feature, secondary_feature):
    # List of countries with the unknown one as the first one
    unique_countries = dataframe[base_feature].unique()
    df_grouped = dataframe.groupby([base_feature, secondary_feature])
    
    key_list = list(df_grouped.groups.keys())
    # Group the secondary_feature values that belong to each value in base_feature
    user_ids_per_country = {c: set() for c in unique_countries}

    for key in key_list:
        user_ids_per_country[key[0]].add(key[1])
        
    return user_ids_per_country

def analyze_groups(dataframe, base_feature):
    df_grouped_country = dataframe.groupby(base_feature)
    
    # See how secondary feature distributes over base_feature by taking each value in the later.
    for key, group in df_grouped_country:
        all_records = sorted(list(group['user_id'].values), reverse=True) 
        if all_records:
            print('Using *{}* to group.'.format(key))
            # Create dictionary of repetitions of each element keyd by the feature value
            repetitions_dict = {key : len(list(group)) for key, group in groupby(all_records)}
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