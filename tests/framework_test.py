import networkx as nx
import numpy as np
import pandas as pd
import role_extraction_test as role_extraction


# get node degrees
def compute_degree(node, g):
    return g.degree(node)

# get node roles
def compute_noderoles(g, node):
    return role_extraction.compute_roles(g)[node]

# get clustering coefficients of node
def compute_clustering(node, g):
    return nx.clustering(g, node)

# get betweenness centrality of node
def compute_betweenness_centrality(g, node):
    return nx.betweenness_centrality(g)[node]


def graph_statistics(g):
    # dict, where each column corresponds to an attribute of a node
    attr_dicts = [
        {'node': node,
#         'role': compute_noderoles(g, node),
         'degree': compute_degree(node, g),
         'clustering coefficient': compute_clustering(node, g),
#         'betweenness centrality': compute_betweenness_centrality(g, node)
         }
        for node in g.nodes
    ]

    # dict used for dataframe
    df = pd.DataFrame(attr_dicts)
    df.set_index('node', inplace=True)
    # sort dataframe according values in a chosen column
    sorted_df = df.sort_values(by=['node'], ascending=True)

    print(sorted_df)
    return sorted_df
