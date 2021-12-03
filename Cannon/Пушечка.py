import math
from random import choice
import pygame as pg
from pygame.draw import *
from random import randint, random
from pygame.locals import *
import pygame.freetype
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
points = 0
anti = False
gun_y = 0
def sign(x):
    """
    Функция, возвращающая знак полученной переменной
    """
    if x >= 0:
        return 1
    else:
        return -1

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = -4
        self.color = MAGENTA
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.vy += self.g
        if not (0 < self.x - self.r + self.vx < WIDTH):
            self.vx = - self.vx / 2
        if not (0 < self.y - self.r - self.vy < HEIGHT - 50):
            self.vy = - self.vy / 2

        self.live -= 1
        self.x += self.vx
        self.y -= self.vy



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            obj.live = 0
            return True
        else:
            return False

class anti_Ball(Ball):
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 4
        self.color = MAGENTA
        self.live = 30


class Gun:
    def __init__(self, screen, x = 30, y = 460):
        self.screen = screen
        self.f2_power = 40
        self.f2_on = 0
        self.an = 1
        self.type_bullet = 1
        self.x = x
        self.y = y
        self.r = 50
        self.color = GREY


    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, anti
        balls = []
        bullet += 1
        self.x0 = math.cos(self.an) * self.f2_power + self.x
        self.y0 = math.sin(self.an) * self.f2_power + self.y
        if not anti:
            self.new_ball = Ball(self.screen, self.x0 , self.y0 )
        else:
            self.new_ball = anti_Ball(self.screen, self.x0 , self.y0 )
        self.new_ball.r += 5
        self.an = math.atan2((event.pos[1]-self.new_ball.y), (event.pos[0]-self.new_ball.x))
        self.new_ball.vx = self.f2_power * math.cos(self.an)
        self.new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(self.new_ball)
        self.f2_on = 0
        self.f2_power = 10



    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)
        line(screen, BLUE, (self.x, self.y), ( math.cos(self.an) *
                                                    self.f2_power + self.x,
                                                    math.sin(self.an) * self.f2_power + self.y), width=15)
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self):
      self.live = 1
      self.new_target()
    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(620, 650)
        self.y = randint(50, 550)
        self.r = randint(10, 50)
        self.color = RED

    def hit(self):
        global balls,  points
        """Попадание шарика в цель."""
        points += 1
        balls = []

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


class Mouse(Target):
    """
    Создание класса мышей
    """
    def __init__(self):
        self.live = 1
        self.new_target()
        self.color = (153, 153, 153)
        self.speed = 15
        self. r = randint(20, 30)
        self.vy = randint(-self.speed, self.speed)
    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(580, 610)
        self.y = randint(50, 550)
    def move(self,t):
        global gun_y
        """
        Функция движения мышей
        """
        if self.vy == 0:
            self.vy = randint(-self.speed, self.speed)

        if (self.y + self.vy + self.r >= HEIGHT) or \
                (self.y + self.vy <= 50):
            el = randint(1, self.speed)
            self.vy = -sign(self.vy) * el
        self.y += self.vy * t
        if self.y == gun_y :
            self.vy = 0



    def draw_mouse(self):
        """
        Функция рисования мыши
        """
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, self.color, (self.x, self.y +  self.r * sign(self.vy)),
               self.r * 0.5)
        circle(screen, (0, 0, 0), (self.x, self.y + 1.50 * self.r * sign(self.vy)),
               self.r * 0.2)
        line(screen, self.color, (self.x, self.y),
             (self.x,
              self.y - 1.5 * self.r * sign(self.vy)), 3)

    def draw_scared_mouse(self):
        """
        Функция рисования мыши
        """
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, self.color, (self.x - 1.50 * self.r , self.y, self.r * 0.5))
        circle(screen, (0, 0, 0), (self.x - 1.50 * self.r, self.y ), self.r * 0.2)
        line(screen, self.color, (self.x, self.y),
             (self.x - 1.5 * self.r, self.y), 3)


class Rat(Mouse):
    """
    Создаем класс крысс, наследующий функции
    рисования мышей, движения мышей,
    и отражения мышей от стен
    """
    def __init__(self):
        self.live = 1
        self.r = randint(20, 30)
        self.new_target()
        self.speed = 15
        self.vy = randint(-self.speed, self.speed)
        self.color = (73, 66, 61)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(700, 780)
        self.y = randint(50, 550)





pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
mouse = Mouse()
rat = Rat()
finished = False

while not finished:
    screen.fill(WHITE)
    font = pygame.freetype.SysFont('Times New Roman', 25)
    font.render_to(screen, (20, 20), "Points: " +
                   str(points), (BLACK))  # выводим кол-во очков на экран
    gun.draw()
    target.draw()
    mouse.draw_mouse()
    rat.draw_mouse()
    mouse.move(1)
    rat.move(1)

    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN  and pygame.mouse.get_pressed()[0]:
            anti = False
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            anti = True
            gun.fire2_start(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or pygame.K_UP:
                gun.y -= 10
                gun_y = gun.y
            elif event.key == pygame.K_s or pygame.K_DOWN:
                gun.y += 10
                gun_y = gun.y

    for b in balls:
        b.move()
        if b.hittest(target):
            target.live = 0
            target.hit()
            target.new_target()
        if b.hittest(mouse):
            mouse.live = 0
            mouse.hit()
            mouse.new_target()
        if b.hittest(rat):
            rat.live = 0
            rat.hit()
            rat.new_target()
    gun.power_up()


pygame.quit()