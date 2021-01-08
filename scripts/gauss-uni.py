#!/usr/bin/env python3

from gauss import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

# Standardna normalna raspodjela
plt.figure()
plot_gaussian(0, 1, 200);
plt.savefig('_build/img/gauss_uni_std.pdf', format='pdf', pad_inches=0,
    bbox_inches='tight')

# Promjena srednje vrijednosti
plt.figure()
plot_gaussian(-2, 1, 200);
plt.savefig('_build/img/gauss_uni_deltamean.pdf', format='pdf', pad_inches=0,
    bbox_inches='tight')

# Promjena varijanse
plt.figure()
plot_gaussian(-2, 4, 200);
plt.savefig('_build/img/gauss_uni_deltavar.pdf', format='pdf', pad_inches=0,
    bbox_inches='tight')
