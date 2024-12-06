import pickle
from functools import reduce

import pandas as pd


def politiker_info():

    # load the node roles
    node_roles = pickle.load(open("./pickles/roles.pickle", "rb"))
    # convert dictionary to dataframe
    df_roles = pd.DataFrame(node_roles.items())
    # rename columns for consistency
    df_roles.columns = ['username', 'role']

    # load csv file containing information on politicians
    pol_info = pd.read_csv('./politiker-info.csv', encoding="ISO-8859-1")

    # remove unecessary columns
    df_info = pol_info.drop(['Unnamed: 0', 'user_id', 'twitter_name', 'from',
                'until', 'abgeordnetenwatch_id', 'wikidata_id'], axis=1)

    # make all twitter handles lower case for efficient merging
    df_info['twitter_handle'] = df_info['twitter_handle'].str.lower()

    # rename column to match with column in roles for efficient merging
    df_info.rename(columns={'twitter_handle': 'username'}, inplace=True)
    print(df_info.head())

    # merge the roles and info dataframes
    df_final = df_roles.merge(df_info, on='username')

    # change values in role column to unique integers for overview
    df_final['role'] = pd.factorize(df_final.role)[0]
    df_final.sort_values('role', inplace=True)

    df_final.to_pickle('./pickles/df_info.pickle')

    return df_final


