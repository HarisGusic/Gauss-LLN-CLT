#!/usr/bin/env python3

from clt import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())
rc('font', size=18)

plt.figure()
plot_binomial(1)
savefig('clt_binom_1')

plt.figure()
plot_binomial(2)
savefig('clt_binom_2')

plt.figure()
plot_binomial(3)
savefig('clt_binom_3')

plt.figure()
plot_binomial(8)
savefig('clt_binom_8')

plt.figure()
plot_binomial(50)
savefig('clt_binom_50')
