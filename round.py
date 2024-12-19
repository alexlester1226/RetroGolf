

class Round:
    def __init__(self, course, par):
        self.course = course
        self.score = [par, 0, 0]
        self.hole = None

    def play(self):
        x=0 # logic for playing

