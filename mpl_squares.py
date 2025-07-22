import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() # fig represent figure, ax represent single plot in the figure
ax.plot(input_values, squares, linewidth=3) # plot is used for plotting the data in a meaningful way. linewidth represent the plot line width

# Set chart title and label, axes
ax.set_title("Square Numbers", fontsize=14) #  the chart title
ax.set_xlabel("Value", fontsize=14) # the x label 
ax.set_ylabel("Square of Value", fontsize=14) # the y label

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14) # axis both apply the effect on both x and y ``


plt.show() # display the matplotlib viewer