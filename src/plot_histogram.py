import matplotlib.pyplot as plt
import pandas as pd

# plot histograms of features for each role
# plots are saved

def plot_histogram(df):

    for i in range(8):
        # specify nodes that are assigned to a role
        result = df[df['role'] == 'role_' + str(i)]
        result = result.reset_index()
        result['index'] = result.index
        # print(result.value_counts())

        plt.title('Betweenness of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("betweenness centrality", fontsize=15)
        plt.hist(result.betweenness, bins=200)
        plt.savefig('./plots/betweenness/histogram/role_' + str(i))
        plt.close()

        plt.title('Closeness of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("closeness centrality", fontsize=15)
        plt.hist(result.closeness, bins=200)
        plt.savefig('./plots/closeness/histogram/role_' + str(i))
        plt.close()

        plt.title('Clustering Coefficient of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("clustering coefficient", fontsize=15)
        plt.hist(result.clustering, bins=200)
        plt.savefig('./plots/clustering/histogram/role_' + str(i))
        plt.close()

        plt.title('Degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("degree", fontsize=15)
        plt.hist(result.degree, bins=200)
        plt.savefig('./plots/degree/histogram/role_' + str(i))
        plt.close()

        plt.title('Eccentricity of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("eccentricity", fontsize=15)
        plt.hist(result.eccentricity, bins=200)
        plt.savefig('./plots/eccentricity/histogram/role_' + str(i))
        plt.close()

        plt.title('Eigenvector centrality of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("eigenvector centrality", fontsize=15)
        plt.hist(result.eigenvector, bins=200)
        plt.savefig('./plots/eigenvector/histogram/role_' + str(i))
        plt.close()

        plt.title('In-degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("in-degree", fontsize=15)
        plt.hist(result.indegree, bins=200)
        plt.savefig('./plots/indegree/histogram/role_' + str(i))
        plt.close()

        plt.title('Out-degree of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("out-degree", fontsize=15)
        plt.hist(result.degree, bins=200)
        plt.savefig('./plots/outdegree/histogram/role_' + str(i))
        plt.close()

        plt.title('PageRank of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("pagerank", fontsize=15)
        plt.hist(result.pagerank, bins=200)
        plt.savefig('./plots/pagerank/histogram/role_' + str(i))
        plt.close()

        plt.title('Shell index of Nodes assigned role_' + str(i), fontsize=18)
        plt.xlabel("nodes", fontsize=15)
        plt.ylabel("shell index", fontsize=15)
        plt.hist(result.shellindex, bins=200)
        plt.savefig('./plots/shellindex/histogram/role_' + str(i))
        plt.close()


# plot a gaussian fit curve
# mu, sigma = scipy.stats.norm.fit(data)
# best_fit_line = scipy.stats.norm.pdf(bins, mu, sigma)
