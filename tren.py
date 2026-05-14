import pygame
import sys

pygame.init()

# Ventana
pantalla = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Tren")

# Colores
AZUL = (135, 206, 235)
VERDE = (0, 200, 0)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
GRIS = (150, 150, 150)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)

clock = pygame.time.Clock()

# posición del tren
x = 0

# Humo
humo_y = 180

# Fuente (mejor crearla una sola vez)
fuente = pygame.font.SysFont(None, 30)

while True:

    # Cerrar ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fondo
    pantalla.fill(AZUL)

    #  Sol
    pygame.draw.circle(pantalla, AMARILLO, (700, 80), 40)
    

    # Piso
    pygame.draw.rect(pantalla, VERDE, (0, 350, 800, 150))

    # Tren
    pygame.draw.rect(pantalla, ROJO, (x, 250, 200, 100))

    # Cabina
    pygame.draw.rect(pantalla, GRIS, (x + 130, 200, 70, 50))

    # Ventana
    pygame.draw.rect(pantalla, BLANCO, (x + 145, 215, 30, 20))

    # Chimenea
    pygame.draw.rect(pantalla, NEGRO, (x + 30, 200, 20, 50))

    # Ruedas
    pygame.draw.circle(pantalla, NEGRO, (x + 40, 350), 20)
    pygame.draw.circle(pantalla, NEGRO, (x + 100, 350), 20)
    pygame.draw.circle(pantalla, NEGRO, (x + 160, 350), 20)

    # Humo
    pygame.draw.circle(pantalla, GRIS, (x + 40, humo_y), 15)

    humo_y -= 2
    if humo_y < 100:
        humo_y = 180

    #  Nombre dentro del tren
    texto = fuente.render("ALEJANDRO", True, BLANCO)
    pantalla.blit(texto, (x + 60, 265))

    # Movimiento del tren
    x += 2
    if x > 800:
        x = -200

    pygame.display.update()
    clock.tick(60)