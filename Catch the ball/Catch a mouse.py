import pygame as pg
from pygame.draw import *
from pygame.locals import *
from random import randint, random
import pygame.freetype
import json
pg.init()

FPS = 30
size_x, size_y = 800, 800
screen = pg.display.set_mode((size_x, size_y))
number_of_rodents = 18
rodents = list()
font = pg.freetype.SysFont('Times New Roman', 35)
points = 0
k = 0
pop_x = 0
pop_y = 0
table = False
timer = 0
seconds = 30
minutes = 0
catpoints = 0
n = 0


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


class Mouse:
    def __init__(self, x1, x2, y1, y2):
        self.x = randint(x1, x2)
        self.y = randint(y1, y2)
        self.r = randint(10, 20)
        self.speed = 15
        self.vx = randint(-self.speed, self.speed)
        self.vy = randint(-self.speed, self.speed)
        self.color = (153, 153, 153)

    def move(self, t):
        if (self.vx == 0) and (self.vx == 0):
            self.vy = randint(-self.speed, self.speed)
            self.vx = randint(-self.speed, self.speed)

        self.x += self.vx * t
        self.y += self.vy * t

    def reflection(self):
        if (self.x + self.vx + self.r >= 700) or \
                (self.x + self.vx <= 100):
            k = randint(1, self.speed)
            self.vx = -sign(self.vx) * k
            self.vy = randint(-self.speed, self.speed)

        if (self.y + self.vy + self.r >= 700) or \
                (self.y + self.vy <= 100):
            k = randint(1, self.speed)
            self.vy = -sign(self.vy) * k
            self.vx = randint(-min(abs(self.speed), self.x),
                              min(abs(self.speed), 700 - self.r - self.x))

    def draw_mouse(self):
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, self.color, (self.x + 0.75 * self.r * sign(self.vx), self.y + 0.75 * self.r * sign(self.vy)),
               self.r * 0.5)
        circle(screen, (0, 0, 0), (self.x + 1.10 * self.r * sign(self.vx), self.y + 1.10 * self.r * sign(self.vy)),
               self.r * 0.2)
        line(screen, self.color, (self.x, self.y),
             (self.x - 1.5 * sign(self.vx) * self.r, self.y - 1.5 * self.r * sign(self.vy)), 3)

    def touch_mouse(self, i):
        global points, k, pop_x, pop_y, n
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.r ** 2:
            rodents.pop(i)
            pop_x = self.x
            pop_y = self.y
            k = 0
            n = 3
            points += n


class Rat(Mouse):
    def __init__(self, x1, x2, y1, y2):
        self.r = 30
        self.x = randint(x1, x2)
        self.y = randint(y1, y2)
        self.speed = 5
        self.vx = randint(-self.speed, self.speed)
        self.vy = randint(-self.speed, self.speed)
        self.color = (73, 66, 61)

    def touch_mouse(self, i):
        global points, k, pop_x, pop_y, n
        if (self.x - event.pos[0]) ** 2 + (self.y - event.pos[1]) ** 2 <= self.r ** 2:
            self.r -= 6
            self.speed += 2
            self.vx += sign(self.vx)*randint(15, 20)
            self.vy += sign(self.vy)*randint(15, 20)
            if self.r == 0:
                rodents.pop(i)
            pop_x = self.x
            pop_y = self.y
            k = 0
            n = 1
            points += n


num_of_rodents_rand = number_of_rodents//6
number_of_mice = randint(3*num_of_rodents_rand, 4*num_of_rodents_rand)
number_of_rats = number_of_rodents - number_of_mice
for i in range(number_of_mice):
    rodents.append(Mouse(110, 690, 110, 690))
    rodents[i].draw_mouse()
for i in range(number_of_rats):
    rodents.append(Rat(120, 660, 120, 660))
    rodents[i].draw_mouse()
pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if (event.pos[0] >= 100) and (event.pos[0] <= 300) and (event.pos[1] >= 710):
                save_sec = seconds
                save_min = minutes
                save_points = points
                points = -1
            for i in range(len(rodents) - 1, -1, -1):
                rodents[i].touch_mouse(i)
    pg.display.update()
    screen.fill((255, 255, 255))
    rect(screen, (255, 204, 255), (100, 100, 600, 600))
    font.render_to(screen, (20, 20), "Catpoints: " + str(points), (255, 153, 255))
    timer += 1
    if timer == 30:
        seconds -= 1
        timer = 0
    if seconds == 0 and minutes != 0:
        minutes -= 1
        seconds = 59
    if seconds == 0 and minutes == 0:
        finished = True
    pg.draw.polygon(screen, (255, 153, 255), ((100, 710), (360, 710), (360, 800), (100, 800)), 10)
    font.render_to(screen, (110, 750), "КОТИК УСТАЛ", (255, 153, 255))
    font.render_to(screen, (510, 20), " ВреМЯУ: " + str(minutes) + ' m ' + str(seconds) + ' s', (255, 153, 255))
    if k < 7:
        font.render_to(screen, (pop_x, pop_y), '+' + str(n), (255, 153, 255))
        k += 1
    for i in range(len(rodents)):
        rodents[i].draw_mouse()
        rodents[i].move(1)
        rodents[i].reflection()
    if points == -1:
        screen.fill((255, 255, 255))
        pg.draw.polygon(screen, (255, 153, 255), ((50, 300), (330, 300), (330, 390), (50, 390)), 10)
        font.render_to(screen, (60, 340), "КОТИК УШЕЛ", (255, 153, 255))
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) and (event.pos[0] > 100) and (
                event.pos[0] < 380) and (event.pos[1] > 300) and (event.pos[1] < 390):
            points = save_points
            finished = True
        pg.draw.polygon(screen, (255, 153, 255), ((370, 300), (710, 300), (710, 390), (370, 390)), 10)
        font.render_to(screen, (380, 340), "КОТИК ОТДОХНУЛ", (255, 153, 255))
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) and (event.pos[0] > 450) and (
                event.pos[0] < 790) and (event.pos[1] > 300) and (event.pos[1] < 390):
            seconds = save_sec
            minutes = save_min
            points = save_points
            timer = 0
            rest = False
screen.fill((255, 255, 255))
font.render_to(screen, (100, 100), "Какая кличка у вашего котика? ", (255, 153, 255))
finished = False
name = ""
while finished is False:
    screen.fill((255, 255, 255))
    font.render_to(screen, (100, 100), "Какая кличка у вашего котика? ", (255, 153, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                finished = True
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += pygame.key.name(event.key)
        font.render_to(screen, (100, 140), name, (255, 153, 255))
        pygame.display.update()
with open(r"C:\Users\Asus\PycharmProjects\Karpenko_MIPT_Pythonlabs\Catch the ball\record_table.json") as f:
    data = json.load(f)
data[name] = points
screen.fill((255, 255, 255))
height = 50
for p, v in data.items():
    font.render_to(screen, (20, height), "имя котика : " + p + "  его catpoints: " + str(v), (255, 153, 255))
    height += 40
    if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) and (event.pos[0] > 100) and (
            event.pos[0] < 380) and (event.pos[1] > 300) and (event.pos[1] < 390):
        finished = True
    pygame.display.update()
    finished = False


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
with open(r"C:\Users\Asus\PycharmProjects\Karpenko_MIPT_Pythonlabs\Catch the ball\record_table.json", 'w') as f:
    json.dump(data, f)

pg.quit()
