_author__ = 'user'
from numpy import *
import powerlaw

data = loadtxt("areas_n.txt", dtype='float')

"""print (data)"""

results = powerlaw.Fit(data)

print(results.power_law.alpha)
print(results.power_law.xmin)
R, p = results.distribution_compare('power_law', 'lognormal')
import set
