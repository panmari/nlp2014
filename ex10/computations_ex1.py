import numpy as np
from helpers import latexify_matrix

#exercise b)
freq_string = """2 36 100;
		 78 45 5;
		 10 30 6;
		11 32 23;
		5 29 0
"""
freq = np.matrix(freq_string)
mt = freq/freq.sum(axis=0)
query = np.matrix("3 2 5 4 2")

# exercise a) relative frequencies taken from somewhere else

mt = np.matrix([[ 0.08583691,  0.0747331 ,  0.02158273],
        [ 0.15450644,  0.35587189,  0.16546763],
        [ 0.38626609,  0.35587189,  0.08633094],
        [ 0.32188841,  0.01067616,  0.48201439],
        [ 0.05150215,  0.20284698,  0.24460432]])
query = np.matrix([25, 40, 45,10,20])

query = query.transpose()
query_rf = query/query.sum()
means = [mt[i].mean() for i in range(5)]
stds = [mt[i].std() for i in range(5)]

zscore = np.zeros([5,3])

for row in range(5):
    for column in range(3):
        zscore[row,column] = (mt[row,column] - mt[row].mean())/ mt[row].std()

query_zscore = np.zeros([5,1])
for row in range(5):
	query_zscore[row,0] = (query_rf[row,0] - mt[row].mean())/ mt[row].std()

# todo: somehow unify zscore and query_zscore here and print it
print('Z scores authors:')
print(latexify_matrix(zscore))	

abs_diff = abs(zscore - query_zscore)
print('absolute diff:')
print(latexify_matrix(abs_diff))	

diff_author = abs_diff.sum(axis=0)/abs_diff.shape[0]
