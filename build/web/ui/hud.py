import pygame

class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("Arial", 20)

    def draw(self, money, selected_type):
        text1 = self.font.render(
            f"Money: {int(money)} Selected tile: {selected_type}",
            True,
            (80, 80, 120)
        )
        text2 = self.font.render(
            "W/A/S/D to move, 1-9 to change tile type, click to place",
            True,
            (80, 80, 120)
        )
        self.screen.blit(text1, (20, 20))
        self.screen.blit(text2, (20, 50))
