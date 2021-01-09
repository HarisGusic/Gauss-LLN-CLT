#!/usr/bin/env python3

from clt import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

plt.figure()
plot_binomial(1)
plt.savefig('_build/img/clt_binom_1.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')

plt.figure()
plot_binomial(2)
plt.savefig('_build/img/clt_binom_2.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')

plt.figure()
plot_binomial(3)
plt.savefig('_build/img/clt_binom_3.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')

plt.figure()
plot_binomial(8)
plt.savefig('_build/img/clt_binom_8.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')

plt.figure()
plot_binomial(50)
plt.savefig('_build/img/clt_binom_50.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')
