# Let's define a Shape class to represent the shapes we will draw on the screen
import math
import random

from PIL import Image
import numpy
import pygame


class Shape:
    def __init__(self, x, y, colour, screen_width, screen_height):
        self.x = x
        self.y = y
        self.colour = colour
        self.vertices = []
        self.screen_width = screen_width
        self.screen_height = screen_height

    def generate_vertices(self):
        # Generate the vertexes of the shape on a circle
        num_vertices = random.randint(3, 10)
        radius = random.randint(10, int(min(self.screen_width, self.screen_height) / 2))  # Circumference radius
        angle_step = 360 / num_vertices  # Step in degrees between an angle and the next
        for i in range(num_vertices):
            angle = i * angle_step
            vertex_x = self.x + radius * math.cos(math.radians(angle))
            vertex_y = self.y + radius * math.sin(math.radians(angle))
            self.vertices.append((vertex_x, vertex_y))

    # Calculate euclidian distance between two points
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def draw(self, screen):
        # Change shape gravity
        gravity_x, gravity_y = random.randint(0, self.screen_width), random.randint(0, self.screen_height)
        distance = self.distance(gravity_x, gravity_y, self.x, self.y)
        self.x += (gravity_x - self.x) / distance
        self.y += (gravity_y - self.y) / distance
        # Draw the shape using the memorized vertexes
        pygame.draw.polygon(screen, self.colour, self.vertices)
