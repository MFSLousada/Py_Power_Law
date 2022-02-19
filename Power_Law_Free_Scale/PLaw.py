_author__ = 'user'
from numpy import *

from igraph import *

data = loadtxt("areas_c", dtype='float')

"""print (data)"""

result = power_law_fit(data)

print(result)






