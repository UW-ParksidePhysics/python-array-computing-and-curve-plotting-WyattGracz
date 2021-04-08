import matplotlib.pyplot as plt
import numpy as np
def h(x):
  h = (1/(2*np.pi)**(.5))*np.exp(-.5*np.asarray(x)**2)
  return h

xlist=np.linspace(-4,4,41)
hlist=h(xlist)

plt.plot(xlist,hlist,'-',markerfacecolor='none')
plt.xlim(-4,4)
plt.title('Gaussian Plot')
plt.xlabel('x')
plt.ylabel('h(x)')