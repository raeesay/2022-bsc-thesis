import framework_test as framework
import networkx as nx
import numpy as np
import pandas as pd

# the (undirected) graph created here was thought out with roles in mind
# therefore any roles extracted should be exactly how we predicted when creating this graph

# create graph entity
g = nx.Graph()

# add nodes to graph
g.add_nodes_from([1, 19])

# create edges between nodes as planned
g.add_edges_from(
    [(1, 2),(1, 3),(1, 5),(1, 10),(1, 15),
     (2, 4),(3, 4),(5, 6),(5, 7),(5, 8),(5, 9),
     (10, 11),(10, 12),(10, 13),(10, 14),
     (15, 16),(15, 17),(15, 18),(15, 19)])


def compute_data(g):
    # compute roles and statistics
    framework.graph_statistics(g)

compute_data(g)
