import pygame
import pygame
from engine.renderer import Renderer
from engine.camera import Camera
from engine.input import InputHandler
from world.map import HexMap
from ui.hud import HUD

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HexCity Builder")
clock = pygame.time.Clock()

game_map = HexMap(radius=8)
camera = Camera()
input_handler = InputHandler(camera, game_map)
renderer = Renderer(screen, camera, game_map)
hud = HUD(screen)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_handler.handle_event(event)

    input_handler.update(dt)

    screen.fill((240, 240, 255))  # pastel background

    renderer.draw_map()
    hud.draw(game_map)

    pygame.display.flip()

pygame.quit()