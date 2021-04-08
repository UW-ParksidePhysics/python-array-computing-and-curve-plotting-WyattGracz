import numpy as np

step = (8/40)
x = []
y = []

x = np.array(x)
y = np.array(y)

for i in range(0,41):
  x = np.append(x, -4 + step*i)
  y=np.append(y,(1/(2*np.pi)**(.5))*np.exp(-.5*np.asarray(x)**2))
