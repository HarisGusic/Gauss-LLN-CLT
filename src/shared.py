import numpy as np; from numpy import *; import numpy.random as rnd
################################################################################
"""
    Racunanje integrala za funkciju `f` definiranu u tackama iz vektora `x`.
    Vrijednosti vektora `x` ne moraju biti uniformo rasporedjene.
"""
def integral(x, f):
    return sum((f + roll(f, -1))[:-1] * diff(x)) / 2
################################################################################
"""
    Konvolucija funkcije `f` sa samom sobom `n` puta.
"""
def convolve_n(f, n):
    g = f
    for i in range(n):
        g = convolve(g, f)
    return g
################################################################################
"""
    Generisanje funkcije odredjenog tipa na osnovu parametra `tip`.

    Podrzane vrijednosti za parametar `tip`: "rect", "noise_uniform",
    "noise_exp", "noise_exp", "exp", "exp2".
"""
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
################################################################################
"""
    Racunanje sekvence srednjih vrijednosti uzoraka za sekvencu `X_n`.
"""
def sample_means(X_n):
    N_realiz, N_sekv = X_n.shape # Broj realizacija, duzina sekvence
    S_n = empty((N_realiz, N_sekv))
    for j in range(0, N_sekv):
        S_n[:,j] = mean(X_n[:, 0:j+1], axis=1)
    return S_n
