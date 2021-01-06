from shared import *
import matplotlib.pyplot as plt


def test_multivariate_gaussian():
    N = 100
    low = -2; high = 4
    x = linspace(low, high, N)
    _X,_Y = meshgrid(x, x)
    X = _X.flatten(); Y = _Y.flatten()
    mean = [1,1]
    cov = [[1, 0.5], [0.5, 1]]

    p = multivariate_gaussian(stack((X,Y)), mean, cov)

    fig = plt.figure()
    ax = fig.add_subplot(1,2,1, projection='3d')
    ax.plot_surface(_X, _Y, p.reshape(N,N), cmap='hot')
    ax.plot3D(X, high*ones_like(X),
              gaussian(X, mean[0], cov[0][0]) / sqrt(2*pi*linalg.det(cov)))
    ax.plot3D(low*ones_like(Y), Y,
              gaussian(Y, mean[1], cov[1][1]) / sqrt(2*pi*linalg.det(cov)))
    plt.xlabel('x'); plt.ylabel('y')
    
    ax = fig.add_subplot(1,2,2, aspect=1)
    ax.contourf(_X, _Y, p.reshape(N,N), 50, cmap='hot', antialiased=False)
    plt.show()
    print(p.sum() * 0.06**2)
    print(pdf_mean(X, p) * (X[1] - X[0]), pdf_mean(Y, p) * (Y[1] - Y[0]))

def test_multivariate_gaussian3():
    mean = [0,0,0]
    x = linspace(-3, 3, 20)
    X,Y,Z = meshgrid(x,x,x)
    print(X.shape)
    X = X.flatten()
    Y = Y.flatten()
    Z = Z.flatten()
    
    cov = [[1,0,0],
           [0,1,0],
           [0,0,1]]
    multivariate_gaussian(stack(()))

test_multivariate_gaussian()
#test_multivariate_gaussian3()

