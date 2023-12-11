import os
import sys
import math
import time
import pygame
current_path = os.getcwd()
import pymunk as pm
from characters import Bird
from level import Level


pygame.init()
screen = pygame.display.set_mode((1200, 650))

pop_up = pygame.image.load(
    "./resources/images/popup.png").convert_alpha()
popup = pygame.transform.scale(pop_up, (320,120))

redbird = pygame.image.load(
    "./resources/images/bullet.png").convert_alpha()
redbird = pygame.transform.scale(redbird,(12,12))


background = pygame.image.load(
    "./resources/images/background.png").convert_alpha()
background2 = pygame.transform.scale(background, (1200,710))

tank_image = pygame.image.load(
    "./resources/images/wheel.png").convert_alpha()

gunner_image = pygame.image.load(
    "./resources/images/gunner.png").convert_alpha()


army = pygame.image.load(
    "./resources/images/army.png").convert_alpha()
general = pygame.transform.scale(army, (20, 45))

pause = pygame.image.load(
    "./resources/images/pause.png").convert_alpha()
pause_button = pygame.transform.scale(pause,(80,80))

replay = pygame.image.load(
    "./resources/images/replay.png").convert_alpha()
replay_button = pygame.transform.scale(replay,(80,80))

play = pygame.image.load(
    "./resources/images/play.png").convert_alpha()
play_button = pygame.transform.scale(play,(80,80))

next = pygame.image.load(
    "./resources/images/next.png").convert_alpha()
next_button = pygame.transform.scale(play,(80,80))

pig_hap = pygame.image.load(
    "./resources/images/tank_failed.png").convert_alpha()
pig_happy = pygame.transform.scale(pig_hap, (320,200))

shell_img = pygame.image.load(
    "./resources/images/shell.png").convert_alpha()

shell = pygame.transform.scale(shell_img, (200 , 200))
shell1 = pygame.transform.rotate(shell, 3)
shell2 = pygame.transform.rotate(shell, 0)
shell3 = pygame.transform.rotate(shell, -3)

clock = pygame.time.Clock()

clock = pygame.time.Clock()
running = True

# the base of the physics
space = pm.Space()
space.gravity = (0.0, -700.0)
armys = []
birds = []
balls = []
polys = []
beams = []
columns = []
woods = []


poly_points = []
ball_number = 0
polys_dict = {}
mouse_distance = 0
rope_lenght = 90
angle = 0
x_mouse = 0
y_mouse = 0
count = 0
mouse_pressed = False

t1 = 0
tick_to_next_circle = 10
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (253, 209, 144)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
tank_x, tank_y = 190, 520
tank2_x, tank2_y = 210, 520
score = 0
total = 0
game_state = 5
bird_path = []
counter = 0
restart_counter = False
bonus_score_once = True
bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)
wall = False

# Static floor
static_body = pm.Body(body_type=pm.Body.STATIC)
static_lines = [pm.Segment(static_body, (0.0, 060.0), (1200.0, 060.0), 0.0)]
static_lines1 = [pm.Segment(static_body, (1200.0, 060.0), (1200.0, 800.0), 0.0)]
for line in static_lines:
    line.elasticity = 0.95
    line.friction = 1
    line.collision_type = 3
for line in static_lines1:
    line.elasticity = 0.95
    line.friction = 1
    line.collision_type = 3
space.add(static_body)
for line in static_lines:
    space.add(line)


def to_pygame(p):
    """Convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)


def vector(p0, p1):
    """Return the vector of the points
    p0 = (xo,yo), p1 = (x1,y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """Return the unit vector of the points
    v = (a,b)"""
    h = ((v[0]**2)+(v[1]**2))**0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)


def distance(xo, yo, x, y):
    """distance between points"""
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d


def load_music():
    """Load the music"""
    song1 = './resources/sounds/music.mp3'
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(-1)

shot = pygame.mixer.Sound('./resources/sounds/shot.mp3')
grunt = pygame.mixer.Sound('./resources/sounds/grunt.mp3')
rock = pygame.mixer.Sound('./resources/sounds/rock.mp3')
    
start_button = pygame.image.load('./resources/images/button.png')
start = pygame.image.load('./resources/images/start.png')
background_start = pygame.transform.scale(start, (1200,710))


