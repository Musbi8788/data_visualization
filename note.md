# Generating date
 * The pyplot module contains a number of functions that generate charts and plots
* subplot can generate one or more plot in the same figure.
  
### Correnting the plot x coodinate
you can change the x conodinat by generating your own like this 
```.plot(input_values, squares, linewidth=3)```

### built in stles in plot
to check the avaible built in styles run 
```>>> import matplotlib.pyplot as plt```
```>>> plt.style.available```

### Plotting and Styling Individual Points with scatter()
this method show a dot on a specific in the chart and to make it apply that the only thing you do is to pass x-y values
```ax.scatter(2, 4)```

To define a color we use ```c='red'``` scatter() method and we can also you RGB we value between zore and one eg ```c=(0, 0.8, 0)```

```c=y_values, cmap=plt.cm.Blues``` we use this to apply a colormap in our chart it's show the light color and the starting and dark to the ending of the chart and you can also use any color name eg `Blues, Reds, ect.`

## Note:
You can see all the colormaps available in pyplot at https://matplotlib.org/; go to
Examples, scroll down to Color, and click Colormap reference.

## Saving a plot
```plt.savefig('squares_plot.png', bbox_inches='tight')```

### Random walk


stop 361