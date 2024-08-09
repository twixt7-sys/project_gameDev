import pygame as pg
import python.matrices.mat as mat
pg.init()

win_size = 900, 900
win = pg.display.set_mode(win_size)
pg.display.set_caption("Matrix Processor")

matrix_box = (200, 200, 500, 500)
mat = mat.Matrices().matrix(0)

def paint_matrix(rect, matrix):
    partition_count = 5
    partitions =   ((rect[0] + (rect[2] / 5 * 0), rect[0] + (rect[2] / 5 * 1), rect[0] + (rect[2] / 5 * 2), rect[0] + (rect[2] / 5 * 3), rect[0] + (rect[2] / 5 * 4)),
                    (rect[1] + (rect[3] / 5 * 0), rect[1] + (rect[3] / 5 * 1), rect[1] + (rect[3] / 5 * 2), rect[1] + (rect[3] / 5 * 3), rect[1] + (rect[2] / 5 * 4)))
    X = (partitions[0][0], partitions[0][1], partitions[0][2], partitions[0][3], partitions[0][4])
    Y = (partitions[1][0], partitions[1][1], partitions[1][2], partitions[1][3], partitions[1][4])
    for x in range(partition_count - 1):
        for y in range(partition_count - 1):
            if matrix[x][y] == 1:
                pg.draw.rect(win, (255, 255, 255), (X[x], Y[y], matrix[2] / partition_count, matrix[3] / partition_count))
            else:
                pg.draw.rect(win, (0, 0, 0), (X[x], Y[y], matrix[2] / partition_count, matrix[3] / partition_count))

run = True
while run:
    pg.time.Clock.tick(30)
    for events in pg.event.get():
        if events.type == pg.QUIT:
            run = False
    paint_matrix(matrix_box, mat)
    pg.display.update()
pg.quit()