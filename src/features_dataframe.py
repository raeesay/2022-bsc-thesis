import pickle
from functools import reduce

import pandas as pd


def role_features():
    # load the node roles
    node_roles = pickle.load(open("./pickles/roles.pickle", "rb"))
    # convert dictionary to dataframe
    df_roles = pd.DataFrame(node_roles.items())
    # rename columns for consistency
    df_roles.columns = ['username', 'role']

    # degree
    node_degree = pickle.load(open("./pickles/metrics/degree.pickle", "rb"))
    df_degree = pd.DataFrame(node_degree.items())
    df_degree.columns = ['username', 'degree']

    # out_degree
    node_outdeg = pickle.load(open("./pickles/metrics/outdeg.pickle", "rb"))
    df_outdeg = pd.DataFrame(node_outdeg.items())
    df_outdeg.columns = ['username', 'outdegree']

    # in_degree
    node_indeg = pickle.load(open("./pickles/metrics/indeg.pickle", "rb"))
    df_indeg = pd.DataFrame(node_indeg.items())
    df_indeg.columns = ['username', 'indegree']

    # clustering coefficient
    node_clustering = pickle.load(open("./pickles/metrics/clustering.pickle", "rb"))
    df_clustering = pd.DataFrame(node_clustering.items())
    df_clustering.columns = ['username', 'clustering']

    # closeness centrality
    node_closecentrality = pickle.load(open("./pickles/metrics/closeness_centrality.pickle", "rb"))
    df_closecentrality = pd.DataFrame(node_closecentrality.items())
    df_closecentrality.columns = ['username', 'closeness']

    # betweenness centrality
    node_betwcentrality = pickle.load(open("./pickles/metrics/betweenness_centrality.pickle", "rb"))
    df_betwcentrality = pd.DataFrame(node_betwcentrality.items())
    df_betwcentrality.columns = ['username', 'betweenness']

    # eigenvector centrality
    node_eigenvectorcentrality = pickle.load(open("./pickles/metrics/eigenvector_centrality.pickle", "rb"))
    df_eigenvectorcentrality = pd.DataFrame(node_eigenvectorcentrality.items())
    df_eigenvectorcentrality.columns = ['username', 'eigenvector']

    # shellindex
    node_shellindex = pickle.load(open("./pickles/metrics/shellindex.pickle", "rb"))
    df_shellindex = pd.DataFrame(node_shellindex.items())
    df_shellindex.columns = ['username', 'shellindex']

    # eccentricity
    node_eccentricity = pickle.load(open("./pickles/metrics/eccentricity.pickle", "rb"))
    df_eccentricity = pd.DataFrame(node_eccentricity.items())
    df_eccentricity.columns = ['username', 'eccentricity']

    # pagerank
    node_pagerank = pickle.load(open("./pickles/metrics/pagerank.pickle", "rb"))
    df_pagerank = pd.DataFrame(node_pagerank.items())
    df_pagerank.columns = ['username', 'pagerank']


    # summarise all dataframes
    data_frames = [
        df_roles, df_degree, df_outdeg, df_indeg, df_clustering,
        df_closecentrality, df_betwcentrality, df_eigenvectorcentrality, df_shellindex,
        df_eccentricity, df_pagerank]

    # merge the dataframes with username as common column
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['username'],
                                                    how='outer'), data_frames)

    # sort dataframe by roles
    df_merged.sort_values('role', inplace=True)

    # pickle the merged dataframe for easy access
    df_merged.to_pickle('./pickles/df_merged.pickle')

    return df_merged

