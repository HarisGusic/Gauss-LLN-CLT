import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
rc('font', size=18)

def savefig(path):
    plt.savefig('_build/img/' + path + '.pdf', format='pdf', pad_inches=0,
        bbox_inches='tight')
