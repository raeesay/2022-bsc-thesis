import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import scipy.stats

df = pd.read_pickle('./pickles/df_merged.pickle')

# specify nodes that are assigned to a role
result = df[df['role'] == 'role_0']
result = result.reset_index()
result['index'] = result.index
# print(result.value_counts())
data = result.closeness

_, bins, _ = plt.hist(data, 200, density=1, alpha=0.5)
mu, sigma = scipy.stats.norm.fit(data)
best_fit_line = scipy.stats.norm.pdf(bins, mu, sigma)
plt.plot(bins, best_fit_line)

plt.title('Closeness of Nodes assigned role_0', fontsize=18)
plt.ylabel("nodes", fontsize=15)
plt.xlabel("closeness centrality", fontsize=15)
plt.savefig('./plots/closeness/histogram/closeness')
plt.close()
  