#!/usr/bin/env python3

from clt import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

rc('font', size=16)

plt.figure()
plot_degenerate([1, 5, 30])
savefig('clt_degen')
