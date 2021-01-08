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

