import pygame as pg
pg.init()

def paint_matrix(rect, matrix, win, color1, color2):
    partition_count = len(matrix)
    partition_width = rect[2] / partition_count
    partition_height = rect[3] / partition_count
    for x in range(partition_count):
        for y in range(partition_count):
            color = color1 if matrix[y][x] == 1 else color2
            pg.draw.rect(win, color, (rect[0] + x * partition_width, rect[1] + y * partition_height, partition_width, partition_height))

class Matrix(object):
    def num(self, n):
        self.matrix = (
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0),
            (0,0,0,0,0)
        )
        if n == 0:
            self.matrix =  (
                (0,1,1,1,0),
                (0,1,0,1,0),
                (0,1,0,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0)
            )
        elif n == 1:
            self.matrix =  (
                (0,1,1,0,0),
                (0,0,1,0,0),
                (0,0,1,0,0),
                (0,0,1,0,0),
                (0,1,1,1,0)
            )
        elif n == 2:
            self.matrix =  (
                (0,1,1,0,0),
                (0,0,0,1,0),
                (0,1,1,1,0),
                (0,1,0,0,0),
                (0,1,1,1,0)
            )
        elif n == 3:
            self.matrix =  (
                (0,1,1,0,0),
                (0,0,0,1,0),
                (0,1,1,0,0),
                (0,0,0,1,0),
                (0,1,1,0,0)
            )
        elif n == 4:
            self.matrix =  (
                (0,1,0,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0),
                (0,0,0,1,0),
                (0,0,0,1,0)
            )
        elif n == 5:
            self.matrix =  (
                (0,1,1,1,0),
                (0,1,0,0,0),
                (0,1,1,1,0),
                (0,0,0,1,0),
                (0,1,1,1,0)
            )
        elif n == 6:
            self.matrix =  (
                (0,1,1,1,0),
                (0,1,0,0,0),
                (0,1,1,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0)
            )
        elif n == 7:
            self.matrix =  (
                (0,1,1,1,0),
                (0,0,0,1,0),
                (0,0,0,1,0),
                (0,0,0,1,0),
                (0,0,0,1,0)
            )
        elif n == 8:
            self.matrix =  (
                (0,1,1,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0)
            )
        elif n == 9:
            self.matrix =  (
                (0,1,1,1,0),
                (0,1,0,1,0),
                (0,1,1,1,0),
                (0,0,0,1,0),
                (0,1,1,1,0)
            )
        return self.matrix

