import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np; from numpy import *
from shared import *
from gauss import *
################################################################################
"""
    Prikazivanje binomne raspodjele za zadani parametar `n`. Parametar
    `approx` odredjuje da li ce biti prikazana aproksimacija sekvence Gaussovom
    funkcijom i moze imati sljdece vrijednosti:

        - 'True', aproksimacija ce biti prikazana
        - 'False', aproksimacija nece biti prikazana
        - 'Auto' (default), aproksimacija ce biti prikazana ako je n>10
"""
def plot_binomial(n, approx='Auto'):
    k = range(n+1)
    pmf = stats.binom.pmf(k, n, 0.5) # Generisanje raspodjele
    
    ax = plt.axes()
    import matplotlib.ticker as tck
    ax.xaxis.set_major_locator(tck.MaxNLocator(integer=True)) #Estetika
    
    if approx == 'True' or (approx == 'Auto' and n > 10):
        plt.plot(stats.norm.pdf(k, n/2, sqrt(n)/2),
                 c='orangered', label='De Moivre-\nLaplace')
    plt.stem(pmf, basefmt=' ', label='$p_K(k)$')
        
    # Anotacija
    plt.xlabel('$k$')
    plt.legend(loc='upper right', bbox_to_anchor=(0.99,0.92), framealpha=1)
################################################################################
"""
    Graficki prikaz funkcije `f` definirane na intervalu [-50, 49], uz korak
    diskretizacije 1.
"""
def plot_fun(f):
    plt.plot(arange(-50, 50), f)
    plt.yticks([], [])
    plt.tight_layout()
    plt.xlabel('$x$'); plt.ylabel('$f(x)$')
################################################################################
"""
    Graficki prikaz konvolucije funkcije `f` sa samom sobom `n` puta, kao i
    aproksimacije Gaussovom funkcijom.
"""
def plot_convolution(f, n):
    # Formiranje normalizovane konvolucije
    g = convolve_n(f, n)
    g = g / sum(g)
    
    # Formiranje ulazne varijable
    N = len(g)
    x = array(range(N)) - N/2
    
    # Aproksimacija Gauss-ovom funkcijom
    g_approx = approx_gaussian(x, g)
    
    # Plot
    plt.plot(x, g_approx, label='$\\widetilde{g}_n(x)$', c='orangered')
    plt.plot(x, g, label='$g_n(x)$');
    # Anotacija i estetika
    plt.yticks([], [])
    plt.xlabel('$x$'); plt.ylabel('$g(x)$'); plt.legend()
################################################################################
"""
    Vizualizacija degenerisanja Gaussove raspodjele sekvence srednjih
    vrijednosti uzoraka standardno normalno distribuirane sekvence.
    Vizualizacija se prikazuje za svaku vrijednost n unutar liste `n_seq`.
"""
def plot_degenerate(n_seq):
    x = linspace(-2.5, 2.5, 100)
    
    for i in n_seq:
        y = stats.norm.pdf(x, 0, 1/sqrt(i))
        plt.plot(x, y, label='$n=' + str(i) + '$')
        
    # Anotacija i estetika
    plt.legend()
    plt.xlabel('$x$')
    plt.ylabel('$\widetilde{p_{S_n}}(x)$'); plt.yticks([], [])
