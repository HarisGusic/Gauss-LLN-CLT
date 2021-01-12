#!/usr/bin/env python3

from clt import *
import os
exec(open(os.path.dirname(__file__) + '/common_plot.py').read())

rc('font', size=26)

# Helper function - Input function
def plotf(path):
    global f
    plt.figure()
    plot_fun(f)
    savefig(path)

# Helper function - Output convolution
def plotg(n, path):
    global f
    plt.figure()
    plot_convolution(f, n)
    savefig(path)

f = gen_fun('rect')
plotf(   'clt_conv_rect')
plotg(1, 'clt_conv_rect_1')
plotg(2, 'clt_conv_rect_2')

f = gen_fun('noise_uniform')
plotf(   'clt_conv_noise')
plotg(1, 'clt_conv_noise_1')
plotg(2, 'clt_conv_noise_2')

f = gen_fun('exp2')
plotf(   'clt_conv_exp')
plotg(1, 'clt_conv_exp_1')
plotg(9, 'clt_conv_exp_2')