def tank_action():
    global mouse_distance
    global rope_lenght
    global angle
    global x_mouse
    global y_mouse
    v = vector((tank_x, tank_y), (x_mouse, y_mouse))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(tank_x, tank_y, x_mouse, y_mouse)
    pu = (uv1*rope_lenght+tank_x, uv2*rope_lenght+tank_y)
    bigger_rope = 102

    x_redbird = x_mouse - 7
    y_redbird = y_mouse - 7
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 7
        puy -= 7
        pul = pux, puy
        screen.blit(redbird, pul)
        pu2 = (-(uv1*bigger_rope)+tank_x, -(uv2*bigger_rope)+tank_y)

        opacity = min(255, int(mouse_distance * 2.5))
        line_color = (0, 0, 0, opacity)
        pygame.draw.aaline(screen, line_color, (tank_x + 10, tank_y), pu2, 5)
    else:
        mouse_distance += 10
        pu3 = (-(uv1*mouse_distance)+tank_x, -(uv2*mouse_distance)+tank_y)
        screen.blit(redbird, (x_redbird, y_redbird))

        opacity = min(255, int(mouse_distance * 2.5))
        line_color = (0, 0, 0, opacity)
        pygame.draw.aaline(screen, line_color, (tank_x + 10, tank_y), pu3, 5)
    # Angle of impulse
    dy = y_mouse - tank_y
    dx = x_mouse - tank_x
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy))/dx)


def draw_level_cleared():
    """Draw level cleared"""
    global game_state
    global bonus_score_once
    global score

    level_cleared = bold_font3.render("Level Cleared!", 1, WHITE)
    score_level_cleared = bold_font2.render(str(score), 1, WHITE)

    if level.number_of_birds >= 0 and len(armys) == 0:
        if bonus_score_once:
            score += (level.number_of_birds-1) * 10000
        bonus_score_once = False
        game_state = 4
        rect = pygame.Rect(300, 0, 600, 800)
        pygame.draw.rect(screen, ORANGE, rect)
        screen.blit(level_cleared, (450, 90))
        if score >= level.one_star and score <= level.two_star:
            screen.blit(shell1, (310, 190))
        if score >= level.two_star and score <= level.three_star:
            screen.blit(shell1, (310, 190))
            screen.blit(shell2, (500, 193))
        if score >= level.three_star:
            screen.blit(shell1, (310, 190))
            screen.blit(shell2, (500, 193))
            screen.blit(shell3, (700, 190))
        screen.blit(score_level_cleared, (550, 400))
        screen.blit(replay_button, (500, 480))
        screen.blit(next_button, (620, 480))

def end_game():
        global total
        screen.fill((0,0,0))
        print(total)
        print('You Win')
        exit()


def draw_level_failed():
    """Draw level failed"""
    global game_state
    failed = bold_font3.render("Level Failed", 1, WHITE)
    if level.number_of_birds <= 0 and time.time() - t2 > 5 and len(armys) > 0:
        game_state = 3
        rect = pygame.Rect(300, 80, 600, 450)
        pygame.draw.rect(screen, ORANGE, rect)
        screen.blit(failed, (485, 120))
        screen.blit(pig_happy, (450, 200))
        screen.blit(replay_button, (560, 430))

def start_game():
    """Draw level failed"""
    global game_state
    game_state = 5
    screen.blit(background_start, (0,0))
    screen.blit(start_button, (500, 320))

def restart():
    """Delete all objects of the level"""
    armys_to_remove = []
    birds_to_remove = []
    columns_to_remove = []
    beams_to_remove = []
    woods_to_remove= []

    for army in armys:
        armys_to_remove.append(army)
    for army in armys_to_remove:
        space.remove(army.shape, army.shape.body)
        armys.remove(army)
    for bird in birds:
        birds_to_remove.append(bird)
    for bird in birds_to_remove:
        space.remove(bird.shape, bird.shape.body)
        birds.remove(bird)

    for column in columns:
        columns_to_remove.append(column)
    for column in columns_to_remove:
        space.remove(column.shape, column.shape.body)
        columns.remove(column)
    for beam in beams:
        beams_to_remove.append(beam)
    for beam in beams_to_remove:
        space.remove(beam.shape, beam.shape.body)
        beams.remove(beam)

    for wood in woods:
        woods_to_remove.append(wood)
    for wood in woods_to_remove:
        space.remove(wood.shape, wood.shape.body)
        woods.remove(wood)

