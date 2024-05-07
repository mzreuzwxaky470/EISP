import numpy as np
from scipy.stats import spearmanr

# 
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([5,4.6,3.2,2.1,1.4])

# 
correlation, p_value = spearmanr(data1, data2)

print("Spearman correlation coefficient:", correlation)
print("P-value:", p_value)
