author__ = 'user'
from numpy import*
from scipy import *


data = loadtxt("areas_a.txt", dtype='float')

print (data)

"""print (data)"""

(xmin, alpha, ks_statistics) = estimate_parameters(data)

p_value = goodness_of_fit(series, xmin, alpha, ks_statistics)

print "p_value"

