import Tools.Dictionary as dic
class MatrixField(object):
    def __init__(self, game):
        self.game = game
        # initialize attributes
        self.anchor_point = [0, 0]
        self.size = 0
        self.text_count = 0
        self.field_length = 0
        self.color1 = (255, 255, 255)
        self.color2 = (0, 0, 0, 0)
        self.text = None

    def draw_matrix_field(self, text, anchor_point, size=10, color1=(255, 255, 255), color2=(0, 0, 0, 0)):
        self.text, self.anchor_point, self.size, self.color1, self.color2 = text, anchor_point, size, color1, color2
        self.text_count = len(text)
        self.field_length = self.text_count * self.size
        self.field_pos = self.anchor_point[0] - self.field_length / 2
        text_pos = []
        x = range(len(text))
        y = self.anchor_point[1] - self.size / 2
        for pos in range(len(text)):
            text_pos.append([x[pos], y])
        for i, char in enumerate(text):
            MatrixField.draw_matrix(self, char, text_pos[i])

    def draw_matrix(self, char, pos):
        value = dic.Dictionary().matrices()[char.upper()]                            #2d array
        partition_count = len(value)
        partition_width, partition_height = self.size / partition_count, self.size / partition_count

        offset_x, offset_y = (self.size - partition_width * partition_count) / 2, (self.size - partition_height * partition_count) / 2

        for hori in range(partition_count):
            for vert in range(partition_count):
                color = self.color1 if value[vert][hori] == 1 else self.color2
                rect_x = pos[0] - self.size / 2 + hori * partition_width + offset_x
                rect_y = pos[1] - self.size / 2 + vert * partition_height + offset_y
                self.game.pyg.draw.rect(self.game.win, color, (rect_x, rect_y, partition_width, partition_height))
