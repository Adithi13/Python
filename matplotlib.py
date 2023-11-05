#to check the Matplotlib verion
import matplotlib
print(matplotlib.__version__)

#PyPlot = this is a sub module and usually imported underr plt
#say i want to draw a line in a diagram from position (0,0) to position (6,250)
import matplotlib.pyplot as plt
import numpy as np
x_axis = np.array([0,6])
y_axis = np.array([0,250])
plt.plot(x_axis,y_axis)
plt.show

