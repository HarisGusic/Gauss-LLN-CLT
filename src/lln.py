import numpy as np; from numpy import *
import numpy.random as rnd
import scipy.stats as stats
import matplotlib.pyplot as plt

from shared import *

def gen_rnd_sequence(N_sekv, N_realiz, tip, mean=0, std=1):
    if tip == 'uniform':
        return rnd.uniform(mean - std*sqrt(3), mean + std*sqrt(3), (N_realiz, N_sekv))
    elif tip == 'exponential':
        return rnd.exponential(std, (N_realiz, N_sekv))
    elif tip == 'normal':
        return rnd.normal(mean, std, (N_realiz, N_sekv))
    elif tip == 'normal_converging_var':
        X_n = empty((N_realiz, N_sekv))
        for j in range(N_sekv):
            X_n[:, j] = rnd.normal(mean, std * (1 - exp(-(j+1))), N_realiz)
        return X_n
    elif tip == 'normal_diverging_var':
        X_n = empty((N_realiz, N_sekv))
        for j in range(N_sekv):
            X_n[:, j] = rnd.normal(mean, std * (j+1), N_realiz)
        return X_n

def gen_pdf(x, tip, mean, std):
    if tip == 'uniform':
        return stats.uniform.pdf(x, mean-std*sqrt(3), 2 * std * sqrt(3))
    elif tip == 'exponential':
        return stats.expon.pdf(x, 0, std)
    elif tip == 'normal':
        return stats.norm.pdf(x, mean, std)

def histogram(X, bins=10):
    # Određivanje raspona vrijednosti
    a = min(X); b = max(X)
    # Širina intervala za svaku "korpu"
    dx = (b - a) / bins
    hist = zeros(bins)
    for i in range(len(X)):
        k = int((X[i]-a)/dx)
        if k < len(hist):
            hist[k] += 1
        else: # Uslijed numericke nepreciznosti može biti van opsega
            hist[k-1] += 1
    return hist, linspace(a, b, bins), dx

# N_sekv - velicina sekvence
# N_realiz - broj realizacija koje se prikazuju
def plot_lln(X_n, mean, plot_range=[-2, 2], colored=True):
    N_realiz, N_sekv = X_n.shape

    # Racunanje sekvence srednjih vrijednosti uzoraka
    S_n = sample_means(X_n)
    n = arange(1, N_sekv+1)
    n_multi = repeat(n.reshape(N_sekv, 1), N_realiz, axis=1)
    
    # Crtanje
    plt.ylim(mean * array([1, 1]) + plot_range)
    plt.plot(n_multi, S_n.T, c=None if colored else 'k')
    plt.plot([n[0], n[-1]], [mean, mean],
             label='Ocekivanje $\mu$', c='k' if colored else 'red')
    plt.legend(); plt.xlabel('$n$')

def plot_hist(tip, N, bins=10):
    
    # Generisanje slucajne varijable i histograma
    X = gen_rnd_sequence(N, 1, tip, 0, 1)[0]
    hist, x, dx = histogram(X, bins)
    
    # Prikaz histograma
    bars = plt.bar(x, hist / (N*dx), width=dx,
                   align='edge', color='wheat', label='Histogram')
    for bar in bars:
        bar.set_edgecolor('sandybrown')
        bar.set_linewidth(2.6)

    # Prikaz PDF
    x = arange(-4, 4, 0.1)
    plt.plot(x, gen_pdf(x, tip, 0, 1), c='k', label='$p_X(x)$')
    plt.legend(); plt.xlabel('$x$'); plt.yticks([], [])
