import numpy as np; from numpy import *
from shared import *
import scipy.stats as stats
################################################################################
import scipy.optimize as opt
def approx_gaussian(x, f):
    # Nalazenje optimalnih parametara
    fun = lambda x, a, m, std: a * stats.norm.pdf(x, m, std)
    try:
        popt, pcov = opt.curve_fit(fun, x, f)
    except:
        raise Exception('Numericki problem prilikom' \
            'aproksimacije normalnom funkcijom')
    
    # Alternativni metod, ako prethodni zakaze
    if np.max(pcov) > 0.1: 
        cijeli_integral = integral(x, f)
        f = f / cijeli_integral # Normalizacija integrala funkcije
        mean = integral(x, x*f)
        var = integral(x, (x-mean)**2 * f)
        return stats.norm.pdf(x, mean, sqrt(var)) * cijeli_integral
    else:
        return fun(x, *popt)
################################################################################
def multivariate_gaussian(x, mean, cov):
    x = array(x); mean = array(mean); cov = array(cov)
    k = x.shape[0] # Broj varijabli
    n = x.shape[1] # Broj ulaznih koordinata
    
    inv_cov = matrix(linalg.inv(cov))
    inv_det = linalg.det(inv_cov)
    
    y = empty(n)
    for j in range(n):
        x_m = matrix(x)[:,j] - matrix(mean).T
        y[j] = sqrt(exp(- x_m.T * inv_cov * x_m).T
            * inv_det / (2*pi)**k)
    
    return y
################################################################################
import matplotlib.pyplot as plt
################################################################################
def plot_gaussian(mean, var, N=100):
    x = linspace(-8, 8, N)
    p = stats.norm.pdf(x, mean, sqrt(var))
    # Vrijednost raspodjele u tacki x=var
    val_at_var = stats.norm.pdf(mean + var, mean, sqrt(var)) 
    
    # Crtanje raspodjele
    plt.plot(x, p, label='$p_X(x)$')
    # Vizualizacija ocekivane vrijednosti
    plt.plot([mean, mean], list(plt.ylim()), label='$\mu$')
    # Vizualizacija varijanse
    plt.annotate(xy=(mean, val_at_var), xytext=(mean+var, val_at_var), text='',
                 arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
    plt.plot([mean+0.1, mean+var-0.1], [val_at_var, val_at_var],
             linewidth=0.8, c='k', label='$\sigma$')
    
    plt.xlabel('$x$'); plt.legend()
################################################################################
def plot_multivariate_gaussian(mean, cov, N=100):
    # Generisanje vektora koordinata
    xlim = ylim = [-6, 6]
    x = linspace(xlim[0], xlim[1], N) # Vektori koji generisu
    y = linspace(ylim[0], ylim[1], N) # mrezu tacaka
    _X,_Y = meshgrid(x, y) # Mreza tacaka
    # Mreza tacaka se pretvara u niz uredjenih parova
    X = _X.flatten(); Y = _Y.flatten()

    # Racunanje raspodjele
    p = multivariate_gaussian(stack((X,Y)), mean, cov)
    
    fig = plt.figure(figsize=(5,8.5))
    ax = fig.add_subplot(2,1,1, projection='3d')
    
    # Crtanje raspodjele
    ax.plot_surface(_X, _Y, p.reshape(N,N), cmap='hot', alpha=1)
    
    # Crtanje marginalnih raspodjela
    ax.plot3D(X, ylim[1]*ones_like(X),
              stats.norm.pdf(X, mean[0], sqrt(cov[0][0]))
                    * sqrt(cov[0][0]/(2*pi*linalg.det(cov))),
              c='orchid', label='$p_{X_1}(x_1)$')
    ax.plot3D(xlim[0]*ones_like(Y), Y,
              stats.norm.pdf(Y, mean[1], sqrt(cov[1][1]))
                    * sqrt(cov[1][1]/(2*pi*linalg.det(cov))),
              c='dodgerblue', label='$p_{X_2}(x_2)$')
    
    # Anotacija i estetika
    ax.xaxis.set_rotate_label(False); ax.yaxis.set_rotate_label(False)
    plt.xlabel('$x_1$', rotation=0); plt.ylabel('$x_2$', rotation=0)
    ax.set_zticklabels([])
    plt.legend(bbox_to_anchor=(0.68,1.05))
    
    # Crtanje konturnog grafika
    ax = fig.add_subplot(2,1,2, aspect=1)
    ax.contourf(_X, _Y, p.reshape(N,N), 80, cmap='hot', antialiased=True)
    
    # Srednja vrijednost
    ax.scatter(mean[0], mean[1], c='k', label='Ocekivanje')

    plt.legend(bbox_to_anchor=(1.02,1.02), loc='upper right')

