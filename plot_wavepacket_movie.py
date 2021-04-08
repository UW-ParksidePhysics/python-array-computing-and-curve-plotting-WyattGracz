import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import animation

plt.ion()

x=np.linspace(-6,6,1000)
t = 0 
f=np.exp(-(x-3*t)**2)*np.sin(3*np.pi*((x-3*t)))


plt.xlabel('X')
plt.ylabel('f(x,t)')

fig = plt.figure()
plt.axis(x[0], x[-1], -0.1, f_max)
lines = plt.plot([],[])
plt.xlabel('x')
plt.ylabel('f')

def init():
  lines[0].set_data([],[])
  return lines

def frame(args):
  frame_no, s , x, lines = args
  y = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*((x-3*t)))
  lines[0].set_data(x, y)
  return lines



anim = animation.FuncAnimation(fig, frame, interval = 150, init_func=init, blit=True)

