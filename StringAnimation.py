import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

L = 2
PARTITIONS = 1000
PLUCK_POINT = 1
DISPLACEMENT = 0.2
C = 1
TIME_STEP = 0.001

def triangle_func(x):
    if x < PLUCK_POINT:
        return x/PLUCK_POINT * DISPLACEMENT
    else:
        return (2*PLUCK_POINT - x)/PLUCK_POINT * DISPLACEMENT


def find_next_yvals(y_last, y_cur):
  y_next = np.zeros(len(y_cur))
  for i in range(1, len(y_cur)-1):
    DELTA_X = L/PARTITIONS
    y_next[i] = (C**2 * TIME_STEP**2 / (DELTA_X ** 2)) * (y_cur[i-1] - 2*y_cur[i] + y_cur[i+1]) + 2*y_cur[i] - y_last[i]
  return y_next


x_vals = np.linspace(0, L, PARTITIONS)
y_cur = np.array([triangle_func(x) for x in x_vals])
y_last = np.array(y_cur)
   


fig, ax = plt.subplots()
# plt.tight_layout()
plt.rcParams["animation.html"] = "jshtml" 
plt.rcParams['figure.dpi'] = 60
plt.ioff()

string_plot = plt.plot(x_vals, y_cur)

def animate(frame):
    y_next = find_next_yvals(y_last, y_cur)
    y_last = y_cur
    y_cur = y_next

    # make a small change to the object
    # string_plot.set_ydata(y_cur)
    # return string_plot,
    plt.plot(x_vals, y_cur)

animation = FuncAnimation(fig, animate, frames=range(100))

plt.show()
