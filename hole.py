import pygame as pg
import pandas as pd
import math
import random
from pygame.draw import circle, line


class Hole:
    def __init__(self, par, wind, direction, game, course, hole, playerX, playerY, flagX, flagY, clubs):
        self.par = par
        self.hole = hole
        self.wind = wind
        self.direction = direction
        self.hole_layout = self.get_hole_layout(course, hole)
        self.game = game
        self.flag_num = [0, 0]
        self.flag = [flagX, flagY]
        self.img = []
        self.font = []
        self.sound = []
        self.player = [playerX, playerY, "Tee"]
        self.map_coordinates = self.get_map()
        self.dx = 0
        self.dy = 0
        self.arrow = ["↑", "→", "↓", "←"]
        self.get_images_fonts()
        self.currentShot = 0
        self.getShotData = [False, False, False]
        self.powerBarSize = [[0, False], [0, False]]
        self.clubs = clubs
        self.clubSelection = 0
        self.justClicked = [True, True]
        self.aim = [0, -50, 0]
        self.test = [False, 0, 0]
        self.shot_data = [0, 0, 0, 0]
        self.club_Str = ["DR", "3W", "5W", "4I", "5I", "6I", "7I", "8I", "9I", "PW", "GW", "SW", "LW"]
        self.animate = False
        self.animation = [False, False]
        self.swing_num = [0, 0]
        self.waterCounter = [0, 0, False, 0, 0]
        self.OB_counter = [0, False]
        self.old_map_coordinates = [0, 0]


        # Define a dictionary for the tile configurations
        self.tile_configs = {
            1: {"sprite_x": 13, "sprite_y": 10, "flag": False, "tree": False},  # Rough 1
            9: {"sprite_x": 12, "sprite_y": 10, "flag": False, "tree": False},  # Rough 2
            5: {"sprite_x": 2, "sprite_y": 0, "flag": False, "tree": False},  # Rough NE
            6: {"sprite_x": 3, "sprite_y": 0, "flag": False, "tree": False},  # Rough SE
            7: {"sprite_x": 0, "sprite_y": 0, "flag": False, "tree": False},  # Rough SE
            8: {"sprite_x": 1, "sprite_y": 0, "flag": False, "tree": False},  # Rough SE
            2: {"sprite_x": 5, "sprite_y": 11, "flag": False, "tree": False},  # Green 1
            14: {"sprite_x": 6, "sprite_y": 11, "flag": False, "tree": False},  # Green 2
            11: {"sprite_x": 5, "sprite_y": 5, "flag": False, "tree": False},  # Green NW
            10: {"sprite_x": 4, "sprite_y": 5, "flag": False, "tree": False},  # Green NE
            13: {"sprite_x": 7, "sprite_y": 5, "flag": False, "tree": False},  # Green SE
            12: {"sprite_x": 6, "sprite_y": 5, "flag": False, "tree": False},  # Green SW
            3: {"sprite_x": 3, "sprite_y": 11, "flag": False, "tree": False},  # Bunker
            19: {"sprite_x": 2, "sprite_y": 11, "flag": False, "tree": False},  # Bunker
            15: {"sprite_x": 8, "sprite_y": 8, "flag": False, "tree": False},  # Bunker
            16: {"sprite_x": 9, "sprite_y": 8, "flag": False, "tree": False},  # Bunker
            18: {"sprite_x": 10, "sprite_y": 8, "flag": False, "tree": False},  # Bunker
            17: {"sprite_x": 11, "sprite_y": 8, "flag": False, "tree": False},  # Bunker
            4: {"sprite_x": 7, "sprite_y": 11, "flag": True, "tree": False},  # Hole
            20: {"sprite_x": 11, "sprite_y": 10, "flag": False, "tree": False},  # Fairway
            0: {"sprite_x": 10, "sprite_y": 10, "flag": False, "tree": False},  # Fairway
            21: {"sprite_x": 0, "sprite_y": 8, "flag": False, "tree": False},  # Water
            22: {"sprite_x": 1, "sprite_y": 8, "flag": False, "tree": False},  # Water
            23: {"sprite_x": 5, "sprite_y": 8, "flag": False, "tree": False},  # Water
            24: {"sprite_x": 3, "sprite_y": 8, "flag": False, "tree": False},  # Water
            25: {"sprite_x": 2, "sprite_y": 8, "flag": False, "tree": False},  # Water
            26: {"sprite_x": 4, "sprite_y": 8, "flag": False, "tree": False},  # Water
            27: {"sprite_x": 2, "sprite_y": 9, "flag": False, "tree": False},  # Water
            28: {"sprite_x": 1, "sprite_y": 9, "flag": False, "tree": False},  # Water
            29: {"sprite_x": 0, "sprite_y": 9, "flag": False, "tree": False},  # Water
            30: {"sprite_x": 3, "sprite_y": 9, "flag": False, "tree": False},  # Water
            32: {"sprite_x": 5, "sprite_y": 11, "flag": False, "tree": False},  # Tee Box
            31: {"sprite_x": 1, "sprite_y": 11, "flag": False, "tree": False},  # Deep Rough
            33: {"sprite_x": 1, "sprite_y": 10, "flag": False, "tree": False},  # Deep Rough
            34: {"sprite_x": 2, "sprite_y": 10, "flag": False, "tree": False},  # Deep Rough
            35: {"sprite_x": 13, "sprite_y": 9, "flag": False, "tree": False},  # Deep Rough
            36: {"sprite_x": 14, "sprite_y": 9, "flag": False, "tree": False},  # Deep Rough
            37: {"sprite_x": 10, "sprite_y": 5, "flag": False, "tree": False},  # Green (water)
            38: {"sprite_x": 9, "sprite_y": 5, "flag": False, "tree": False},  # Green (water)
            39: {"sprite_x": 8, "sprite_y": 5, "flag": False, "tree": False},  # Green (water)
            40: {"sprite_x": 11, "sprite_y": 5, "flag": False, "tree": False},  # Green (water)
            41: {"sprite_x": 13, "sprite_y": 10, "flag": False, "tree": True},  # Tree rough
            42: {"sprite_x": 10, "sprite_y": 10, "flag": False, "tree": True},  # Tree Fairway
            43: {"sprite_x": 1, "sprite_y": 11, "flag": False, "tree": True},  # Tree Deep Rough

        }


        self.sprite_sheet = pg.image.load('assets/new_sprite_sheet.png')

    def get_images_fonts(self):
        # Load Flag img
        flagImgs = []
        for i in range(0, 4):
            flagImg = pg.image.load(f'assets/Flag/Flag_{i}.png24')
            flagImgs.append(flagImg)

        self.img.append(flagImgs)

        # Load Box img
        boxImg = pg.image.load(f'assets/DistanceBox.png')
        boxImg.set_colorkey((0, 0, 0))
        boxImg = pg.transform.scale(boxImg, (100, 34))
        pg.Surface.convert_alpha(boxImg)
        self.img.append(boxImg)

        barImg = pg.image.load('assets/progressBar.png')
        barImg.set_colorkey((0, 0, 0))
        barImg = pg.transform.scale(barImg, (130, 10))
        pg.Surface.convert_alpha(barImg)
        self.img.append(barImg)

        windBoxImg = pg.image.load(f'assets/WindBox.png')
        windBoxImg.set_colorkey((0, 0, 0))
        windBoxImg = pg.transform.scale(windBoxImg, (38, 60))
        pg.Surface.convert_alpha(windBoxImg)
        self.img.append(windBoxImg)


        swingImgs = []
        for i in range(1, 6):
            if i != 3:
                swingImg = pg.image.load(f'assets/Swing/Swing0{i}.png')
                swingImgs.append(swingImg)
        self.img.append(swingImgs)


        ballImg = pg.image.load('assets/ball/Ball-Sprites_0000.png24')
        ballImg2 = pg.image.load('assets/ball/Ball-Sprites_0001.png24')
        # ballImg2.set_colorkey((0, 0, 0))
        # pg.Surface.convert_alpha(ballImg2)
        ball = [ballImg, ballImg2]
        self.img.append(ball)

        lieImgs = []
        for i in range(0, 3):
            lieImg = pg.image.load(f'assets/ball/Ball-Lay_000{i}.png')
            lieImg = pg.transform.scale(lieImg, (32, 32))
            lieImgs.append(lieImg)
        self.img.append(lieImgs)

        clubBox = pg.image.load('assets/ClubBox.png')
        clubBox.set_colorkey((0, 0, 0))
        pg.Surface.convert_alpha(clubBox)
        clubBox = pg.transform.scale(clubBox, (19*2, 19*2))
        self.img.append(clubBox)

        clubBox = pg.transform.scale(clubBox, (19*3, 19*2))
        self.img.append(clubBox)

        splash = []
        for i in range(0, 3):
            splashImg = pg.image.load(f'assets/Water/splash{i}.tiff')
            splashImg = pg.transform.scale(splashImg, (16, 16))
            splashImg.set_colorkey((255, 255, 255))
            pg.Surface.convert_alpha(splashImg)
            splash.append(splashImg)
        self.img.append(splash)

        treeImg = pg.image.load('assets/tree.png')
        treeImg = pg.transform.scale(treeImg, (16, 32))
        treeImg.set_colorkey((255, 255, 255))
        pg.Surface.convert_alpha(treeImg)
        self.img.append(treeImg)

        # Load your font with a specific size
        font_path = "assets/Fonts/letters.ttf"  # Path to your font file

        # Create font
        custom_font_hole = pg.font.Font(font_path, 21)
        self.font.append(custom_font_hole)

        custom_font_par = pg.font.Font(font_path, 25)
        self.font.append(custom_font_par)

        custom_font_wind = pg.font.Font(font_path, 40)
        self.font.append(custom_font_wind)

        custom_font_wind_text = pg.font.Font(font_path, 15)
        self.font.append(custom_font_wind_text)

        custom_font_water_text = pg.font.Font(font_path, 60)
        self.font.append(custom_font_water_text)

        # get sounds
        # golf shot sound
        # shots = []
        # for i in range(0, 3):
        #     golfShot = pg.mixer.Sound(f'assets/sound/effects/golfshot{i}.wav')  # Replace with your sound file
        #     shots.append(golfShot)
        golfShot = pg.mixer.Sound('assets/sound/effects/golfshot2.wav')  # Replace with your sound file

        self.sound.append(golfShot)

        splashSound = pg.mixer.Sound('assets/sound/effects/splash.mp3')
        self.sound.append(splashSound)

        OBSound = pg.mixer.Sound('assets/sound/effects/OB.wav')
        self.sound.append(OBSound)




    def get_map(self):
        y_start = (self.player[1] + 5) - 29
        y_start *= 16

        x_start = (self.player[0] * 16) - 320/2

        return [x_start, y_start]


    def change_map(self):
        # Check for keys held down
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.dy -= 1
        elif keys[pg.K_DOWN]:
            self.dy += 1
        else:
            self.dy = 0

        if self.dy < -5:
            self.dy = -5

        if self.dy > 5:
            self.dy = 5

        if (self.map_coordinates[1] + self.dy)/16 > 0 and self.dy < 0:
            self.map_coordinates[1] += self.dy

        if (self.map_coordinates[1] + self.dy) < (len(self.hole_layout)*16-480) and self.dy > 0:
            self.map_coordinates[1] += self.dy


        if keys[pg.K_LEFT]:
            self.dx -= 1
        elif keys[pg.K_RIGHT]:
            self.dx += 1
        else:
            self.dx = 0

        if self.dx < -5:
            self.dx = -5

        if self.dx > 5:
            self.dx = 5

        if (self.map_coordinates[0] + self.dx)/16 > 0 and self.dx < 0:
            self.map_coordinates[0] += self.dx

        if (self.map_coordinates[0] + self.dx) < (len(self.hole_layout[0])*16-320) and self.dx > 0:
            self.map_coordinates[0] += self.dx


    def get_hole_layout(self, course, hole):
        # Read the CSV file into a DataFrame
        df = pd.read_csv( f"Courses/{course}/Hole{hole}.csv", header=None)

        # Convert the DataFrame to integers (if there are NaN values, you might want to fill or drop them first)
        df = df.fillna(0)  # Replace NaN with 0 or you can choose to drop them using df.dropna()
        df = df.astype(int)  # Convert to integers

        # Convert the DataFrame to a 2D array (list of lists)
        hole_map = df.values.tolist()
        return hole_map

    def get_sprite(self, x, y):
        # Extract a specific sprite from the sprite sheet
        sprite = pg.Surface((16, 16))  # Create a surface for the sprite
        sprite.blit(self.sprite_sheet, (0, 0), (x * 16, y * 16, 16, 16))  # Blit the desired sprite
        return sprite

    def get_result(self):
        # Retrieve the current position value
        res_x = round(self.player[0] + self.shot_data[0]/16)
        res_y = round(self.player[1] + self.shot_data[1]/16)
        OB = False
        if res_y < 0 or res_y > len(self.hole_layout):
            OB = True
        if res_x < 0 or res_x > len(self.hole_layout[0]):
            OB = True

        if not OB:
            current_position_value = self.hole_layout[res_y][res_x]

            # Check the terrain type based on the current position value
            if current_position_value in (1, 9, 5, 6, 7, 8):
                result = "Rough"
            elif current_position_value in (2, 14, 11, 10, 13, 12, 37, 38, 39, 40):
                result = "Green"
            elif current_position_value in (3, 19, 15, 16, 18, 17):
                result = "Bunker"
            elif current_position_value in (4,):
                result = "Hole"
            elif current_position_value in (20, 0):
                result = "Fairway"
            elif current_position_value in (21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
                result = "Water"
            elif current_position_value in (31, 33, 34, 35, 36):
                result = "Deep Rough"
            else:
                result = "Tee Box"

            if result != "Water":
                self.player[2] = result # lie change

                # update play location
                self.player[0] += round(self.shot_data[0] / 16)
                self.player[1] += round(self.shot_data[1] / 16)

                # reset shot data
                self.shot_data = [0, 0, 0, 0]
                self.swing_num[0] = 0
                self.swing_num[1] = 0
                self.animation[0] = False
                self.currentShot += 1
                self.animate = False
            else:
                self.shot_data = [0, 0, 0, 0]
                self.swing_num[0] = 0
                self.swing_num[1] = 0
                self.animation[0] = False
                self.currentShot += 1
                self.animate = False
                self.currentShot += 1
                self.waterCounter[2] = True
                self.waterCounter[3] = res_x
                self.waterCounter[4] = res_y



        else:
            self.shot_data = [0, 0, 0, 0]
            self.swing_num[0] = 0
            self.swing_num[1] = 0
            self.animation[0] = False
            self.currentShot += 1
            self.animate = False
            self.currentShot += 1
            self.OB_counter[1] = True

    def animate_ball(self, screen):
        playerX = -self.map_coordinates[0] + self.player[0] * 16
        playerY = -self.map_coordinates[1] + self.player[1] * 16

        dx = self.shot_data[0] / 200
        dy = self.shot_data[1] / 200

        if self.shot_data[2] > 200:
            # Reset variables
            self.get_result()


        else:
            # Create a sine wave effect
            amplitude = 20  # Adjust amplitude as needed
            frequency = math.pi / 100  # Completes one cycle over 200 runs

            # Calculate sine wave y-offset
            y_offset = amplitude * math.sin(frequency * self.shot_data[2])

            # Draw the ball with the sine wave offset
            circle(screen, 'black',
                   ((playerX + 7 + 8) + dx * self.shot_data[3], (playerY + 3 + 8) + dy * self.shot_data[3] + y_offset),
                   2, 0)
            screen.blit(self.img[5][0],
                        ((playerX + 7) + dx * self.shot_data[2], (playerY + 3) + dy * self.shot_data[2] + y_offset))

            self.shot_data[2] += 1

            # Shadow movement adjustment
            if self.shot_data[2] <= 125:
                self.shot_data[3] += 0.75
            elif self.shot_data[2] <= 145:
                self.shot_data[3] += 1.1
            elif self.shot_data[2] <= 160:
                self.shot_data[3] += 1.3
            else:
                self.shot_data[3] += 1.55

            if self.shot_data[2] > 20:
                if (self.map_coordinates[1] + dy) / 16 > 0 and dy < 0:
                    self.map_coordinates[1] += dy * 0.85

                if (self.map_coordinates[1] + dy) < (len(self.hole_layout) * 16 - 480) and dy > 0:
                    self.map_coordinates[1] += dy * 0.85

                if (self.map_coordinates[0] + dx) / 16 > 0 and dx < 0:
                    self.map_coordinates[0] += dx * 0.85

                if (self.map_coordinates[0] + dx) < (len(self.hole_layout[0]) * 16 - 320) and dx > 0:
                    self.map_coordinates[0] += dx * 0.85

    def draw_player(self, screen):
        playerX = -self.map_coordinates[0] + self.player[0] * 16
        playerY = -self.map_coordinates[1] + self.player[1] * 16



        angle = self.get_angle(playerX, playerY)

        # print(angle * 180/math.pi)
        # circle(screen, (255, 0, 0), (playerX+7, playerY + 10), 5, 0)

        if self.player[2] == "Green":
            circle(screen, 'black',
                   (playerX + 7 + (math.cos(angle) * 45) * 3, playerY + 10 + (math.sin(angle) * 45) * 3), 4, 2)
            circle(screen, 'white',
                   (playerX + 7 + (math.cos(angle) * 45) * 3, playerY + 10 + (math.sin(angle) * 45) * 3), 2, 0)

            circle(screen, 'black', (playerX + 7 + (math.cos(angle) * 45)*2, playerY + 10 + (math.sin(angle) * 45)*2), 4, 2)
            circle(screen, 'white', (playerX + 7 + (math.cos(angle) * 45)*2, playerY + 10 + (math.sin(angle) * 45)*2), 2, 0)

            circle(screen, 'black',
                   (playerX + 7 + (math.cos(angle) * 45), playerY + 10 + (math.sin(angle) * 45)), 4, 2)
            circle(screen, 'white',
                   (playerX + 7 + (math.cos(angle) * 45), playerY + 10 + (math.sin(angle) * 45)), 2, 0)

            screen.blit(self.img[4][0], (playerX, playerY))
            screen.blit(self.img[5][0], (playerX + 7, playerY + 3))  # draw ball

        else:
            if not self.animate:

                circle(screen, (255, 255, 255), (playerX + 7 + (math.cos(angle) * 45), playerY + 20 + (math.sin(angle) * 45)), 4, 0)
                circle(screen, (0, 0, 0), (playerX + 7 + (math.cos(angle) * 45), playerY + 20 + (math.sin(angle) * 45)), 5,2)

                screen.blit(self.img[4][0], (playerX, playerY))
                screen.blit(self.img[5][0], (playerX + 7, playerY + 3)) # draw ball
            else:
                if not self.animation[0] and not self.animation[1]:
                    screen.blit(self.img[4][self.swing_num[1]], (playerX, playerY))
                    screen.blit(self.img[5][0], (playerX + 7, playerY + 3))  # draw ball

                    if self.swing_num[0] < 10:
                        self.swing_num[0] += 1
                    else:
                        self.swing_num[0] = 0
                        self.swing_num[1] += 1

                    if self.swing_num[1] == 2:
                        self.animation[0] = True
                        # rand_index = random.randint(0, 2)
                        self.sound[0].play()

                    if self.swing_num[1] > 3:
                        self.swing_num[1] = 3

                elif self.animation[0] and not self.animation[1]:
                    screen.blit(self.img[4][self.swing_num[1]], (playerX, playerY))

                    if self.swing_num[0] < 10:
                        self.swing_num[0] += 1
                    else:
                        self.swing_num[0] = 0
                        self.swing_num[1] += 1

                    if self.swing_num[1] > 3:
                        self.swing_num[1] = 3

                    self.animate_ball(screen)

    def calculate_distance(self):
        distX = abs(self.player[0] - self.flag[0]) * 8
        distY = abs(self.player[1] - self.flag[1]) * 8
        dist = math.sqrt(math.pow(distX, 2) + math.pow(distY, 2))

        if self.hole_layout[self.player[1]][self.player[0]] in (2, 4, 14, 10, 11, 12, 13):
            return -1
        else:
            return round(dist)


    def draw(self, screen):
        # Loop through the hole layout and draw the corresponding sprites
        for i in range(len(self.hole_layout)):
            for j in range(len(self.hole_layout[i])):

                # In your draw method, retrieve the configuration for each tile
                config = self.tile_configs.get(self.hole_layout[i][j], {"sprite_x": 10, "sprite_y": 10, "flag": False, "tree": False,})  # Default to Fairway (0)

                sprite_x = config["sprite_x"]
                sprite_y = config["sprite_y"]
                flag = config["flag"]
                tree = config["tree"]

                sprite = self.get_sprite(sprite_x, sprite_y)

                # Calculate the position on the screen to draw the sprite
                x = -self.map_coordinates[0] + j * 16  # Adjust this for your game map scaling
                y = -self.map_coordinates[1] + i * 16  # Adjust this for your game map scaling
                screen.blit(sprite, (x, y))  # Draw the sprite on the screen

                if flag:
                    screen.blit(self.img[0][self.flag_num[1]], (x + 8, y - 7))

                    # Add to counter
                    self.flag_num[0] += 1

                    # If statements to change animation
                    if self.flag_num[0] > 50/self.wind:
                        self.flag_num[1] += 1
                        self.flag_num[0] = 0

                    if self.flag_num[1] > 3:
                        self.flag_num[1] = 0
                if tree:
                    screen.blit(self.img[10], (x, y-16))  # Draw the sprite on the screen



        # Draw Player
        self.draw_player(screen)


        # Draw HUD:
        screen.blit(self.img[1], (5, 5))
        shot_text = self.font[0].render(f"Shot {self.currentShot+1}", False, (255, 255, 255))
        screen.blit(shot_text, (14, 13))


        screen.blit(self.img[1], (218, 5))
        screen.blit(self.img[1], (218, 42))
        screen.blit(self.img[1], (218, 78))

        # Create label with font
        hole_text = self.font[0].render(f"Hole {self.hole}", False, (255, 255, 255))
        par_text = self.font[1].render(f"Par {self.par}", False, (255, 255, 255))

        if self.calculate_distance() == -1:
            dist_text = self.font[1].render("Green", False, (255, 255, 255))
        else:
            dist_text = self.font[1].render(f"{self.calculate_distance()} Y", False, (255, 255, 255))

        # Display font
        if int(self.hole) > 9:
            screen.blit(hole_text, (226, 13))
        else:
            screen.blit(hole_text, (230, 13))

        screen.blit(par_text, (230, 48))

        if self.calculate_distance() > 99:
            screen.blit(dist_text, (227, 84))
        elif self.calculate_distance() > 9:
            screen.blit(dist_text, (227, 84))
        else:
            screen.blit(dist_text, (227, 84))


        # Power
        screen.blit(self.img[2], (15, 440))
        pg.draw.rect(screen, (0, 255, 0), (22, 442, self.powerBarSize[0][0], 5))

        # Accuracy
        screen.blit(self.img[2], (15, 460))
        pg.draw.rect(screen, (0, 255, 0), (22, 462, self.powerBarSize[1][0], 5))

        # Wind Img
        wind_text = self.font[2].render(self.arrow[self.direction], False, (255, 255, 255))
        wind_text_number = self.font[3].render(f'{self.wind}', False, (255, 255, 255))

        screen.blit(self.img[3], (270, 415))
        screen.blit(wind_text, (277, 415))

        if self.wind > 9:
            screen.blit(wind_text_number, (280, 455))
        else:
            screen.blit(wind_text_number, (285, 455))

        # draw lie
        imgIndex = 2
        if self.player[2] == "Fairway":
            imgIndex = 2
        elif self.player[2] == "Rough" or self.player[2] == "Deep Rough":
            imgIndex = 1
        elif self.player[2] == "Bunker":
            imgIndex = 0

        screen.blit(self.img[6][imgIndex], (273, 380))

        # Draw Club
        screen.blit(self.img[7], (160, 437))
        screen.blit(self.img[8], (205, 437))

        if self.player[2] == "Green":
            club_text = self.font[0].render("PT", False, (255, 255, 255))
            dist_text = self.font[0].render("N/A", False, (255, 255, 255))
        else:
            club_text = self.font[0].render(f"{self.club_Str[self.clubSelection]}", False, (255, 255, 255))

            config = self.clubs.get(self.club_Str[self.clubSelection])
            distance = config["distance"]

            dist_text = self.font[0].render(f"{distance}", False, (255, 255, 255))

        screen.blit(club_text, (167, 445))
        screen.blit(dist_text, (215, 445))

        # test to see shot line
        # if self.test[0]:
        #     playerX = -self.map_coordinates[0] + self.player[0] * 16 + 7
        #     playerY = -self.map_coordinates[1] + self.player[1] * 16 + 10
        #     line(screen, (255, 0, 0), (playerX, playerY), (playerX + self.test[1], playerY +self.test[2]), 5)

        # draw Water notification
        if self.waterCounter[2]:
            water_text = self.font[4].render("Water", False, (255, 255, 255))
            stroke_text = self.font[4].render("+1 Stroke", False, (255, 255, 255))
            screen.blit(water_text, (82, 120))
            screen.blit(stroke_text, (3, 220))


            if self.waterCounter[0] == 0 and self.waterCounter[1] == 0:
                self.sound[1].play()

            if self.waterCounter[3] != -1:
                screen.blit(self.img[9][self.waterCounter[1]], (8 -self.map_coordinates[0] + self.waterCounter[3] * 16, 8 -self.map_coordinates[1] + self.waterCounter[4] *16))

            self.waterCounter[0] += 1

            if self.waterCounter[0] > 5:
                self.waterCounter[1] += 1
                if self.waterCounter[1] <= 2:
                    self.waterCounter[0] = 0

            if self.waterCounter[1] > 2:
                self.waterCounter[3] = -1

            if self.waterCounter[0] > 120:
                self.waterCounter = [0, 0, False, 0, 0]
                self.map_coordinates = [self.old_map_coordinates[0], self.old_map_coordinates[1]]

        # draw OB notification
        if self.OB_counter[1]:
            OB_text = self.font[4].render("OB", False, (255, 255, 255))
            stroke_text = self.font[4].render("+1 Stroke", False, (255, 255, 255))
            screen.blit(OB_text, (82, 120))
            screen.blit(stroke_text, (3, 220))

            if self.OB_counter[0] == 0:
                self.sound[2].play()

            self.OB_counter[0] += 1

            if self.OB_counter[0] > 125:
                self.OB_counter = [0, False]

                self.map_coordinates = [self.old_map_coordinates[0], self.old_map_coordinates[1]]




    def get_angle(self, playerX, playerY):
        aimX = playerX + 7 + self.aim[0]
        aimY = playerY - 40

        if self.aim[2] == -1:
            angle = math.atan2(aimX - (playerX + 7), aimY - (playerY + 10))
        elif self.aim[2] == 1:
            angle = math.atan2(aimX - (playerX + 7), (aimY - (playerY + 10)) * -1)
        else:
            angle = math.atan2(aimY - (playerY + 10), aimX - (playerX + 7))

        return angle

    def calculate_shot(self):
        if self.player[2] == "Green":
            power = round((self.powerBarSize[0][0] / 116) * 100)
            precision = round((self.powerBarSize[1][0] / 116) * 100)

            if power > 100:
                power = 100
            elif power <= 0:
                power = 10

            if precision > 100:
                precision = 100
            elif precision < 0:
                precision = 0

            # max_dist =

        else:
            config = self.clubs.get(self.club_Str[self.clubSelection])  # Default to Driver

            distance = config["distance"]
            accuracy = config["accuracy"]
            height = config["angle"]

            power = round((self.powerBarSize[0][0]/116) * 100)
            precision = round((self.powerBarSize[1][0]/116) * 100)

            if power > 100:
                power = 100
            elif power <= 0:
                power = 10

            if precision > 100:
                precision = 100
            elif precision < 0:
                precision = 0

            if self.player[2] == "Fairway":
                lie = 0
            elif self.player[2] == "Rough":
                lie = 15
            elif self.player[2] == "Bunker":
                lie = 25
            elif self.player[2] == "Deep Rough":
                lie = 35
            else:
                lie = 0

            max_dist = (distance * (power/100)) * ((100 - lie) / 100)

            deviation_range = (accuracy - (accuracy * (precision / 100)))  # Adjust this factor for realism


            # Randomly determine left or right deviation within the range
            miss = random.randint(0, 1)
            if miss == 0:
                horizontal_deviation = deviation_range
            else:
                horizontal_deviation = -deviation_range

            # cos(0) = A/H -> A = Hcos(0)


            playerX = -self.map_coordinates[0] + self.player[0] * 16
            playerY = -self.map_coordinates[1] + self.player[1] * 16


            angle = self.get_angle(playerX, playerY)


            # max_dist = round(max_dist/16)
            # self.arrow = ["↑", "→", "↓", "←"]

            wind_x = 0
            wind_y = 0

            if self.direction == 0:
                wind_y = -self.wind * 8
            elif self.direction == 1:
                wind_x = self.wind * 8
            elif self.direction == 2:
                wind_y = self.wind * 8
            else:
                wind_x = -self.wind * 8

            dist_x = ((round(max_dist * math.cos(angle) + horizontal_deviation)) * 2) + wind_x
            dist_y = round(max_dist * math.sin(angle)) * 2 + wind_y

            # x yards * 1 box/8yards *16 px/1 box

            self.test[0] = True
            self.test[1] = dist_x
            self.test[2] = dist_y
            self.shot_data[0] = dist_x
            self.shot_data[1] = dist_y
            print(self.map_coordinates)
            self.old_map_coordinates = [self.map_coordinates[0], self.map_coordinates[1]]
            print(self.old_map_coordinates)

            print("Power: ", power)
            print("Precision: ", precision)
            print("Lie: ", lie)
            print("Max_Dist: ", max_dist)
            print("Dist_X: ", dist_x)
            print("Dist_Y: ", dist_y)
            print("Wind_X", wind_x)
            print("Wind_Y", wind_y)
            print("Deviation: ", horizontal_deviation)



    def run(self):
        if not self.waterCounter[2] and not self.OB_counter[1] and self.shot_data[0] == 0 and self.shot_data[1] == 0:
            self.change_map()
            keys = pg.key.get_pressed()




            if keys[pg.K_a]:
                if self.aim[2] == 0 or self.aim[2] == 1:
                    self.aim[0] -= 3
                else:
                    self.aim[0] += 3
            if keys[pg.K_s]:
                if self.aim[2] == 0 or self.aim[2] == 1:
                    self.aim[0] += 3
                else:
                    self.aim[0] -= 3

            if self.aim[0] < -225 and self.aim[2] == 0:
                self.aim[0] = 0
                self.aim[2] = -1

            if self.aim[0] < -255 and self.aim[2] == -1:
                self.aim[0] = 0
                self.aim[2] = 0

            if self.aim[0] > 255 and self.aim[2] == 0:
                self.aim[0] = 0
                self.aim[2] = 1

            if self.aim[0] < -255 and self.aim[2] == 1:
                self.aim[0] = 0
                self.aim[2] = 0



            if keys[pg.K_z]:
                if not self.justClicked[1]:
                    self.justClicked[1] = True
                    if self.clubSelection < 12:
                        self.clubSelection += 1
                    else:
                        self.clubSelection = 0
            else:
                self.justClicked[1] = False

            if self.player[2] == "Green":
                speed = 1
            else:
                speed = 5

            if keys[pg.K_x]:
                if not self.justClicked[0]:
                    self.justClicked[0] = True
                    if not self.getShotData[2]:
                        if not self.getShotData[0] and not self.getShotData[1]:
                            self.getShotData[0] = True
                        elif self.getShotData[0] and not self.getShotData[1]:
                            self.getShotData[0] = False
                            self.powerBarSize[0][1] = False
                            self.getShotData[1] = True
                        elif self.getShotData[1]:
                            self.getShotData[1] = False
                            self.getShotData[2] = True
                            self.powerBarSize[1][1] = False
            else:
                self.justClicked[0] = False

            if not self.getShotData[2]:
                if self.getShotData[0]:
                    if not self.powerBarSize[0][1]:
                        self.powerBarSize[0][0] += speed
                    else:
                        self.powerBarSize[0][0] -= speed

                    # add logic so that power bar will go down if missed but stop at zero on way back 0-116
                    if not self.powerBarSize[0][1] and self.powerBarSize[0][0] > 115:
                        self.powerBarSize[0][1] = True
                    elif self.powerBarSize[0][1] and self.powerBarSize[0][0] < 0:
                        self.powerBarSize[0][0] = 0
                        self.getShotData[0] = False
                        self.powerBarSize[0][1] = False
                        self.getShotData[1] = True

                elif self.getShotData[1]:
                    if not self.powerBarSize[1][1]:
                        self.powerBarSize[1][0] += speed
                    else:
                        self.powerBarSize[1][0] -= speed

                    # add logic so that power bar will go down if missed but stop at zero on way back 0-116
                    if not self.powerBarSize[1][1] and self.powerBarSize[1][0] > 115:
                        self.powerBarSize[1][1] = True
                    elif self.powerBarSize[1][1] and self.powerBarSize[1][0] < 0:
                        self.powerBarSize[1][0] = 0
                        self.getShotData[1] = False
                        self.powerBarSize[1][1] = False
                        self.getShotData[2] = True


            elif self.getShotData[2]:
                self.calculate_shot()
                self.animate = True
                self.getShotData = [False, False, False]
                self.powerBarSize = [[0, False], [0, False]]





