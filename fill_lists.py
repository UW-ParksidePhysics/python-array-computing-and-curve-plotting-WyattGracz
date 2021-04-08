import numpy as np
def h(x):
    return (1/(2*np.pi)**(.5))*np.exp(-.5*np.asarray(x)**2)

xlist=np.linspace(-4,4,41)
hlist=h(xlist)