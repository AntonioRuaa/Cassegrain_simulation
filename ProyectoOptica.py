import pygame
import math
import numpy as np
import pygame.gfxdraw


def x1(y1):
    x1 = (-6.951*10**2)+1.779*10*y1+(-8.873*10**-2)*y1**2+1.976*10**-4*y1**3+(-1.656*10**-7)*y1**4
    return x1

def x2(y2):
    x2 = (-3.302*10**3)+4.53*10*y2+(-2.149*10**-1)*y2**2+4.64*10**-4*y2**3+(-3.855*10**-7)*y2**4
    return x2
def x3(y3):
    x3 = (2.221*10**2)+1.323*y3+(-5.226*10**-3)*y3**2+9.593*10**-6*y3**3+(-7.276*10**-9)*y3**4
    return x3

def y_1(y3):
    y_1 = (2.181*10**2)+9.602*10**-2*y3+(1.151*10**-3)*y3**2+(-2.448*10**-6)*y3**3+(1.922*10**-9)*y3**4
    return y_1

# Inicializa Pygame
pygame.init()

# Configura la ventana de visualización
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simulación Telescopio Cassegrain")
clock = pygame.time.Clock()




# Bucle de simulación
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Borra la pantalla
    screen.fill((0, 0, 0))

    # Obtener las coordenadas del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Dibujar las coordenadas del mouse en la pantalla
    mouse_text = pygame.font.SysFont(None, 24).render(f"Coords: ({mouse_x}, {mouse_y})", True, 'white')
    screen.blit(mouse_text, (10, 10))

    # Obtener el estado del botón del mouse
    mouse_buttons = pygame.mouse.get_pressed()

    # Verificar si se ha realizado un clic
    if mouse_buttons[0] :  # Botón izquierdo del mouse
        if (200<mouse_y<254 or 342<mouse_y<400):
            pygame.draw.line(screen, 'yellow', (0,mouse_y), (x1(mouse_y),mouse_y),3)
            pygame.draw.line(screen, 'yellow', (x1(mouse_y),mouse_y), (x3(mouse_y),y_1(mouse_y)),3)
            pygame.draw.line(screen, 'yellow', (x3(mouse_y),y_1(mouse_y)), (650, 300),3)
        elif (254<=mouse_y<=342):
            pygame.draw.line(screen, 'yellow', (0,mouse_y), (x2(mouse_y),mouse_y),3)
            pygame.draw.line(screen, 'yellow', (x2(mouse_y),mouse_y), (200,300),3)
        else:
            pygame.draw.line(screen, 'yellow', (0,mouse_y), (800,mouse_y),3)
            
    


    #Dibujo línea
    pygame.draw.line(screen, 'white', (0,300), (800,300))

    #Dibujo parábola
    pygame.draw.arc(screen, 'white', (600, 200, 50, 200), 3/2*np.pi, np.pi*17/9,2 )
    pygame.draw.arc(screen, 'white', (600, 200, 50, 200), 1/9*np.pi, np.pi/2,2 )

    #Dibujo hipérbola
    pygame.draw.arc(screen, 'white', (300, 250, 50, 100), 5/3*np.pi, np.pi/3,2 )

    #Dibujo de focos
    pygame.draw.circle(screen, 'red', (200, 300), 5,0) #foco 1 150 px
    pygame.draw.circle(screen, 'red', (650, 300), 5,0) #foco 2 150 px

    #Render the game
    pygame.display.flip()
    clock.tick(40) #40 fps

    
pygame.quit()