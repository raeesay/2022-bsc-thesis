import networkx as nx

import load_data as load
import role_extraction  as role
import node_features as features
import features_dataframe as dataframe
import correlation
import plot_scatter as scatter
import plot_histogram as histogram
import politiker_info as pol_data
import political_analysis as analysis

if __name__ == "__main__":
    
    # load data either locally or remotely by connecting to the database
    # create directed network g 1using data
    x = input('Enter 1 if data is to be loaded locally, enter 2 to connect to the database and retrieve the results: ')
    if x == '1':
        g = load.local_data()
    elif x == '2':
        g = load.remote_data()
    else:
        print('ERROR')
        exit()
    
    # basic information of network
    print('graph information:', nx.info(g))

    # extract roles from network and pickle
    role.compute_roles(g)

    # extract features for all nodes and pickle
    features.extract_node_features()
    # list all nodes with their respective roles and features in dataframe
    # dataframe is sorted by roles
    df = dataframe.role_features()

    # compute correlation matrix and plot the mean, standard deviation and variance for all features
    # plots are saved
    correlation.mean(df)
    correlation.std_dev(df)
    correlation.variance(df)

    # plot and save scatterplots for all features
    scatter.plot_scatter(df)
    # plot and save histograms for all features
    histogram.plot_histogram(df)

    # list all nodes and their roles and political attributes in a dataframe
    df_political = pol_data.politiker_info()
    # plot the distribution across roles for each political attribute
    analysis.pol_analysis(df)