def post_solve_bird_army(arbiter, space, _):
    surface=screen
    a, b = arbiter.shapes
    bird_body = a.body
    army_body = b.body
    p = to_pygame(bird_body.position)
    p2 = to_pygame(army_body.position)
    r = 30
    pygame.draw.circle(surface, BLACK, p, r, 4)
    pygame.draw.circle(surface, RED, p2, r, 4)
    armys_to_remove = []
    for army in armys:
        if army_body == army.body:
            army.life -= 20
            armys_to_remove.append(army)
            global score
            score += 10000
    for army in armys_to_remove:
        space.remove(army.shape, army.shape.body)
        armys.remove(army)
    
    grunt.set_volume(1.5)
    grunt.play()


def post_solve_bird_wood(arbiter, space, _):
    """Collision between bird and wood"""
    poly_to_remove = []
    if arbiter.total_impulse.length > 1100:
        a, b = arbiter.shapes
        for column in columns:
            if b == column.shape:
                poly_to_remove.append(column)
        for beam in beams:
            if b == beam.shape:
                poly_to_remove.append(beam)
        for wood in woods:
            if b == wood.shape:
                poly_to_remove.append(wood)
        for poly in poly_to_remove:
            if poly in columns:
                columns.remove(poly)
            if poly in beams:
                beams.remove(poly)
            if poly in woods:
                woods.remove(poly)
        space.remove(b, b.body)
        global score
        score += 5000
        rock.play()

def post_solve_army_wood(arbiter, space, _):
    armys_to_remove = []
    if arbiter.total_impulse.length > 700:
        army_shape, wood_shape = arbiter.shapes
        for army in armys:
            if army_shape == army.shape:
                army.life -= 20
                global score
                score += 10000
                if army.life <= 0:
                    armys_to_remove.append(army)
    for army in armys_to_remove:
        space.remove(army.shape, army.shape.body)
        armys.remove(army)



space.add_collision_handler(0, 1).post_solve=post_solve_bird_army

space.add_collision_handler(0, 2).post_solve=post_solve_bird_wood

space.add_collision_handler(1, 2).post_solve=post_solve_army_wood
load_music()
level = Level(armys, columns, beams, woods, space)
level.number = 5
level.load_level()


