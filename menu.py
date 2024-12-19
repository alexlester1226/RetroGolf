import pygame as pg
from shop import Shop
from course import Course


class Menu:
    def __init__(self, game):
        self.game = game
        self.imgs = []
        self.fonts = []
        self.sounds = []
        self.pos = 0
        self.colours = [[255, 117, 27], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.justPressed = [False, False]



        self.get_imgs_sounds_fonts()

    def get_imgs_sounds_fonts(self):
        backgroundImg = pg.image.load(f'assets/Menu/background.png')
        backgroundImg = pg.transform.scale(backgroundImg, (320, 480))
        self.imgs.append(backgroundImg)

        boxImg = pg.image.load(f'assets/OptionBox.png')
        # boxImg = pg.transform.rotate(boxImg, 90)
        boxImg = pg.transform.scale(boxImg, (200, 60))
        self.imgs.append(boxImg)

        # Fonts
        font_path = "assets/Fonts/letters.ttf"
        title_font = pg.font.Font(font_path, 45)
        self.fonts.append(title_font)

        item_font = pg.font.Font(font_path, 35)
        self.fonts.append(item_font)

        # Sounds
        nextSound = pg.mixer.Sound("assets/sound/effects/next.wav")
        self.sounds.append(nextSound)

        backSound = pg.mixer.Sound("assets/sound/effects/cancel.mp3")
        self.sounds.append(backSound)


    def move(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_DOWN]:
            if not self.justPressed[0]:
                self.justPressed[0] = True

                self.colours[self.pos] = [0, 0, 0]
                self.pos += 1
                self.pos = self.pos % 4
                self.colours[self.pos] = [255, 117, 27]
        else:
            self.justPressed[0] = False

        if keys[pg.K_UP]:
            if not self.justPressed[1]:
                self.justPressed[1] = True
                self.colours[self.pos] = [0, 0, 0]
                self.pos -= 1
                self.pos = self.pos % 4
                self.colours[self.pos] = [255, 117, 27]
        else:
            self.justPressed[1] = False

        if keys[pg.K_x]:
            self.game.onMenu = False
            self.game.menu = None
            self.sounds[0].play()

            if self.pos == 0:
                self.game.course = Course(self.game)
                self.game.onCourse = True
                self.game.fade_out(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay
                self.game.fade_in(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay

                # self.game.play = True
                # self.game.new_game()
                # self.game.music.stop()

            if self.pos == 1:
                self.game.onShop = True
                self.game.shop = Shop(self.game)
                self.game.fade_out(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay
                self.game.fade_in(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay

    def draw(self, screen):
        # Green - (85, 107, 47) Orange - (255, 117, 27)
        screen.blit(self.imgs[0], (0, 0))
        title_label = self.fonts[0].render(f"Retro Golf", False, (0, 0, 0))
        play_label = self.fonts[1].render(f"Play", False, (self.colours[0][0], self.colours[0][1], self.colours[0][2]))
        shop_label = self.fonts[1].render(f"Shop", False, (self.colours[1][0], self.colours[1][1], self.colours[1][2]))
        locker_label = self.fonts[1].render(f"Locker", False, (self.colours[2][0], self.colours[2][1], self.colours[2][2]))
        controls_label = self.fonts[1].render(f"Controls", False, (self.colours[3][0], self.colours[3][1], self.colours[3][2]))

        # print(title_label.get_size())
        screen.blit(title_label, (30, 35))
        screen.blit(play_label, (70, 110))
        screen.blit(shop_label, (70, 160))
        screen.blit(locker_label, (70, 210))
        screen.blit(controls_label, (70, 260))



        # for i in range(0, 4):
        #     screen.blit(self.imgs[1], (52, 160 + i * 80))


        x=0 # logic for playing

