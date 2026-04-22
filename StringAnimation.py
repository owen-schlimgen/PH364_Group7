import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

L = 2
PARTITIONS = 200
PLUCK_POINT = 1
DISPLACEMENT = 0.2
C = 1
TIME_STEP = 0.01

def triangle_func(x):
  if x < PLUCK_POINT:
    return x/PLUCK_POINT * DISPLACEMENT
  else:
    return (L - x)/(L - PLUCK_POINT) * DISPLACEMENT


def find_next_yvals(y_last, y_cur):
  y_next = np.zeros(len(y_cur))
  for i in range(1, len(y_cur)-1):
    DELTA_X = L/PARTITIONS
    y_next[i] = (C**2 * TIME_STEP**2 / (DELTA_X ** 2)) * (y_cur[i-1] - 2*y_cur[i] + y_cur[i+1]) + 2*y_cur[i] - y_last[i]
  return y_next


x_vals = np.linspace(0, L, PARTITIONS)
y_cur = np.array([triangle_func(x) for x in x_vals])
y_last = np.array(y_cur)

all_strings = [np.array(y_cur)]

for t in range(500):
  y_cur, y_last = find_next_yvals(y_last, y_cur), y_cur
  all_strings.append(np.array(y_cur))


fig, ax = plt.subplots()
# plt.tight_layout()
plt.rcParams["animation.html"] = "jshtml" 
plt.rcParams['figure.dpi'] = 60
plt.ioff()

string_plot, = plt.plot(x_vals, y_cur)
plt.ylim(ymin=-5/4*DISPLACEMENT, ymax=5/4*DISPLACEMENT)

def animate(frame):
  string_plot.set_ydata(frame)
  return string_plot,

FuncAnimation(fig, animate, frames=all_strings, blit=True, interval = 10)
