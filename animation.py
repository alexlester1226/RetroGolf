import pygame as pg

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLACK = (0, 0, 0)


class Animate:
    def __init__(self, game):
        self.time_left = None
        self.game = game
        self.img = []
        self.counter = 0
        self.pos = 0
        self.done = False
        self.sound = pg.mixer.Sound('assets/sound/effects/introsound.mp3')
        self.play = False
        self.colour = [0, 0, 0]
        self.highlight = True
        self.reset_ticks = 0
        self.got_reset = False
        self.font = []
        self.snake = True
        self.snake_pos = [-310, 80]
        self.snake_counters = [0, 0]


        # Timer setup
        self.start_time = 15 # Set the countdown in seconds
        self.clock = pg.time.Clock()

        self.get_images()

    def get_images(self):

        intro = []
        for i in range(0, 85):
            img = pg.image.load(f'assets/Intro/intro_{i}.png')
            img = pg.transform.scale(img, (320, 480))
            intro.append(img)
        self.img.append(intro)

        snake = []
        for i in range(1, 8):
            snakeImg = pg.image.load(f'assets/Intro/Snake/snake-{i}.tiff')
            snakeImg = pg.transform.rotate(snakeImg, -90)
            snakeImg = pg.transform.scale(snakeImg, (300, 150))
            snake.append(snakeImg)
        self.img.append(snake)

        pygameImg = pg.image.load("assets/Intro/Snake/pygame.png")
        pygameImg = pg.transform.scale(pygameImg, (260, 95))
        self.img.append(pygameImg)



        font_path = "assets/Fonts/letters.ttf"
        title_font = pg.font.Font(font_path, 50)
        self.font.append(title_font)




    def get_adjusted_ticks(self):
        return pg.time.get_ticks() - self.reset_ticks

    def update(self):
        # Get adjusted time
        self.time_left = self.start_time - self.get_adjusted_ticks() // 1000
        self.update_colour()

    def update_colour(self):
        if self.highlight:
            self.colour[0] += 1
            self.colour[1] += 1
            self.colour[2] += 1

            if self.colour[0] > 255:
                self.highlight = False

    def draw(self, screen):
        if self.highlight:
            screen.fill((self.colour[0], self.colour[1], self.colour[2]))
        else:
            screen.fill('white')
            screen.blit(self.img[2], (30, 100))
            if self.snake_pos[0] > -20:
                pg.draw.rect(screen, 'white', (self.snake_pos[0] + 50, 100, 300, 95))
            else:
                pg.draw.rect(screen, 'white', (30, 100, 260, 95))


            if self.snake:
                if self.snake_counters[0] > 6:
                    self.snake_counters[0] = 0
                    self.snake_counters[1] += 1

                if self.snake_counters[1] > 6:
                    self.snake_counters[1] = 0

                self.snake_counters[0] += 1
                self.snake_pos[0] += 1

                screen.blit(self.img[1][self.snake_counters[1]], (self.snake_pos[0], self.snake_pos[1]))

                if self.snake_pos[0] > 450:
                    self.snake = False
            else:
                if not self.play:
                    self.sound.play()
                    self.play = True

                if not self.done:
                    if self.counter > 5:
                        self.pos += 1
                        self.counter = 0

                    if self.pos > 84:
                        self.pos = 84

                    if self.counter == 5 and self.pos == 84:
                        self.done = True
                        self.reset_ticks = pg.time.get_ticks()


                    screen.blit(self.img[0][self.pos], (0, 0))
                    self.counter += 1

                else:
                    if self.time_left > 13:
                        screen.blit(self.img[0][self.pos], (0, 0))
                    elif self.time_left > 10:
                        screen.fill('black')

                    elif self.time_left > 7:
                        screen.fill('black')
                        text = self.font[0].render("Lester GD", False, 'white')
                        screen.blit(text, (20, 20))

                    elif self.time_left > 4:
                        screen.fill('black')
                        text = self.font[0].render("Lester GD", False, 'white')
                        text2 = self.font[0].render("Presents", False, 'white')

                        screen.blit(text, (20, 20))
                        screen.blit(text2, (20, 120))

                    else:
                        self.game.new_menu()
                        self.game.onStartAnimation = False
                        self.game.startAnimate = None
                        self.game.music.play(-1)


