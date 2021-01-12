#!/usr/bin/env python3

from gauss import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())
rc('font', size=24)

# Standardna normalna raspodjela
plt.figure()
plot_gaussian(0, 1, 200);
savefig('gauss_uni_std')

# Promjena srednje vrijednosti
plt.figure()
plot_gaussian(-2, 1, 200);
savefig('gauss_uni_deltamean')

# Promjena varijanse
plt.figure()
plot_gaussian(-2, 4, 200);
savefig('gauss_uni_deltavar')
