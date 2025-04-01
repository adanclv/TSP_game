import pygame
from src.configs import *
from src.spaceship import Spaceship
from src.node import Nodo
import ejemplo1
import random as rand
import math

def calcular_punto_exterior(nodo1, nodo2, radio):
    """Calcula los puntos donde la línea toca el borde del nodo."""
    x1, y1 = nodo1.rect.center
    x2, y2 = nodo2.rect.center
    angulo = math.atan2(y2 - y1, x2 - x1)  # Calcula el ángulo entre los nodos

    # Calcula los nuevos puntos de inicio y fin de la línea
    start_x = x1 + math.cos(angulo) * radio
    start_y = y1 + math.sin(angulo) * radio
    end_x = x2 - math.cos(angulo) * radio
    end_y = y2 - math.sin(angulo) * radio

    return (start_x, start_y), (end_x, end_y)

def generar_imagen_ruta(ruta, nodos):
    if not ruta:
        return None  # Si no hay ruta, no muestra nada

    imagenes_ruta = []
    for idx in ruta:
        imagen = nodos[idx].original_image # Cargar la imagen del nodo
        imagen = pygame.transform.scale(imagen, (40, 40))  # Ajustar tamaño si es necesario
        imagenes_ruta.append(imagen)

    return imagenes_ruta

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TSP game")

bg_img = pygame.image.load(PATH_BG)
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
fit_logo = pygame.image.load(PATH_FIT).convert_alpha()
fit_logo = pygame.transform.smoothscale(fit_logo, (75, 89))
uat_logo = pygame.image.load(PATH_UAT).convert_alpha()
uat_logo = pygame.transform.smoothscale(uat_logo, (102, 63))

nodos = [
    Nodo(388, 396, NODES_PATH_IMG[0][0], 1, NODES_PATH_IMG[0][1], NODES_PATH_IMG[0][2]),
    Nodo(438, 226, NODES_PATH_IMG[1][0], 2, NODES_PATH_IMG[1][1], NODES_PATH_IMG[1][2]),
    Nodo(588, 516, NODES_PATH_IMG[2][0], 2, NODES_PATH_IMG[2][1], NODES_PATH_IMG[2][2]),
    Nodo(598, 336, NODES_PATH_IMG[3][0], 1, NODES_PATH_IMG[3][1], NODES_PATH_IMG[3][2]),
    Nodo(718, 176, NODES_PATH_IMG[4][0], 1, NODES_PATH_IMG[4][1], NODES_PATH_IMG[4][2]),
    Nodo(768, 356, NODES_PATH_IMG[5][0], 1, NODES_PATH_IMG[5][1], NODES_PATH_IMG[5][2]),
    Nodo(788, 536, NODES_PATH_IMG[6][0], 1, NODES_PATH_IMG[6][1], NODES_PATH_IMG[6][2]),
    Nodo(988, 396, NODES_PATH_IMG[7][0], 0, NODES_PATH_IMG[7][1], NODES_PATH_IMG[7][2]),
    Nodo(900, 60, NODES_PATH_IMG[8][0], 0, NODES_PATH_IMG[8][1], NODES_PATH_IMG[8][2]),
    Nodo(1200, 260, NODES_PATH_IMG[9][0], 0, NODES_PATH_IMG[9][1], NODES_PATH_IMG[9][2]),
    Nodo(1250, 580, NODES_PATH_IMG[10][0], 0, NODES_PATH_IMG[10][1], NODES_PATH_IMG[10][2]),
    Nodo(700, 660, NODES_PATH_IMG[11][0], 0, NODES_PATH_IMG[11][1], NODES_PATH_IMG[11][2]),
    Nodo(290, 490, NODES_PATH_IMG[12][0], 0, NODES_PATH_IMG[12][1], NODES_PATH_IMG[12][2]),
    Nodo(200, 120, NODES_PATH_IMG[13][0], 0, NODES_PATH_IMG[13][1], NODES_PATH_IMG[13][2]),

]
# 288, -16
obstaculos = [
    Nodo(683, 420, NODES_PATH_IMG[14][0], 7, NODES_PATH_IMG[14][1], NODES_PATH_IMG[14][2]),
    Nodo(590, 160, NODES_PATH_IMG[15][0], 4, NODES_PATH_IMG[15][1], NODES_PATH_IMG[15][2]),
    Nodo(530, 390, NODES_PATH_IMG[16][0], 5, NODES_PATH_IMG[16][1], NODES_PATH_IMG[16][2]),
]


pos_actual = rand.randint(0, len(nodos) - 1)
inicio = pos_actual
destino = None
costo_total = 0
ruta = []
planetas_visitados = set()

frame_index = 0  # Empezamos con el primer frame (arriba)
frame_time = 0  # Tiempo acumulado para cambiar de frame
frame_duration = 500  # Duración entre cambios de frames en milisegundos

