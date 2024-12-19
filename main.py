import pygame as pg
import sys
from hole import Hole
from animation import Animate
from menu import Menu
from course import Course

# Game Settings
RES = WIDTH, HEIGHT = 320, 480
FPS = 60


clubs = {
        "DR": {"distance": 305, "accuracy": 150, "angle": 11},  # Driver
        "3W": {"distance": 220, "accuracy": 120, "angle": 11},  # Driver
        "5W": {"distance": 205, "accuracy": 90, "angle": 11},  # Driver
        "4I": {"distance": 190, "accuracy": 80, "angle": 11},  # Driver
        "5I": {"distance": 175, "accuracy": 70, "angle": 11},  # Driver
        "6I": {"distance": 160, "accuracy": 60, "angle": 11},  # Driver
        "7I": {"distance": 145, "accuracy": 50, "angle": 11},  # Driver
        "8I": {"distance": 130, "accuracy": 40, "angle": 11},  # Driver
        "9I": {"distance": 115, "accuracy": 30, "angle": 40},  # Driver
        "PW": {"distance": 100, "accuracy": 25, "angle": 48},  # Driver
        "GW": {"distance": 85, "accuracy": 25, "angle": 48},  # Driver
        "SW": {"distance": 70, "accuracy": 20, "angle": 56},  # Driver
        "LW": {"distance": 55, "accuracy": 20, "angle": 56},  # Driver
}


class Game:
    def __init__(self):
        # Start Pygame window and call new game function
        pg.init()
        self.screen = pg.display.set_mode(RES)  # .set_mode(RES, pg.NOFRAME) to remove menu bar
        self.clock = pg.time.Clock()

        self.onMenu = False
        self.onStartAnimation = True
        # self.onStartAnimation = False
        # self.onMenu = True
        self.play = False
        self.onShop = False
        self.music = pg.mixer.Sound('assets/sound/mainTheme.mp3')
        self.hole = None
        self.menu = None
        # self.menu = Menu(self)
        self.shop = None

        self.startAnimate = Animate(self)
        # self.startAnimate = None
        # self.menu = Menu(self)

        self.onCourse = False
        self.course = None

        # Create a surface for the fade effect
        self.fade_surface = pg.Surface((320, 480))
        self.fade_surface.fill('black')




        # self.new_game()

    def new_menu(self):
        self.menu = Menu(self)
        self.onMenu = True

    def new_game(self):
        self.play = True
        birdSound = pg.mixer.Sound('assets/sound/effects/backgroundBirds.mp3')
        birdSound.play(-1)
        self.hole = Hole(4, 3, 0, self, "Beldale", "3", 12, 58, 11, 7, clubs)
        # self.hole = Hole(3, 13, 1, self, "Beldale", "4", 10, 40, 8, 16, clubs)
        # self.hole = Hole(3, 13, 1, self, "Beldale", "5", 10, 56, 39, 19, clubs)

        # self.map = Map(self)
        pass

    def fade_in(self, screen, fade_surface, duration):
        """Fade in the screen."""
        for alpha in range(255, -1, -5):  # Gradually decrease alpha
            fade_surface.set_alpha(alpha)
            # screen.fill('white')  # Background color
            self.draw()
            screen.blit(fade_surface, (0, 0))
            pg.display.flip()
            pg.time.delay(duration)

    def fade_out(self, screen, fade_surface, duration):
        """Fade out the screen."""
        for alpha in range(0, 256, 5):  # Gradually increase alpha
            fade_surface.set_alpha(alpha)
            # screen.fill('white')  # Background color
            screen.blit(fade_surface, (0, 0))
            pg.display.flip()
            pg.time.delay(duration)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        # pg.display.set_caption('Retro Golf')

        if self.onStartAnimation:
            self.startAnimate.update()

        if self.onMenu:
            self.menu.move()

        if self.play:
            self.hole.run()

        if self.onShop:
            self.shop.update()

        if self.onCourse:
            self.course.update()



    def draw(self):
        if self.onCourse:
            self.course.draw(self.screen)

        if self.onStartAnimation:
            self.startAnimate.draw(self.screen)

        if self.onMenu:
            self.menu.draw(self.screen)

        if self.play:
            self.hole.draw(self.screen)

        if self.onShop:
            self.shop.draw(self.screen)

        # self.screen.fill('white')
        # self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
