import pygame as pg
from card import Card


class Course:
    def __init__(self, game):
        self.game = game
        self.backgroundImg = pg.image.load(f'assets/Menu/background.png')
        self.backgroundImg = pg.transform.scale(self.backgroundImg, (320, 480))
        self.cards = []
        self.cards_x = []
        self.justPressed = [True, True, True, True]
        self.pos = 0
        self.moveLeft = [False, 0]
        self.moveRight = [False, 0]
        self.sounds = []
        cancelSound = pg.mixer.Sound("assets/sound/effects/cancel.mp3")
        startSound = pg.mixer.Sound("assets/sound/effects/buying.wav")
        self.sounds.append(cancelSound)
        self.sounds.append(startSound)


        self.get_courses()

    def get_courses(self):
        x = 34
        card1 = Card("Beldale", 72, 18, 2, [2000, 500, 250], False)
        card2 = Card("Tour Championship", 71, 18, 4.5, [100000, 50000, 25000], True)
        card3 = Card("Pebble Beach", 70, 18, 3, [2000, 500, 250], True)

        self.cards.append(card1)
        self.cards_x.append(x)
        x += 22 + 258

        self.cards.append(card2)
        self.cards_x.append(x)
        x += 22 + 258

        self.cards.append(card3)
        self.cards_x.append(x)

    # def fade_in(self, screen, fade_surface, duration):
    #     """Fade in the screen."""
    #     for alpha in range(255, -1, -5):  # Gradually decrease alpha
    #         fade_surface.set_alpha(alpha)
    #         # screen.fill('white')  # Background color
    #         if self.game.play:
    #             self.game.hole.draw(screen)
    #
    #         screen.blit(fade_surface, (0, 0))
    #         pg.display.flip()
    #         pg.time.delay(duration)
    #
    # def fade_out(self, screen, fade_surface, duration):
    #     """Fade out the screen."""
    #     for alpha in range(0, 256, 5):  # Gradually increase alpha
    #         fade_surface.set_alpha(alpha)
    #         # screen.fill('white')  # Background color
    #         screen.blit(fade_surface, (0, 0))
    #         pg.display.flip()
    #         pg.time.delay(duration)

    def draw(self, screen):
        screen.blit(self.backgroundImg, (0, 0))
        for i in range(0, len(self.cards)):
            self.cards[i].draw_card(screen, self.cards_x[i], 20)


    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            if not self.justPressed[0]:
                self.justPressed[0] = True
                if not self.moveLeft[0] and not self.moveRight[0]:
                    if self.pos < len(self.cards) - 1:
                        self.pos += 1
                        for i in range(0, len(self.cards_x)):
                            self.moveRight[0] = True
        else:
            self.justPressed[0] = False

        if keys[pg.K_LEFT]:
            if not self.justPressed[1]:
                self.justPressed[1] = True
                if not self.moveLeft[0] and not self.moveRight[0]:
                    if self.pos > 0:
                        self.pos -= 1
                        for i in range(0, len(self.cards_x)):
                            self.moveLeft[0] = True
        else:
            self.justPressed[1] = False

        if self.moveRight[0]:
            if self.moveRight[1] < 280:
                for i in range(0, len(self.cards_x)):
                    self.cards_x[i] -= 28
                self.moveRight[1] += 28
            else:
                self.moveRight[1] = 0
                self.moveRight[0] = False

        if self.moveLeft[0]:
            if self.moveLeft[1] < 280:
                for i in range(0, len(self.cards_x)):
                    self.cards_x[i] += 28
                self.moveLeft[1] += 28
            else:
                self.moveLeft[1] = 0
                self.moveLeft[0] = False

        if keys[pg.K_x]:
            if not self.justPressed[2]:
                self.justPressed[2] = True

                if self.cards[self.pos].lock:
                    self.sounds[0].play()
                else:
                    self.sounds[1].play()
                    self.game.fade_out(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay
                    self.game.onCourse = False
                    self.game.course = None
                    self.game.new_game()
                    self.game.music.stop()
                    self.game.fade_in(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay

        else:
            self.justPressed[2] = False

        if keys[pg.K_z]:
            self.sounds[0].play()
            self.game.fade_out(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay
            self.game.onCourse = False
            self.game.course = None
            self.game.new_menu()
            self.game.fade_in(self.game.screen, self.game.fade_surface, 30)  # Fade out with 30ms delay

