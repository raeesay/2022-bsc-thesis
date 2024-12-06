import matplotlib.pyplot as plt
import pandas as pd


# plot scatterplots of features for each role
# plots are saved
def plot_scatter(df):

    for i in range(8):
        # specify nodes that are assigned to a role
        result = df[df['role'] == 'role_' + str(i)]
        result = result.reset_index()
        result['index'] = result.index
        # print(result.value_counts())
        
        plt.title('Betweenness of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("betweenness centrality", fontsize=15)
        plt.plot(result.betweenness, '.', alpha=0.3)
        plt.savefig('./plots/betweenness/scatter/role_' + str(i))
        plt.close()

        plt.title('Closeness of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("closeness centrality", fontsize=15)
        plt.plot(result.closeness, '.', alpha=0.3)
        plt.savefig('./plots/closeness/scatter/role_' + str(i))
        plt.close()

        plt.title('Clustering Coefficient of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("clustering coefficient", fontsize=15)
        plt.plot(result.clustering, '.', alpha=0.3)
        plt.savefig('./plots/clustering/scatter/role_' + str(i))
        plt.close()

        plt.title('Degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("degree", fontsize=15)
        plt.plot(result.degree, '.', alpha=0.3)
        plt.savefig('./plots/degree/scatter/role_' + str(i))
        plt.close()

        plt.title('Eccentricity of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("eccentricity", fontsize=15)
        plt.plot(result.eccentricity, '.', alpha=0.3)
        plt.savefig('./plots/eccentricity/scatter/role_' + str(i))
        plt.close()

        plt.title('Eigenvector centrality of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("eigenvector centrality", fontsize=15)
        plt.plot(result.eigenvector, '.', alpha=0.3)
        plt.savefig('./plots/eigenvector/scatter/role_' + str(i))
        plt.close()

        plt.title('In-degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("in-degree", fontsize=15)
        plt.plot(result.indegree, '.', alpha=0.3)
        plt.savefig('./plots/indegree/scatter/role_' + str(i))
        plt.close()

        plt.title('Out-degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("out-degree", fontsize=15)
        plt.plot(result.degree, '.', alpha=0.3)
        plt.savefig('./plots/outdegree/scatter/role_' + str(i))
        plt.close()

        plt.title('PageRank of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("pagerank", fontsize=15)
        plt.plot(result.pagerank, '.', alpha=0.3)
        plt.savefig('./plots/pagerank/scatter/role_' + str(i))
        plt.close()

        plt.title('Shell index of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("shell index", fontsize=15)
        plt.plot(result.shellindex, '.', alpha=0.3)
        plt.savefig('./plots/shellindex/scatter/role_' + str(i))
        plt.close()