clock = pygame.time.Clock() # controlar frame rate
run = True
mostrar_ruta = False
tiempo_marcado = 0
ruta_imagenes = []  # Variable para almacenar las imágen
font = pygame.font.Font("assets//fonts//Kanit-Regular.ttf", 22)  # Fuente para los costos de las rutas
font_bold = pygame.font.Font("assets//fonts//Kanit-Regular.ttf", 23)  # Fuente para los costos de las rutas
font_bold.set_bold(True)
font_title = pygame.font.Font("assets//fonts//AlfaSlabOne-Regular.ttf", 32)
texto_ruta = font.render("Ruta a seguir:", True, (255, 255, 255))

player = Spaceship(nodos[inicio].rect.x, nodos[inicio].rect.y)
while run:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))
    #pygame.draw.rect(screen, (255, 255, 255), (0, 0, 800, 100))
    screen.blit(fit_logo, (1260, 15))
    screen.blit(uat_logo, (35, 25))

    for obs in obstaculos:
        obs.draw(screen)
        obs.rotation(screen)

    # Crear nodos y conexiones
    for i, nodo in enumerate(nodos):
        nodo.draw(screen)
        nodo.rotation(screen)
        for j, nodo2 in enumerate(nodos):
            if i != j and ejemplo1.are_adjacent(i, j):
                # Calcular las posiciones corregidas
                (start_x, start_y), (end_x, end_y) = calcular_punto_exterior(nodo, nodo2, (NODES_PATH_IMG[i][1]/2))

                # Dibujar línea entre los nodos sin tocar el centro
                pygame.draw.line(screen, LINES['white2'], (start_x, start_y), (end_x, end_y), 4)
                pygame.draw.line(screen, LINES['white1'], (start_x, start_y), (end_x, end_y), 2)

                # Dibujar el costo en el centro de la línea
                mid_x = (start_x + end_x) / 2
                mid_y = (start_y + end_y) / 2
                costo = ejemplo1.get_cost(i, j)  # Asegúrate de tener esta función que devuelva el costo de la arista
                texto = font.render(str(costo), True, (255, 255, 200))
                texto2 = font_bold.render(str(costo), True, (0, 0, 0))

                screen.blit(texto2, (mid_x - 10, mid_y - 10))
                screen.blit(texto, (mid_x - 9, mid_y - 9))

    # Si hay una ruta seleccionada, resaltarla antes de mover la nave
    if mostrar_ruta:
        for idx in range(len(ruta) - 1):
            nodo1 = nodos[ruta[idx]]
            nodo2 = nodos[ruta[idx + 1]]
            (start_x, start_y), (end_x, end_y) = calcular_punto_exterior(nodo1, nodo2, SHAPE_NODES['radius'])
            pygame.draw.line(screen, LINES['yellow2'], (start_x, start_y), (end_x, end_y), 5)  # Amarillo más grueso
            pygame.draw.line(screen, LINES['yellow1'], (start_x, start_y), (end_x, end_y), 3)

        if pygame.time.get_ticks() - tiempo_marcado > 1000:
            mostrar_ruta = False

    # Movimiento de la nave
    if not mostrar_ruta and player.distancia_target() < 3:
        if len(ruta) > 0:
            pos_actual = ruta.pop(0)

            player.set_target(nodos[pos_actual].rect.x, nodos[pos_actual].rect.y)
            inicio = pos_actual

        if pos_actual not in planetas_visitados:
            planetas_visitados.add(pos_actual)

    frame_time += clock.get_time()

    if frame_time > frame_duration:  # Cambiar de frame después del tiempo adecuado
        frame_index = (frame_index + 1) % len(player.frames)  # Cambiar el frame de forma cíclica
        frame_time = 0  # Resetear el tiempo de frame

    player.draw(screen,player.frames[frame_index].convert_alpha())
    player.move_towards()

    for event in pygame.event.get(): # lista de eventos del juego
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, nodo in enumerate(nodos):
                if nodo.check_click(event.pos):
                    destino = i
                    ruta, costo_total = ejemplo1.dijkstra(inicio, destino)
                    mostrar_ruta = True
                    tiempo_marcado = pygame.time.get_ticks()

                    ruta_imagenes = generar_imagen_ruta(ruta, nodos)

    if ruta_imagenes:
        texto_costo = font.render(f"Costo del viaje: {costo_total}", True, (255, 255, 255))
        screen.blit(texto_costo, (1050, 660))  # Posición fija en la esquina superior izquierda
        screen.blit(texto_ruta, (1050, 685))  # Posición (X, Y) en la pantalla
        x_offset = 1050
        y_offset = 710
        for imagen in ruta_imagenes:
            screen.blit(imagen, (x_offset, y_offset))
            x_offset += 45

    txt_title = font_title.render("Traveling Salesman", True, (255, 255, 255))
    txt_title2 = font_title.render("Problem", True, (255, 255, 255))
    txt_subtitle = font.render("(Problema del Agente Viajero)", True, (255, 255, 255))

    screen.blit(txt_title, (25, 645))
    screen.blit(txt_title2, (25, 685))
    screen.blit(txt_subtitle, (185, 690))
    pygame.display.update()

pygame.quit()