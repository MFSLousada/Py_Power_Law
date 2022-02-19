_author__ = 'user'
from numpy import *
from scipy import*
from powerlaw.regression import estimate_parameters, goodness_of_fit


data = loadtxt("O1", dtype='float')

"""print (data)"""

(xmin, alpha, ks_statistics) = estimate_parameters(data)

p_value = goodness_of_fit(series, xmin, alpha, ks_statistics)

print "p_value"