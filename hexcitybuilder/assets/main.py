import pygame
from engine.renderer import Renderer
from engine.camera import Camera
from engine.input import InputHandler
from world.map import HexMap
from ui.hud import HUD
from ui.shop import TileShop

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HexCity Builder")
clock = pygame.time.Clock()

game_map = HexMap()
camera = Camera()
input_handler = InputHandler(camera, game_map)
renderer = Renderer(screen, camera, game_map)
hud = HUD(screen)
shop = TileShop(screen, input_handler)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_handler.handle_event(event)

    camera.update()

    screen.fill((240, 240, 255))

    renderer.draw_map()
    hud.draw(input_handler.money, input_handler.selected_type)
    shop.draw()
    hud.draw(input_handler.money, input_handler.selected_type)

    pygame.display.flip()

pygame.quit()