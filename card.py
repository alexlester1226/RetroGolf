import pygame as pg
import math

class Card:
    def __init__(self, title, par, num_holes, difficulty, prize, lock):
        self.title = title
        self.par = par
        self.num_holes = num_holes
        self.difficulty = difficulty
        self.prize = prize  # An array {1st, 2nd, 3rd}
        self.lock = lock
        self.img = []
        self.font = []
        self.show_star = [0, 0, 0, 0, 0]

        self.load_images()
        self.get_show_star()


    def load_images(self):
        headerImg = pg.image.load("assets/GUI/bar.png")
        headerImg = pg.transform.scale(headerImg, (232, 48))
        self.img.append(headerImg)

        bodyImg = pg.image.load("assets/GUI/Window_Body.png")
        bodyImg = pg.transform.scale(bodyImg, (252, 396))
        self.img.append(bodyImg)

        outlineImg = []

        outline_top = pg.image.load("assets/GUI/Window_Outline_Top.png")
        outline_top = pg.transform.scale(outline_top, (36, 6))
        outline_right = pg.image.load("assets/GUI/Window_Outline_Right.png")
        outline_right = pg.transform.scale(outline_right, (6, 36))
        outline_bottom = pg.image.load("assets/GUI/Window_Outline_Bottom.png")
        outline_bottom = pg.transform.scale(outline_bottom, (36, 6))
        outline_left = pg.image.load("assets/GUI/Window_Outline_Left.png")
        outline_left = pg.transform.scale(outline_left, (6, 36))

        outline_top_left = pg.image.load("assets/GUI/Window_Outline_Top_Left.png")
        outline_top_left = pg.transform.scale(outline_top_left, (6, 6))

        outline_top_right = pg.image.load("assets/GUI/Window_Outline_Top_Right.png")
        outline_top_right = pg.transform.scale(outline_top_right, (6, 6))

        outline_bottom_left = pg.image.load("assets/GUI/Window_Outline_Bottom_Left.png")
        outline_bottom_left = pg.transform.scale(outline_bottom_left, (6, 6))

        outline_bottom_right = pg.image.load("assets/GUI/Window_Outline_Bottom_Right.png")
        outline_bottom_right = pg.transform.scale(outline_bottom_right, (6, 6))

        outlineImg.append(outline_top)
        outlineImg.append(outline_right)
        outlineImg.append(outline_bottom)
        outlineImg.append(outline_left)

        outlineImg.append(outline_top_left)
        outlineImg.append(outline_top_right)
        outlineImg.append(outline_bottom_left)
        outlineImg.append(outline_bottom_right)

        self.img.append(outlineImg)

        course_img = pg.image.load(f"assets/Course-Img/{self.title}.webp")
        course_img = pg.transform.scale(course_img, (206, 206))
        self.img.append(course_img)

        bodyImg = pg.transform.scale(bodyImg, (210, 210))
        self.img.append(bodyImg)


        lockImg = pg.image.load(f"assets/lock.png")
        lockImg = lockImg.convert_alpha()
        lockImg = pg.transform.scale(lockImg, (20, 20))
        self.img.append(lockImg)

        stars = []
        for i in range(0, 3):
            star = pg.image.load(f"assets/Stars/star_{i}.png")
            star = pg.transform.scale(star, (16, 16))
            stars.append(star)
        self.img.append(stars)

        # Fonts
        font_path = "assets/Fonts/letters.ttf"
        title_font = pg.font.Font(font_path, 15)
        self.font.append(title_font)

        item_font = pg.font.Font(font_path, 20)
        self.font.append(item_font)

    def get_show_star(self):
        for i in range(0, math.floor(self.difficulty)):
            self.show_star[i] = 1

        halfStar = self.difficulty - math.floor(self.difficulty)
        if halfStar > 0:
            self.show_star[math.floor(self.difficulty)] = 0.5



    def draw_card(self, screen, x, y):
        for i in range(0, 7):
            screen.blit(self.img[2][0], (x + 36 * i, y - 6))
            screen.blit(self.img[2][2], (x + 36 * i, y + 396))

        for k in range(0, 11):
            screen.blit(self.img[2][3], (x - 6, y + 36 * k))
            screen.blit(self.img[2][1], (x + 252, y + 36 * k))

        screen.blit(self.img[2][4], (x - 6, y - 6))
        screen.blit(self.img[2][5], (x + 252, y - 6))
        screen.blit(self.img[2][6], (x - 6, y + 396))
        screen.blit(self.img[2][7], (x + 252, y + 396))

        screen.blit(self.img[1], (x, y))
        # pg.draw.rect(screen, (0, 0, 0), (x + 5, y + 5, 242, 48))

        screen.blit(self.img[0], (x + 10, y + 15))
        title = self.font[1].render(f"{self.title}", False, (0, 0, 0))
        screen.blit(title, (x + 22, y + 28))

        # screen.blit(self.img[4], (x + 20, y + 85))
        screen.blit(self.img[3], (x + 17 + 5, y + 75 + 5))

        for i in range(0, 6):
            screen.blit(self.img[2][0], (x + 17 + 36 * i, y + 75 - 6))
            screen.blit(self.img[2][2], (x + 17 + 36 * i, y + 75 + 216))

            screen.blit(self.img[2][3], (x + 17 - 6, y + 75 + 36 * i))
            screen.blit(self.img[2][1], (x + 17 + 216, y + 75 + 36 * i))

        screen.blit(self.img[2][4], (x + 17 - 6, y + 75 - 6))
        screen.blit(self.img[2][5], (x + 17 + 216, y + 75 - 6))
        screen.blit(self.img[2][6], (x + 17 - 6, y + 75 + 216))
        screen.blit(self.img[2][7], (x + 17 + 216, y + 75 + 216))

        # par_label = self.font[0].render(f" Par: {self.par} {self.num_holes} Holes  Winnings:", False, 'black')
        par_label = self.font[0].render(f" Par: {self.par}       Winnings:", False, 'black')
        if self.num_holes < 10:
            prize_label1 = self.font[0].render(f" {self.num_holes} Holes       1st: {self.prize[0]}", False, 'black')

        else:
            prize_label1 = self.font[0].render(f" {self.num_holes} Holes      1st: {self.prize[0]}", False, 'black')
        prize_label2 = self.font[0].render(f" Difficulty:   2nd: {self.prize[1]}", False, 'black')
        prize_label3 = self.font[0].render(f"               3rd: {self.prize[2]}", False, 'black')


        screen.blit(par_label, (x + 5, y + 310))
        screen.blit(prize_label1, (x + 5, y + 330))
        screen.blit(prize_label2, (x + 5, y + 350))
        screen.blit(prize_label3, (x + 5, y + 370))

        # screen.blit(self.img[6][0], (x + 5, y + 368))

        star_x = x + 12
        for i in range(0, 5):
            if self.show_star[i] == 1:
                screen.blit(self.img[6][0], (star_x, y + 368))
            elif self.show_star[i] == 0.5:
                screen.blit(self.img[6][2], (star_x, y + 368))
            else:
                screen.blit(self.img[6][1], (star_x, y + 368))

            star_x += 20



        if self.lock:
            screen.blit(self.img[5], (x + 226, y + 365))


        # screen.blit(self.img[0], (x + 10, y + 330))







