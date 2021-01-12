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

def gen_pdf(x, tip, mean, std):
    if tip == 'uniform':
        return stats.uniform.pdf(x, mean-std*sqrt(3), 2 * std * sqrt(3))
    elif tip == 'exponential':
        return stats.expon.pdf(x, 0, std)
    elif tip == 'normal':
        return stats.exp.normal(x, mean, std)

# N_sekv - veličina sekvence
# N_realiz - broj realizacija koje se prikazuju
def plot_lln(X_n, mean, plot_range=[-2, 2], colored=True):
    N_realiz, N_sekv = X_n.shape

    # Računanje sekvence srednjih vrijednosti uzoraka
    S_n = sample_means(X_n)
    n = arange(1, N_sekv+1)
    n_multi = repeat(n.reshape(N_sekv, 1), N_realiz, axis=1)
    
    # Crtanje
    plt.ylim(mean * array([1, 1]) + plot_range)
    plt.plot(n_multi, S_n.T, c=None if colored else 'k')
    plt.plot([n[0], n[-1]], [mean, mean],
             label='Očekivanje $\mu$', c='k' if colored else 'red')
    plt.legend(); plt.title('Realizacije sekvence $\{S_n\}$')
