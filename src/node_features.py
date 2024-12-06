import pickle

import igraph as ig
import networkx as nx

import load_data as load

# load the graph
g = load.local_data()

# execute each function pertaining to a certain attribute
# pickle the resulting dictionary for easy access

def extract_node_features(g):
    # node degrees
    with open("./pickles/degree.pickle", "wb") as f:
        obj = {node: g.degree(node) for node in g}
        pickle.dump(obj, f)

    # node in-degree
    with open("./pickles/indeg.pickle", "wb") as f:
        obj = {node: g.in_degree(node) for node in g}
        pickle.dump(obj, f)

    # node out-degree
    with open("./pickles/outdeg.pickle", "wb") as f:
        obj = {node: g.out_degree(node) for node in g}
        pickle.dump(obj, f)

    # clustering coefficient of node
    with open("./pickles/clustering.pickle", "wb") as f:
        obj = {node: nx.clustering(g, node) for node in g}
        pickle.dump(obj, f)

    # eigenvector centrality
    with open("./pickles/eigenvector_centrality.pickle", "wb") as f:
        obj = nx.eigenvector_centrality(g)
        pickle.dump(obj, f)

    # closeness centrality
    with open("./pickles/closeness_centrality.pickle", "wb") as f:
        obj = nx.closeness_centrality(g)
        pickle.dump(obj, f)

    # betweenness centrality
    with open("./pickles/betweenness_centrality.pickle", "wb") as f:
        obj = nx.betweenness_centrality(g)
        pickle.dump(obj, f)

    # convert to igraph
    G = ig.Graph.from_networkx(g)

    # recover original node identifiers
    nx_ids = G.vs.get_attribute_values('_nx_name')

    with open("./pickles/shellindex.pickle", "wb") as f:
        temp = ig.Graph.shell_index(G)
        obj = dict(zip(nx_ids, temp))
        pickle.dump(obj, f)

    with open("./pickles/eccentricity.pickle", "wb") as f:
        temp = ig.Graph.eccentricity(G)
        obj = dict(zip(nx_ids, temp))
        pickle.dump(obj, f)

    with open("./pickles/pagerank.pickle", "wb") as f:
        temp = ig.Graph.pagerank(G)
        obj = dict(zip(nx_ids, temp))
        pickle.dump(obj, f)
