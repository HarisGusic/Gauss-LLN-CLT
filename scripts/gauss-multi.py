#!/usr/bin/env python3

from gauss import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())
rc('font', size=16)

# Standardna normalna raspodjela
plt.figure()
plot_multivariate_gaussian([0,0], [[1,0],[0,1]], 100);
#plt.tight_layout()
savefig('gauss_multi_std')

# Raširena po y osi
plt.figure()
plot_multivariate_gaussian([0,0], [[1,0],[0,5]], 100);
#plt.tight_layout()
bbox_inches='tight'
savefig('gauss_multi_y')

# Pozitivno korelirane
plt.figure()
plot_multivariate_gaussian([0,0], [[1,0.6],[0.6,1]], 100);
#plt.tight_layout()
savefig('gauss_multi_corr+')

# Negativno korelirane
plt.figure()
plot_multivariate_gaussian([0,0], [[1,-0.6],[-0.6,1]], 100);
#plt.tight_layout()
savefig('gauss_multi_corr-')

# Maksimalno korelirane
plt.figure()
plot_multivariate_gaussian([0,0], [[1,0.97],[0.97,1]], 200);
#plt.tight_layout()
savefig('gauss_multi_corr1')

# Negativno korelirane sa velikom varijansom po x
plt.figure()
plot_multivariate_gaussian([0,0], [[4,-1.2],[-1.2,1]], 100);
#plt.tight_layout()
savefig('gauss_multi_xcorr-')

