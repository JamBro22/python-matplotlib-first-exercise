# import modules
import matplotlib.pyplot as plt
import numpy as np

# create arrays with values for x and y axes
x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
y = np.array([220, 330, 190, 340, 410, 445, 415])

# mapping slope and intercept
m, b = np.polyfit(x, y, 1)

# creating best fit line
plt.plot(x, m*x + b)

# creating scatterplot graph
plt.scatter(x, y, label="sales vs. temperature", color="b", marker="x")

# label axes and give a title
plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
# creating legend and showing output
plt.legend()
plt.show()
