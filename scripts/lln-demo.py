#!/usr/bin/env python3

from lln import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

rnd.seed(1) # Always generate the same plot

X_n = gen_rnd_sequence(100, 3, 'normal', 0, 1)
plt.figure()
plot_lln(X_n, 0)
savefig('lln_demo_1')

X_n = gen_rnd_sequence(100, 3, 'normal', 0, 2)
plt.figure()
plot_lln(X_n, 0)
savefig('lln_demo_2')

X_n = gen_rnd_sequence(100, 50, 'normal', 0, 2)
plt.figure()
plot_lln(X_n, 0)
savefig('lln_demo_3')
