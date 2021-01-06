import numpy as np; from numpy import *

def pdf_mean(f, p):
    return (f * p).sum()
def pdf_mean_square(x, p):
    return pdf_mean(x**2, p)
def pdf_var(x, p):
    return pdf_mean_square(x,p) - pdf_mean(x,p)**2

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


def cov_elipsa(mean, cov, N=50):
    a = cov[0][0]; b = cov[0][1]; c = cov[1][1]
    A = (a+c) / 2
    B = sqrt((a-c)**2/4 + b**2)
    l1 = A + B
    l2 = A - B
    if isclose(b, 0) and a >= c: theta = 0
    elif isclose(b, 0) and a < c: theta = pi/2
    else: theta = arctan2(l1 - a, b)
    t = linspace(0, 2*pi, 50)
    x = sqrt(l1) * cos(theta) * cos(t) - sqrt(l2) * sin(theta) * sin(t) + mean[0]
    y = sqrt(l1) * sin(theta) * cos(t) + sqrt(l2) * cos(theta) * sin(t) + mean[1]
    dx = max(x) - min(x)
    dy = max(y) - min(y)
    return x, y, dx, dy
