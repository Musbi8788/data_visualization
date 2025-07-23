from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize the attribues of a walk."""
        self.num_points=num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self,):
        """Calculate all the points in the walk."""

        
        self.x = self.x_values.get_step()
        self.y = self.y_values.get_step()

    def get_step(self):
        """Determine the direction and distance of each step.
        """
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction

            # move right when positive , move left when negative, and 0 move vertical
            x_direction = choice([1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            x_step = x_direction * x_distance

            # move right when positive , move left when negative, 0 move horizontal
            y_direction = choice([1, -1])
            # choose random distance from 0 4
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Store the new positions
            self.x_values.append(x)
            self.y_values.append(y)
