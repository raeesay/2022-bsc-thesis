import pprint as pprint
import pickle
import networkx as nx
import numpy as np
import pandas as pd
from graphrole import RecursiveFeatureExtractor, RoleExtractor

# the (undirected) graph created here was thought out with roles in mind
# therefore any roles extracted should be exactly how we predicted when creating this graph

# create graph entity
g = nx.Graph()

# add nodes to graph
g.add_nodes_from([1, 19])

# create edges between nodes as planned
g.add_edges_from(
    [(1, 2), (1, 3), (1, 5), (1, 10), (1, 15),
     (2, 4), (3, 4), (5, 6), (5, 7), (5, 8), (5, 9),
     (10, 11), (10, 12), (10, 13), (10, 14),
     (15, 16), (15, 17), (15, 18), (15, 19)])


def compute_roles(g):
    # extract features using graphrole library
    feature_extractor = RecursiveFeatureExtractor(g)
    features = feature_extractor.extract_features()

    # assign node roles
    role_extractor = RoleExtractor(n_roles=None)
    role_extractor.extract_role_factors(features)
    node_roles = role_extractor.roles

    # pprint.pprint(node_roles)
    pickle.dump(node_roles, open("save.p", "wb"))
    return node_roles


load_roles = pickle.load(open("save.p", "rb"))
pprint.pprint(load_roles)

