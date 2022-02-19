from scipy.stats import powerlaw

author__ = 'user'
from numpy import*
from scipy import *


data = loadtxt("areas_a.txt", dtype='float')

print (data)

"""print (data)"""
powerlaw.regression.estimate_parameters(data)