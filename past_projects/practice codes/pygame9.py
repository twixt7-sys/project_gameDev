import pygame as pg
import mat

pg.init()

win_size = 900, 900
win = pg.display.set_mode(win_size)
pg.display.set_caption("Matrix Processor")

matrix_box = (200, 200, 500, 500)
Mat = mat.Matrix().num(3)

def paint_matrix(rect, matrix):
    partition_count = len(matrix)
    partition_width = rect[2] / partition_count
    partition_height = rect[3] / partition_count
    for x in range(partition_count):
        for y in range(partition_count):
            color = (255, 255, 255) if matrix[y][x] == 1 else (0, 0, 0)
            pg.draw.rect(win, color, (rect[0] + x * partition_width, rect[1] + y * partition_height, partition_width, partition_height))

run = True
clock = pg.time.Clock()
i = 0
while run:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    win.fill((0, 0, 0))
    Mat = mat.Matrix().num(i)
    i += 1 if i != 10 else (- 9)
    paint_matrix(matrix_box, Mat)
    pg.display.update()

pg.quit()