while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            # Toggle wall
            if wall:
                for line in static_lines1:
                    space.remove(line)
                wall = False
            else:
                for line in static_lines1:
                    space.add(line)
                wall = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            space.gravity = (0.0, -700.0)
            level.bool_space = False


        if (pygame.mouse.get_pressed()[0] and x_mouse > 100 and
                x_mouse < 250 and y_mouse > 370 and y_mouse < 550):
            mouse_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and
                event.button == 1 and mouse_pressed):
            mouse_pressed = False
            shot.play()
            if level.number_of_birds > 0:
                level.number_of_birds -= 1
                t1 = time.time()*1000
                xo = 203
                yo = 90
                if mouse_distance > rope_lenght:
                    mouse_distance = rope_lenght
                if x_mouse < tank_x+5:
                    bird = Bird(mouse_distance, angle, xo, yo, space)
                    birds.append(bird)
                else:
                    bird = Bird(-mouse_distance, angle, xo, yo, space)
                    birds.append(bird)
                if level.number_of_birds == 0:
                    t2 = time.time()

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if game_state == 5:
                if (x_mouse < 700 and x_mouse >500 and y_mouse < 420 and y_mouse > 320):
                    game_state = 0
            if game_state ==0:
                if (x_mouse < 60 and y_mouse < 155 and y_mouse > 90):
                    game_state = 1
            if game_state == 1:
                if x_mouse < 560 and y_mouse > 200 and y_mouse < 400:
                    # Resume in the paused screen
                    game_state = 0
                if x_mouse > 640 and y_mouse > 200 and y_mouse < 400:
                    # Restart in the paused screen
                    restart()
                    level.load_level()
                    game_state = 0
                    bird_path = []

            if game_state == 3:
                # Restart in the failed level screen
                if x_mouse > 560 and x_mouse < 640 and y_mouse > 430:
                    restart()
                    level.load_level()
                    game_state = 0
                    bird_path = []
                    score = 0

            if game_state == 4:
                # Build next level
                if x_mouse > 620 and y_mouse > 450:
                    total += score
                    if level.number ==5:
                        game_state = 6
                    else: 
                        restart()
                        level.number += 1
                        game_state = 0
                        score = 0
                        bird_path = []
                        bonus_score_once = True
                        level.load_level()
                if x_mouse < 580 and x_mouse > 500 and y_mouse > 450:
                    # Restart in the level cleared screen
                    restart()
                    level.load_level()
                    game_state = 0
                    bird_path = []
                    score = 0
            if game_state == 6:
                if x_mouse > 620 and y_mouse > 450:
                    end_game()
                
            

    x_mouse, y_mouse = pygame.mouse.get_pos()
    # Draw background
    screen.fill((130, 200, 100))
    screen.blit(background2, (0, -50))
    # Draw first part of the tank
    rect = pygame.Rect(0, 3, 100, 24)
    screen.blit(tank_image, (155, 520), rect)

    # Draw the trail left behind
    for point in bird_path:
        pygame.draw.circle(screen, WHITE, point, 5, 0)
    # Draw the birds in the wait line


    # Draw tank behavior
    if mouse_pressed and level.number_of_birds > 0:
        tank_action()
    else:
        if time.time()*1000 - t1 > 300 and level.number_of_birds > 0:
            screen.blit(redbird, (200, 500))
        else:
            pygame.draw.line(screen, (0, 0, 0), (tank_x, tank_y-8),
                             (tank2_x, tank2_y-7), 5)
    birds_to_remove = []
    armys_to_remove = []
    counter += 1
    # Draw birds
    for bird in birds:
        if bird.shape.body.position.y < 0:
            birds_to_remove.append(bird)
        p = to_pygame(bird.shape.body.position)
        x, y = p
        x -= 8
        y -= 6
        screen.blit(redbird, (x, y))
        if counter >= 3 and time.time() - t1 < 5:
            bird_path.append(p)
            restart_counter = True
    if restart_counter:
        counter = 0
        restart_counter = False



    for bird in birds_to_remove:
        space.remove(bird.shape, bird.shape.body)
        birds.remove(bird)
    for army in armys_to_remove:
        space.remove(army.shape, army.shape.body)
        armys.remove(army)
    
    # Draw static lines
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, (150, 150, 150), False, [p1, p2])
    
    
    i = 0 
    for army in armys:
        i += 1
        # print (i,army.life)
        army = army.shape
        if army.body.position.y < 0:
            armys_to_remove.append(army)

        p = to_pygame(army.body.position)
        x, y = p

        angle_degrees = math.degrees(army.body.angle)
        img = pygame.transform.rotate(general, angle_degrees)
        w,h = img.get_size()

        x -= w*0.5
        y -= h*0.5

        screen.blit(img, (x, y))

    # Draw columns and Beams
    for column in columns:
        column.draw_poly('columns', screen)
    for beam in beams:
        beam.draw_poly('beams', screen)
    for wood in woods:
        wood.draw_poly('woods', screen)
    # Update physics
    dt = 1.0/70.0/2.
    for x in range(2):
        space.step(dt) # make two updates per frame for better stability
    
    # Drawing second part of the tank
    rect = pygame.Rect(0, 0, 100, 30)
    screen.blit(gunner_image, (165, 498), rect)
    # Draw score
    score_font = bold_font.render("SCORE", 1, WHITE)
    number_font = bold_font.render(str(score), 1, WHITE)
    screen.blit(score_font, (1060, 90))
    if score == 0:
        screen.blit(number_font, (1100, 130))
    else:
        screen.blit(number_font, (1060, 130))
    screen.blit(pause_button, (10, 90))
    # Pause option
    if game_state == 1:
        screen.blit(popup, (440,300))
        screen.blit(play_button, (480, 320))
        screen.blit(replay_button, (640, 320))
    
    # start_screen()
    if game_state == 5:
        start_game()
    
    draw_level_cleared()
    draw_level_failed()
    pygame.display.flip()
    clock.tick(70)

    pygame.display.set_caption("20201077_박재우")
