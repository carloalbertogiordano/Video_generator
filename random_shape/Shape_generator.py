# Definiamo una classe Forma per rappresentare le forme che disegneremo sullo schermo
import math
import random

from PIL import Image
import numpy
import pygame


class Forma:
    def __init__(self, x, y, colore, screen_width, screen_height):
        self.x = x
        self.y = y
        self.colore = colore
        self.vertici = []
        self.screen_width = screen_width
        self.screen_height = screen_height

    def genera_vertici(self):
        # Genera i vertici della forma sulla circonferenza
        num_vertici = random.randint(3, 10)  # Numero di vertici della forma (esagono)
        raggio = random.randint(10, int(min(self.screen_width, self.screen_height) / 2))  # Raggio della circonferenza
        angolo_step = 360 / num_vertici  # Passo in gradi tra un vertice e il successivo
        for i in range(num_vertici):
            angolo = i * angolo_step
            vertice_x = self.x + raggio * math.cos(math.radians(angolo))
            vertice_y = self.y + raggio * math.sin(math.radians(angolo))
            self.vertici.append((vertice_x, vertice_y))

    # Calcola la distanza euclidea tra due punti (x1, y1) e (x2, y2)
    def distanza(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def disegna(self, schermo):
        # Cambia gravità alla forma
        gravita_x, gravita_y = random.randint(0, self.screen_width), random.randint(0, self.screen_height)
        distanza = self.distanza(gravita_x, gravita_y, self.x, self.y)
        self.x += (gravita_x - self.x) / distanza
        self.y += (gravita_y - self.y) / distanza
        # Disegna la forma utilizzando i vertici memorizzati
        pygame.draw.polygon(schermo, self.colore, self.vertici)

    def make_pillow_image(self, schermo):
        x3 = pygame.surfarray.pixels3d(schermo)
        array = numpy.uint8(x3)
        im = Image.fromarray(array)
        im.transpose(Image.ROTATE_90)
        im.save("out.jpg")
