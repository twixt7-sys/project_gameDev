#Redo the damn thing (use a box for debugging) (no centeringf)
import Tools.Dictionary as dic

class Matrix(object):
    def __init__(self, game):
        self.game = game
        self.resolution = 5
    def draw_matrix_field(self, text, loc, size=10, color1=[255, 255, 255], color2=[0, 0, 0, 0]):
        self.text, self.loc, self.size, self.color1, self.color2 = text, loc, size, color1, color2
        self.field_length = self.size * self.resolution * len(self.text)
        pos = []
        for i in range(len(self.text)):
            pos.append((self.loc[0] + i * self.size * self.resolution, self.loc[1]))
        for i, char in enumerate(text):
            print(self.loc)
            Matrix.draw_matrix(self, char, pos[i])
    def draw_matrix(self, matrix, pos):
        matrix_val = dic.Dictionary().matrices()[matrix.upper()]
        color, size = None, self.size
        for i in range(self.resolution):
            for j in range(self.resolution):
                color = self.color1 if matrix_val[i][j] == 1 else (self.color2)
                self.game.pyg.draw.rect(self.game.win, color, (pos[0] + j * size,pos[1] + i * size, size, size))