#Class for drawing 5x5 pixel squares
class Matrix(object):
    def __init__(self, game, pyg, dic, color1, color2):
        self.game = game
        self.pyg = pyg
        self.win = self.game.win
        self.d = dic
        self.color1 = color1
        self.color2 = color2

    def paint_matrix_field(self, center, size, length, text):
        mat = Matrix(self.game, self.pyg, self.d, self.color1, self.color2)
        field_width = size * length
        if len(text) > length:
            text = text[-length:]
        total_text_width = size * len(text)
        start_x = center[0] - (total_text_width / 2)
        for i, char in enumerate(text):
                pos_x = start_x + i * size
                mat.paint_matrix(char, (pos_x, center[1]), size)
        if len(text) < length:
                # Number of blanks to add
                num_blanks = length - len(text)
                blank_width = num_blanks * size
                blank_start_x = start_x + len(text) * size
                for i in range(num_blanks):
                    pos_x = blank_start_x + i * size
                    mat.paint_matrix(None, (pos_x, center[1]), size)

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
