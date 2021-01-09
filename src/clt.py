import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np; from numpy import *

def plot_binomial(n, approx='Auto'):
    k = range(n+1)
    pmf = stats.binom.pmf(k, n, 0.5) # Generisanje raspodjele
    
    ax = plt.axes()
    import matplotlib.ticker as tck
    ax.xaxis.set_major_locator(tck.MaxNLocator(integer=True)) #Estetika
    
    if approx == 'True' or (approx == 'Auto' and n > 10):
        plt.plot(stats.norm.pdf(k, n/2, sqrt(n)/2),
                 c='orangered', label='DeMoivre-\nLaplace')
    plt.stem(pmf, basefmt=' ', label='$p_K(k)$')
        
    # Anotacija
    plt.xlabel('$k$')
    plt.legend(loc='upper right', bbox_to_anchor=(0.99,0.92), framealpha=1)
