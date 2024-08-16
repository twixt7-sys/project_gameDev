#Class for drawing 5x5 pixel squares
class Matrix(object):
    def __init__(self, game, pyg, dic, color1, color2):
        self.game = game
        self.pyg = pyg
        self.win = self.game.win
        self.d = dic
        self.color1 = color1
        self.color2 = color2

    def paint_matrix_field(self, center, size, length, text, reversed=False):
        #Creating Instance Variable for Ease
        mat = Matrix(self.game, self.pyg, self.d, self.color1, self.color2)
        start_index, end_index = 0, (-length if reversed else length)
        if length >= len(text):
            for i in range(length):                                             #To modify(make compatible with reversed)
                if i <= length - len(text):
                    mat.paint_matrix(None, (i * center[0], center[1]), size)
                else:
                    mat.paint_matrix(text[i], (center[0], center[1]), size)
        else:                                                                   #partial
            length = len(text) - length
            for i in range(length):
                mat.paint_matrix(text[i], (center[0], center[1]), size)

    def paint_matrix(self, val, center, size):
        self.matrix = self.d.Dictionary().matrices()[val]
        partition_count = len(self.matrix)
        partition_width, partition_height = size / partition_count, size / partition_count

        offset_x, offset_y = (size - partition_width * partition_count) / 2, (size - partition_height * partition_count) / 2

        for hori in range(partition_count):
            for vert in range(partition_count):
                color = self.color1 if self.matrix[vert][hori] == 1 else self.color2
                rect_x = center[0] - size / 2 + hori * partition_width + offset_x
                rect_y = center[1] - size / 2 + vert * partition_height + offset_y
                self.pyg.draw.rect(self.win, color, (rect_x, rect_y, partition_width, partition_height))
