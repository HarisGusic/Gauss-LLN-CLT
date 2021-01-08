import numpy as np; from numpy import *
from shared import *

def gaussian(x, mean=0.0, var=1.0):
    return sqrt(exp(-(x-mean)**2 / var) / (2*pi*var))

def multivariate_gaussian(x, mean, cov):
    x = array(x); mean = array(mean); cov = array(cov)
    k = x.shape[0] # Broj varijabli
    n = x.shape[1] # Broj ulaznih koordinata
    
    # Provjera ulaznih parametara
    #if len(x.shape) != 1:
        #raise Exception('Neispravan vektor ulaznih promjenljivih x');
    #if shape(cov)[0] != shape(cov)[1] or any(cov != cov.T) or any(linalg.eig(cov) < 0):
        #raise Exception('Neispravna kovarijantna matrica')
    #TODO provjere
    
    inv_cov = matrix(linalg.inv(cov))
    inv_det = linalg.det(inv_cov)
    
    y = empty(n)
    for j in range(n):
        x_m = matrix(x)[:,j] - matrix(mean).T
        y[j] = sqrt(exp(- x_m.T * inv_cov * x_m).T * inv_det / (2*pi)**k)
    
    return y

# Aproksimacija Gauss-ovom funkcijom
def approx_gaussian(x, f):
    cijeli_integral = integral(x, f)
    f = f / cijeli_integral # Normalizacija integrala funkcije
    mean = integral(x, x*f)
    var = integral(x, x**2 * f)
    return gaussian(x, mean, var) * cijeli_integral

import matplotlib.pyplot as plt

def plot_gaussian(mean, var, N=100):
    x = linspace(-8, 8, N)
    p = gaussian(x, mean, var)
    val_at_var = gaussian(mean + var, mean, var) # Vrijednost raspodjele u tački x=var
    
    # Crtanje raspodjele
    plt.plot(x, p, label='$p_X(x)$')
    # Vizualizacija očekivane vrijednosti
    plt.plot([mean, mean], list(plt.ylim()), label='$\mu$')
    # Vizualizacija varijanse
    plt.annotate(xy=(mean, val_at_var), xytext=(mean+var, val_at_var),
                 text='', arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
    plt.plot([mean+0.1, mean+var-0.1], [val_at_var, val_at_var],
             linewidth=0.8, c='k', label='$\sigma$')
    
    plt.xlabel('$x$'); plt.legend()

def plot_multivariate_gaussian(mean, cov, N=100):
    # Generisanje vektora koordinata
    xlim = ylim = [-6, 6]
    x = linspace(xlim[0], xlim[1], N) # Vektori koji generišu
    y = linspace(ylim[0], ylim[1], N) # mrežu tačaka
    _X,_Y = meshgrid(x, y) # Mreža tačaka
    # Mreža tačaka se pretvara u niz uređenih parova
    X = _X.flatten(); Y = _Y.flatten()

    # Računanje raspodjele
    p = multivariate_gaussian(stack((X,Y)), mean, cov)
    
    fig = plt.figure(figsize=(4,8.7))
    ax = fig.add_subplot(2,1,1, projection='3d')
    
    # Crtanje raspodjele
    ax.plot_surface(_X, _Y, p.reshape(N,N), cmap='hot', alpha=1)
    
    # Crtanje marginalnih raspodjela
    ax.plot3D(X, ylim[1]*ones_like(X),
              gaussian(X, mean[0], cov[0][0]) * sqrt(cov[0][0]/(2*pi*linalg.det(cov))),
							c='orchid', label='$p_{X_1}(x_1)$')
    ax.plot3D(xlim[0]*ones_like(Y), Y,
              gaussian(Y, mean[1], cov[1][1]) * sqrt(cov[1][1]/(2*pi*linalg.det(cov))),
							c='dodgerblue', label='$p_{X_2}(x_2)$')
    
    # Anotacija
    ax.xaxis.set_rotate_label(False); ax.yaxis.set_rotate_label(False)
    plt.xlabel('$x_1$', rotation=0); plt.ylabel('$x_2$', rotation=0)
    plt.legend(bbox_to_anchor=(0.68,1.05))
    
    # Crtanje konturnog grafika
    ax = fig.add_subplot(2,1,2, aspect=1)
    ax.contourf(_X, _Y, p.reshape(N,N), 80, cmap='hot', antialiased=True)
    
    # Srednja vrijednost
    ax.scatter(mean[0], mean[1], c='k', label='Očekivanje')
    
    # Elipsa kovarijanse
    elipsa = cov_elipsa(mean, cov)
    ax.plot(elipsa[0], elipsa[1], label='Elipsa kovarijanse')
    plt.xlabel('$x_1$'); plt.ylabel('$x_2$', rotation=0);
    plt.legend(bbox_to_anchor=(1.02, 1.02))

