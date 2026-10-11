import pygame
import math
from engine.hex_math import hex_to_pixel, HEX_SIZE

class Renderer:
    def __init__(self, screen, camera, game_map):
        self.screen = screen
        self.camera = camera
        self.game_map = game_map

        self.colors = {
            "grass": (160, 200, 160),
            "water": (100, 149, 237),
            "forest": (34, 139, 34),
            "hill": (139, 69, 19),
            "residential": (255, 255, 255),
            "commercial": (255, 255, 0),
            "industrial": (128, 128, 128),
            "utility": (0, 0, 255),
            "park": (50, 205, 50)
        }

    def draw_hex(self, x, y, color):
        points = []
        for i in range(6):
            angle = math.radians(60 * i + 30)
            px = x + HEX_SIZE * math.cos(angle)
            py = y + HEX_SIZE * math.sin(angle)
            points.append((px, py))
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, (255, 255, 255), points, 2)

    def draw_map(self):
        for tile in self.game_map.tiles:
            px, py = hex_to_pixel(tile.q, tile.r)
            px -= self.camera.x
            py -= self.camera.y

            color = self.colors.get(tile.tile_type, (200, 200, 200))
            self.draw_hex(px, py, color)