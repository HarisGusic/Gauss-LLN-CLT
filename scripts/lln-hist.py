#!/usr/bin/env python3

from lln import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

rnd.seed(1) # Always generate the same plot

plt.figure()
plot_hist('normal', 100, 10)
savefig('lln_hist_1')

plt.figure()
plot_hist('normal', 1000, 30)
savefig('lln_hist_2')

plt.figure()
plot_hist('normal', 10000, 80)
savefig('lln_hist_3')
