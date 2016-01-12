# priklad poslal Filip Matzner, dekujte jemu :)

# nasledujici funkce slouzi pro vykreslovani a uprav grafu v ipython noteboooku za behu
import random
import numpy as np

# nastavte matplotlib na backend notebook
import matplotlib.pyplot as plt
%matplotlib notebook

# vytvorte graf
plot = plt.subplots(1,1)

# funkce pro pridani noveho mereni do grafu
def updatePlot(plot, new_data):
  fig, ax = plot
  if len(ax.lines):
    xdata = ax.lines[0].get_xdata()
    xdata = np.append(xdata, len(xdata))
    if len(xdata) > 5000:
      xdata = xdata[-5000:]
    ydata = ax.lines[0].get_ydata()
    ydata = np.append(ydata, new_data)
    if len(ydata) > 5000:
      ydata = ydata[-5000:]
    ax.set_xlim(0, np.max(xdata))
    ax.set_ylim(0, np.max(ydata))
    ax.lines[0].set_xdata(xdata)
    ax.lines[0].set_ydata(ydata)
  else:
    ax.plot([0], [new_data])
  fig.canvas.draw()

# priklad pouziti
for i in range(500):
  updatePlot(plot, random.randint(0, i))