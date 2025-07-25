from plotly.graph_objs import Scatter, Layout
from plotly import offline


from random_walk import RandomWalk


# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in walks
    point_numbers = list(range(1,rw.num_points+1))

    data = [Scatter(
        x=rw.x_values,
        y=rw.y_values,
        mode='markers',
        marker=dict(
            size=3,
            color=list(range(rw.num_points)),
            colorscale='Viridis',
            showscale=True
        )
        )]  

    my_layout = Layout(
        title='Random Walk Visualization.',
        xaxis=dict(title='X Values'),
        yaxis=dict(title='Y Values'),
        )  # set the chart layout

    # generate a chart and save it in a html format
    offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')

    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break