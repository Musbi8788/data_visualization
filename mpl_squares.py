import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Using a built in styles
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots() # fig represent figure, ax represent single plot in the figure

ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0)) # s adjust the dot size

# ax.plot(input_values, squares, linewidth=3) # plot is used for plotting the data in a meaningful way. linewidth represent the plot line width

# Set chart title and label, axes
ax.set_title("Square Numbers", fontsize=24) #  the chart title
ax.set_xlabel("Value", fontsize=14) # the x label 
ax.set_ylabel("Square of Value", fontsize=14) # the y label

# Set size of tick labels
ax.tick_params(axis='both', which='major' ,labelsize=14) # axis both apply the effect on both x and y ``

# Set the range of each axis
ax.axis([0, 1100, 0, 1100000]) #type: ignore

plt.show() # display the matplotlib viewer