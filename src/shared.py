import numpy as np; from numpy import *; import numpy.random as rnd

def pdf_mean(f, p):
    return sum(f * p)
def pdf_mean_square(x, p):
    return pdf_mean(x**2, p)
def pdf_var(x, p):
    return pdf_mean_square(x,p) - pdf_mean(x,p)**2
def integral(x, f):
    return sum((f + roll(f, -1))[:-1] * diff(x)) / 2
def convolve_n(f, n):
    g = f
    for i in range(n):
        g = convolve(g, f)
    return g
def gen_fun(tip='rect'):
    if tip == 'rect':
        f = pad(ones(50), (25,25))
    elif tip == 'noise_uniform':
        f = pad(rnd.uniform(0,1,50), (25,25))
    elif tip == 'noise_exp':
        f = pad(rnd.exponential(1,50), (25,25))
    elif tip == 'exp':
        f = pad(exp(-0.1*arange(50)), (30,20))
    elif tip == 'exp2':
        f = exp(-0.1*arange(40))
        f = pad(concatenate((f, flip(f)/2)), (10,10))
    return f / sum(f)

def sample_means(X_n):
    N_realiz, N_sekv = X_n.shape
    S_n = empty((N_realiz, N_sekv))
    for j in range(0, N_sekv):
        S_n[:,j] = mean(X_n[:, 0:j+1], axis=1)
    return S_n
