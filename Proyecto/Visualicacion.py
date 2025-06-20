from math import log, atan2, cos, sin, sqrt
import pygame
import random

# create the main surface (or window)
WIDTH, HEIGHT   = 1020, 720
BORDER          = 10
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
BG    = (255, 255, 255)
BLACK = (40, 40, 40)

# configuration
ITERS           = 500
FPS             = 90
NODE_RADIUS     = 3
DIST_MIN        = (min(WIDTH, HEIGHT)) // 30
NODE_MIN_WIDTH  = 5
NODE_MIN_HEIGHT = 5
NODE_MAX_WIDTH  = WIDTH - 5
NODE_MAX_HEIGHT = HEIGHT - 5

# spring constants
c1 = 1.65
c2 = 0.9
c3 = 0.4
c4 = 0.6
x=random.randint(0,150)
y=random.randint(0,150)
z=random.randint(0,150)
colorRam=(x,y,z)

def spring(g):
    """
    Muestra una animación del metodo de visualizacion spring de Eades.

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    run = True
    clock = pygame.time.Clock()

    init_nodes(g)
    draw_edges(g)
    draw_nodes(g)


    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            continue

        WIN.fill(BG)
        update_nodes(g)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        i += 1

    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones random

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for node in g.ObtenerNodos():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]
        node.attrs['disp'] = [0.0,0.0]

    return

def update_nodes(g):
    """
    Aplica la fuerza a los nodos del grafo G para actualizar su poisicion

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """
    ################
    for node in g.ObtenerNodos():
        x_attraction = 0
        y_attraction = 0
        x_node, y_node = node.attrs['coords']

        for other in node.vecinos:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5

            # defining minimum distance
            if d < DIST_MIN:
                continue
            attraction = c1 * log(d / c2)
            angle = atan2(y_other - y_node, x_other - x_node)
            x_attraction += attraction * cos(angle)
            y_attraction += attraction * sin(angle)

        not_connected = (other for other in g.ObtenerNodos() 
                        if (other.valor not in node.vecinos and other != node))
        x_repulsion = 0
        y_repulsion = 0
        for other in not_connected:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5
            if d == 0:
                continue
            repulsion = c3 / d ** 0.5
            angle = atan2(y_other - y_node, x_other - x_node)
            x_repulsion -= repulsion * cos(angle)
            y_repulsion -= repulsion * sin(angle)

        fx = x_attraction + x_repulsion
        fy = y_attraction + y_repulsion
        node.attrs['coords'][0] += c4 * fx
        node.attrs['coords'][1] += c4 * fy

        # Restrict for limits of window
        node.attrs['coords'][0] = max(node.attrs['coords'][0], NODE_MIN_WIDTH)
        node.attrs['coords'][1] = max(node.attrs['coords'][1], NODE_MIN_HEIGHT)
        node.attrs['coords'][0] = min(node.attrs['coords'][0], NODE_MAX_WIDTH)
        node.attrs['coords'][1] = min(node.attrs['coords'][1], NODE_MAX_HEIGHT)

    return


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """
    
    for node in g.ObtenerNodos():
        pygame.draw.circle(WIN, colorRam, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, colorRam, node.attrs['coords'], NODE_RADIUS, 3)

    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g

    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """

    for edge in g.ObtenerAristas():
        u, v = edge.ObtenerNodos()
        u_pos = u.attrs['coords']
        v_pos = v.attrs['coords']

        pygame.draw.line(WIN, BLACK, u_pos, v_pos, 1)

    return

def fruchterman_reginold(g,fuerza=0.3):
    """
    Muestra una animación del metodo de visualizacion de Furchterman y Reginold
    Parametros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualizacion
    """
    run = True
    clock = pygame.time.Clock()
    area = (NODE_MAX_WIDTH - NODE_MIN_WIDTH) * (NODE_MAX_HEIGHT - NODE_MIN_HEIGHT)
    k = sqrt(area / len(g.ObtenerNodos())) * fuerza # constante de fuerza
    t = min(WIDTH, HEIGHT) / 10  # temperatura inicial
    i=0

    init_nodes(g)
    draw_edges(g)
    draw_nodes(g)

    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            False

        WIN.fill(BG)
        update_nodesfruchterman_reginold(g, t, k)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        t *= 0.995  # enfriar temperatura
        i += 1

    pygame.quit()
    return

def update_nodesfruchterman_reginold(g,t,k):
    """
    Aplica el algoritmo de Fruchterman-Reingold para actualizar las posiciones.
    """
    for v in g.ObtenerNodos():
        v.attrs['disp'] = [0.0, 0.0]

    for v in g.ObtenerNodos():
        for u in g.ObtenerNodos():
            if v == u:
                continue
            delta = [v.attrs['coords'][0] - u.attrs['coords'][0], v.attrs['coords'][1] - u.attrs['coords'][1]]
            dist = distancia(v.attrs['coords'], u.attrs['coords'])
            if dist < DIST_MIN:
                dist = DIST_MIN
            fuerza = k * k / max(dist, 0.1)
            v.attrs['disp'][0] += delta[0] / dist * fuerza
            v.attrs['disp'][1] += delta[1] / dist * fuerza

    for arista in g.ObtenerAristas():
        u, v = arista.ObtenerNodos()
        delta = [v.attrs['coords'][0] - u.attrs['coords'][0], v.attrs['coords'][1] - u.attrs['coords'][1]]
        dist = distancia(u.attrs['coords'], v.attrs['coords'])
        if dist < DIST_MIN:
                dist = DIST_MIN
        fuerza = dist * dist / k
        u.attrs['disp'][0] += delta[0] / dist * fuerza
        u.attrs['disp'][1] += delta[1] / dist * fuerza
        v.attrs['disp'][0] -= delta[0] / dist * fuerza
        v.attrs['disp'][1] -= delta[1] / dist * fuerza

    for nodo in g.ObtenerNodos():
        dx, dy = nodo.attrs['disp']
        x, y = nodo.attrs['coords']
        max_disp = min(t, 10)
        dx = max(-max_disp, min(max_disp, dx))
        dy = max(-max_disp, min(max_disp, dy))
        x += dx + (WIDTH / 2 - x) * t * 0.001
        y += dy + (HEIGHT / 2 - y) * t * 0.001
        x = max(20, min(WIDTH - 20, x))
        y = max(20, min(HEIGHT - 20, y))
        nodo.attrs['coords'] = [x, y]

def distancia(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return sqrt(dx**2 + dy**2) + 0.01


