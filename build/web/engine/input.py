import pygame
from engine.hex_math import pixel_to_hex

class InputHandler:
    def __init__(self, camera, game_map):
        self.camera = camera
        self.game_map = game_map
        
        self.selected_type = "grass"
        self.money = 1000

        self.tile_costs = {
            "grass": 10,
            "water": 10,
            "forest": 25,
            "hill": 25,
            "residential": 50,
            "commercial": 100,
            "industrial": 75,
            "utility": 150,
            "park": 20
        }

        self.hover_q = None
        self.hover_r = None
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
            mx += self.camera.x
            my += self. camera.y
            self.hover_q, self.hover_r = pixel_to_hex(mx, my)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Check shop clicks first
            if shop.handle_click(mx,my):
                return
            
            if self.game_map.get_tile(q, r) is None:
                if self.game_map.is_adjacent_to_existing(q, r):
                    cost = self.tile_costs.get[self.selected_type]
                    if self.money >= cost:
                       self.money -= cost
                       self.game_map.add_tile(q, r, self.selected_type)