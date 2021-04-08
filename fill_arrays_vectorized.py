import numpy as np

x = np.linspace(-4, 4, 41)
y = np.array(list(1/(2*np.pi)**(.5))*np.exp(-.5*np.asarray(x)**2) for i in x)