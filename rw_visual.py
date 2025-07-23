import matplotlib.pyplot as plt

from random_walk import RamdonWalk


# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk
    rw = RamdonWalk(50_000)
    rw.fill_walk()

    # Plot the points in walks
    plt.style.use('classic')

    fig, ax = plt.subplots()
    # generate list of number that are equal to number in the points
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues, edgecolors='none', s=1) # edgecolors none get rid of the black outline #type: ignore

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) 

    # Remove the axes
    ax.get_xaxis().set_visible(False) # remove x axis
    ax.get_yaxis().set_visible(False) # remove y axis

    plt.show()
    # plt.savefig("random_walk.png", bbox_inches='tight')

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break