import os
import sys

import pygame
import requests
spn = [50, 2]
coords = [135.530887, -26.703118]

map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map".format(coords[0], coords[1], spn[0], spn[1])
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)