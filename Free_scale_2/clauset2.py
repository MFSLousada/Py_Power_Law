author__ = 'user'
from numpy import *
from mpmath import*
from scipy import *
from matplotlib import *
from scipy.optimize import*
from sys import float_info
import powerlaw


data = loadtxt("areas_c.txt", dtype='float')

"""print (data)"""

results = powerlaw.Fit(data)
print results.power_law.alpha
print results.power_law.xmin
R, p = results.distribution_compare('power_law', 'lognormal')

print (R, p)
