# projectile.py

"""projectile.py
Provides a simple class for modeling the
flight of projectiles."""

import math


class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity, and height."""
        self.x_pos = 0.0
        self.y_pos = height
        theta = math.radians(angle)
        self.x_vel = velocity * math.cos(theta)
        self.y_vel = velocity * math.sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.x_pos = self.x_pos + time * self.x_vel
        y_vel_1 = self.y_vel - time * 9.8
        self.y_pos = self.y_pos + time * (self.y_vel + y_vel_1) / 2
        self.y_vel = y_vel_1

    def get_x(self):
        """Returns the x position (distance) of this projectile."""
        return self.x_pos

    def get_y(self):
        """Returns the y position (height) of this projectile."""
        return self.y_pos
