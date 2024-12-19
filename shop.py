import pygame as pg

class Shop:
    def __init__(self, game):
        self.game = game
        self.imgs = []
        self.fonts = []
        self.pos = [0, 0]
        self.title_colours = [[255, 117, 27], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.cost_colours = [[[255, 117, 27], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0,0]],
                             [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                             [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        self.justPressed = [False, False, False, False]
        self.coins = 0
        self.clubLevels = []
        self.coin_sprite_sheet = pg.image.load('assets/coins.png').convert_alpha()
        self.coinAnimation = [0, 0]

        self.get_saved_info()
        self.get_images_fonts()


    def get_saved_info(self):
        self.clubLevels = [1, 3, 0, 2, 1]
        self.coins = 234310

    def get_images_fonts(self):
        backgroundImg = pg.image.load(f'assets/Menu/background.png')
        backgroundImg = pg.transform.scale(backgroundImg, (320, 480))
        self.imgs.append(backgroundImg)

        boxImg = pg.image.load(f'assets/OptionBox.png')
        # boxImg = pg.transform.rotate(boxImg, 90)
        boxImg = pg.transform.scale(boxImg, (200, 60))
        self.imgs.append(boxImg)

        coinImgs = []
        for i in range(0, 5):
            sprite = self.get_sprite(i, 0)
            sprite.set_colorkey((0, 0, 0))
            pg.Surface.convert_alpha(sprite)
            coinImgs.append(sprite)
        self.imgs.append(coinImgs)

        # Fonts
        font_path = "assets/Fonts/letters.ttf"
        title_font = pg.font.Font(font_path, 45)
        self.fonts.append(title_font)

        item_font = pg.font.Font(font_path, 25)
        self.fonts.append(item_font)

        font2 = pg.font.Font(font_path, 20)
        self.fonts.append(font2)

        font3 = pg.font.Font(font_path, 10)
        self.fonts.append(font3)





    def get_sprite(self, x, y):
        # Extract a specific sprite from the sprite sheet
        sprite = pg.Surface((16, 16))  # Create a surface for the sprite
        sprite.blit(self.coin_sprite_sheet, (0, 0), (x * 16, y * 16, 16, 16))  # Blit the desired sprite
        return sprite

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_DOWN]:
            if not self.justPressed[0]:
                self.justPressed[0] = True

                self.title_colours[self.pos[0]] = [0, 0, 0]
                self.cost_colours[self.pos[0]][self.pos[1]] = [0, 0, 0]

                self.pos[0] += 1
                self.pos[0] = self.pos[0] % 5
                self.title_colours[self.pos[0]] = [255, 117, 27]
                self.cost_colours[self.pos[0]][self.pos[1]] = [255, 117, 27]

        else:
            self.justPressed[0] = False

        if keys[pg.K_UP]:
            if not self.justPressed[1]:
                self.justPressed[1] = True
                self.title_colours[self.pos[0]] = [0, 0, 0]
                self.cost_colours[self.pos[0]][self.pos[1]] = [0, 0, 0]
                self.pos[0] -= 1
                self.pos[0] = self.pos[0] % 5
                self.title_colours[self.pos[0]] = [255, 117, 27]
                self.cost_colours[self.pos[0]][self.pos[1]] = [255, 117, 27]
        else:
            self.justPressed[1] = False


        if keys[pg.K_RIGHT]:
            if not self.justPressed[2]:
                self.justPressed[2] = True
                self.cost_colours[self.pos[0]][self.pos[1]] = [0, 0, 0]
                self.pos[1] += 1
                self.pos[1] = self.pos[1] % 4
                self.cost_colours[self.pos[0]][self.pos[1]] = [255, 117, 27]
        else:
            self.justPressed[2] = False

        if keys[pg.K_LEFT]:
            if not self.justPressed[3]:
                self.justPressed[3] = True
                self.cost_colours[self.pos[0]][self.pos[1]] = [0, 0, 0]
                self.pos[1] -= 1
                self.pos[1] = self.pos[1] % 4
                self.cost_colours[self.pos[0]][self.pos[1]] = [255, 117, 27]
        else:
            self.justPressed[3] = False

        if keys[pg.K_z]:
            self.game.onShop = False
            self.game.shop = None
            self.game.new_menu()
            self.game.menu.sounds[1].play()
            self.game.fade_out(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay
            self.game.fade_in(self.game.screen, self.game.fade_surface, 30)  # Fade in with 30ms delay


    def draw(self, screen):
        screen.blit(self.imgs[0], (0, 0))
        title_label = self.fonts[0].render(f"Shop", False, (0, 0, 0))
        coin_label = self.fonts[1].render(f"{self.coins}", False, (0, 0, 0))

        driver_label = self.fonts[2].render(f"Driver", False, (self.title_colours[0][0], self.title_colours[0][1], self.title_colours[0][2]))
        woods_label = self.fonts[2].render(f"Woods", False, (self.title_colours[1][0], self.title_colours[1][1], self.title_colours[1][2]))
        irons_label = self.fonts[2].render(f"Irons", False, (self.title_colours[2][0], self.title_colours[2][1], self.title_colours[2][2]))
        wedges_label = self.fonts[2].render(f"Wedges", False, (self.title_colours[3][0], self.title_colours[3][1], self.title_colours[3][2]))
        putter_label = self.fonts[2].render(f"Putter", False, (self.title_colours[4][0], self.title_colours[4][1], self.title_colours[4][2]))

        driver_price1_label = self.fonts[3].render(f"1000", False, (self.cost_colours[0][0][0], self.cost_colours[0][0][1], self.cost_colours[0][0][2]))
        driver_price2_label = self.fonts[3].render(f"5000", False, (self.cost_colours[0][1][0], self.cost_colours[0][1][1], self.cost_colours[0][1][2]))
        driver_price3_label = self.fonts[3].render(f"50000", False, (self.cost_colours[0][2][0], self.cost_colours[0][2][1], self.cost_colours[0][2][2]))
        driver_price4_label = self.fonts[3].render(f"100000", False, (self.cost_colours[0][3][0], self.cost_colours[0][3][1], self.cost_colours[0][3][2]))

        woods_price1_label = self.fonts[3].render(f"750", False, (self.cost_colours[1][0][0], self.cost_colours[1][0][1], self.cost_colours[1][0][2]))
        woods_price2_label = self.fonts[3].render(f"3750", False, (self.cost_colours[1][1][0], self.cost_colours[1][1][1], self.cost_colours[1][1][2]))
        woods_price3_label = self.fonts[3].render(f"37500", False, (self.cost_colours[1][2][0], self.cost_colours[1][2][1], self.cost_colours[1][2][2]))
        woods_price4_label = self.fonts[3].render(f"75000", False, (self.cost_colours[1][3][0], self.cost_colours[1][3][1], self.cost_colours[1][3][2]))

        iron_price1_label = self.fonts[3].render(f"2000", False, (self.cost_colours[2][0][0], self.cost_colours[2][0][1], self.cost_colours[2][0][2]))
        iron_price2_label = self.fonts[3].render(f"10000", False, (self.cost_colours[2][1][0], self.cost_colours[2][1][1], self.cost_colours[2][1][2]))
        iron_price3_label = self.fonts[3].render(f"100000", False, (self.cost_colours[2][2][0], self.cost_colours[2][2][1], self.cost_colours[2][2][2]))
        iron_price4_label = self.fonts[3].render(f"200000", False, (self.cost_colours[2][3][0], self.cost_colours[2][3][1], self.cost_colours[2][3][2]))

        wedge_price1_label = self.fonts[3].render(f"750", False, (self.cost_colours[3][0][0], self.cost_colours[3][0][1], self.cost_colours[3][0][2]))
        wedge_price2_label = self.fonts[3].render(f"3750", False, (self.cost_colours[3][1][0], self.cost_colours[3][1][1], self.cost_colours[3][1][2]))
        wedge_price3_label = self.fonts[3].render(f"37500", False, (self.cost_colours[3][2][0], self.cost_colours[3][2][1], self.cost_colours[3][2][2]))
        wedge_price4_label = self.fonts[3].render(f"75000", False, (self.cost_colours[3][3][0], self.cost_colours[3][3][1], self.cost_colours[3][3][2]))

        putter_price1_label = self.fonts[3].render(f"750", False, (self.cost_colours[4][0][0], self.cost_colours[4][0][1], self.cost_colours[4][0][2]))
        putter_price2_label = self.fonts[3].render(f"3750", False, (self.cost_colours[4][1][0], self.cost_colours[4][1][1], self.cost_colours[4][1][2]))
        putter_price3_label = self.fonts[3].render(f"37500", False, (self.cost_colours[4][2][0], self.cost_colours[4][2][1], self.cost_colours[4][2][2]))
        putter_price4_label = self.fonts[3].render(f"75000", False, (self.cost_colours[4][3][0], self.cost_colours[4][3][1], self.cost_colours[4][3][2]))

        screen.blit(title_label, (30, 35))
        screen.blit(coin_label, (320 - coin_label.get_size()[0] - 10, 12))

        if self.coinAnimation[0] > 10:
            self.coinAnimation[1] += 1
            self.coinAnimation[0] = 0

        if self.coinAnimation[1] > 4:
            self.coinAnimation[1] = 0

        self.coinAnimation[0] += 1

        coin_x = 320 - 31 - coin_label.get_size()[0]

        screen.blit(self.imgs[2][self.coinAnimation[1]], (coin_x, 16))




        screen.blit(driver_label, (20, 120))
        screen.blit(woods_label, (20, 170))
        screen.blit(irons_label, (20, 220))
        screen.blit(wedges_label, (20, 270))
        screen.blit(putter_label, (20, 320))

        screen.blit(driver_price1_label, (115, 112))
        screen.blit(driver_price2_label, (165, 112))
        screen.blit(driver_price3_label, (215, 112))
        screen.blit(driver_price4_label, (262, 112))

        screen.blit(woods_price1_label, (115, 162))
        screen.blit(woods_price2_label, (165, 162))
        screen.blit(woods_price3_label, (215, 162))
        screen.blit(woods_price4_label, (262, 162))

        screen.blit(iron_price1_label, (115, 212))
        screen.blit(iron_price2_label, (165, 212))
        screen.blit(iron_price3_label, (212, 212))
        screen.blit(iron_price4_label, (262, 212))

        screen.blit(wedge_price1_label, (115, 262))
        screen.blit(wedge_price2_label, (165, 262))
        screen.blit(wedge_price3_label, (215, 262))
        screen.blit(wedge_price4_label, (262, 262))

        screen.blit(putter_price1_label, (115, 312))
        screen.blit(putter_price2_label, (165, 312))
        screen.blit(putter_price3_label, (215, 312))
        screen.blit(putter_price4_label, (262, 312))



        rect_x = 110
        rect_y = 125
        for k in range(0, 5):
            for i in range(0, 4):
                # Draw a rectangle with rounded corners
                rect = pg.Rect(rect_x, rect_y, 40, 10)  # x, y, width, height
                border_radius = 20  # Radius for rounded corners
                pg.draw.rect(screen, (0, 0, 0), rect, border_radius=border_radius)

                if self.clubLevels[k] > i:
                    rect = pg.Rect(rect_x + 1, rect_y + 1, 38, 8)  # x, y, width, height
                    pg.draw.rect(screen, (150, 255, 0), rect, border_radius=border_radius)

                rect_x += 50
            rect_y += 50
            rect_x = 110

        rect = pg.Rect(111, 126, 38, 8)  # x, y, width, height
        border_radius = 20  # Radius for rounded corners
        pg.draw.rect(screen, (150, 255, 0), rect, border_radius=border_radius)

