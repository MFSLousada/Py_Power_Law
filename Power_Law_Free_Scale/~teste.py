_author__ = 'user'
from IPython.core.display import Image
import collections


def plot_basics(counter, data_inst, fig, units):
    from powerlaw import plot_pdf, Fit, pdf
    annotate_coord = (-.4, .95)
    ax = fig.add_subplot(n_graphs, n_data, data_inst)

    ax.plot(counter.keys(), counter.values(), marker='o', linestyle='')

    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xlabel(units)


def plot_fit_pdf(data, data_inst, fig, units):
    from powerlaw import plot_ccdf, Fit, pdf, plot_pdf
    annotate_coord = (-.4, .95)
    ax = fig.add_subplot(n_graphs, n_data, data_inst)

    fit = Fit(data, discrete=True)
    fit.plot_pdf(ax=ax, color='r')
    fit.power_law.plot_pdf(ax=ax, linestyle=':', color='g')
    fit.exponential.plot_pdf(ax=ax, linestyle=':', color='b')

    ax.set_ylim(0.00000001, 1)
    # ax.set_yticks(ax3.get_yticks()[::2])
    # ax.set_xlim(ax1.get_xlim()

    # plot_ccdf(data, ax=ax, color='r', linewidth=.5)

    ax.set_xlabel(units)

def plot_fit_ccdf(data, data_inst, fig, units):
    from powerlaw import plot_ccdf, Fit, pdf, plot_pdf
    annotate_coord = (-.4, .95)
    ax = fig.add_subplot(n_graphs, n_data, data_inst)

    fit = Fit(data, discrete=True)
    fit.plot_ccdf(ax=ax, color='r')
    fit.power_law.plot_ccdf(ax=ax, linestyle=':', color='g')

    fit = Fit(data, discrete=True, xmin=1)
    # plot_ccdf(data, ax=ax, color='r')
    fit.power_law.plot_ccdf(ax=ax, linestyle='--', color='b')
    # fit.exponential.plot_ccdf(ax=ax, linestyle=':', color='b')

    if data_inst == 1:
        ax.set_ylim(0.00001, 1)
    else:
        ax.set_ylim(0.001, 1)
    # ax.set_yticks(ax3.get_yticks()[::2])
    # ax.set_xlim(ax1.get_xlim()

    # plot_ccdf(data, ax=ax, color='r', linewidth=.5)

    ax.set_xlabel(units)
from numpy import *

"""print (data)"""
a =loadtxt("areas_a.txt", dtype='float') #/10**3
b =loadtxt("areas_a.txt", dtype='float')
c =loadtxt("areas_a.txt", dtype='float')


n_data = 3
n_graphs = 1
f = figure(figsize=(8,4))

data = a
data_inst = 1
units = 'Areas frequency a'
plot_basics(collections.Counter(a), data_inst, f, units)

data_inst = 2
#data = city
#units = 'City Population'
data = b
units = 'Areas frequency b'
plot_basics(collections.Counter(b), data_inst, f, units)

data = c
data_inst = 3
units = 'Areas frequency c'
plot_basics(collections.Counter(c), data_inst, f, units)

f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.2)
f.savefig('basics_frequ.png', bbox_inches='tight')
plt.close()

Image(filename='basics_frequ.png')

n_data = 3
n_graphs = 1
f = figure(figsize=(8,4))

data = a
data_inst = 1
units = 'Areas frequency a'
plot_basics_ccdf(data, data_inst, f, units)

data_inst = 2
#data = a
#units = 'sqm'
data = b
units = 'Areas frequency b'
plot_basics_ccdf(data, data_inst, f, units)

data = c
data_inst = 3
units = 'Areas frequency c'
plot_basics_ccdf(data, data_inst, f, units)

f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.2)
f.savefig('basics_ccdf.png', bbox_inches='tight')
plt.close()

Image(filename='basics_ccdf.png')






