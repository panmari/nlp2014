import numpy as np
from helpers import latexify_matrix
from math import log

#exercise b)
freq_string = """2 36 100;
		 78 45 5;
		 10 30 6;
		11 32 23;
		5 29 0
"""
query = np.matrix("3 2 5 4 2", dtype=np.float)

# exercise a)
# freq_string = """20 21 3;
# 36 100 23;
# 90 100 12;
# 75 3 67;
# 12 57 34"""
# query = np.matrix([25, 40, 45, 10, 20], dtype=np.float)

freq = np.matrix(freq_string, dtype=np.float)
mt = (freq + 1) / freq.sum(axis=0)

query = query.transpose()
query_rf = (query + 1) / query.sum()
kld_matrix = np.zeros(mt.shape())
for row in range(5):
    for column in range(3):
        kld_matrix[row,column] = (query_rf[row] * np.log2(query_rf[row] / mt[row, column]))
print("Full kld matrix:")
print(kld_matrix)
print("Summed up over terms:")
print(kld_matrix.sum(axis=0))