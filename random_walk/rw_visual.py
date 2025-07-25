import matplotlib.pyplot as plt

from .random_walk import RandomWalk


# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in walks
    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(7, 5), dpi=105) # figsize adjust the screen size of the plt
    # generate list of number that are equal to number in the points
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=5, marker='o', linestyle='', color='lightgreen') # edgecolors none get rid of the black outline #type: ignore

    # Remove the axes
    ax.get_xaxis().set_visible(False) # remove x axis
    ax.get_yaxis().set_visible(False) # remove y axis

    plt.show()
    # plt.savefig("random_walk.png", bbox_inches='tight')

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break