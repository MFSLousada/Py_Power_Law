from numpy import *

from igraph import *

data = loadtxt("areas1.txt", dtype='float')

"""print (data)"""

result = power_law_fit(data)

print(result)
