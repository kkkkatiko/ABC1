import os
import sys

import pygame
import requests
a = input('Введите масштаб:')
spn = list(map(int, a.split()))
a = input('Введите координаты:')
coords = list(map(int, a.split()))


def fdecj():
    global map_request, respone, map_file
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


while pygame.event.wait().type != pygame.QUIT:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_PAGEUP:
                if spn[0] + 10 <= 90 and spn[1] + 10 <= 90:
                    spn[0] += 10
                    spn[1] += 10
            if i.key == pygame.K_PAGEDOWN:
                if spn[0] - 10 >= 0 and spn[1] - 10 >= 0:
                    spn[0] -= 10
                    spn[1] -= 10
    fdecj()
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove(map_file)