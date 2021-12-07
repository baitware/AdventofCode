import numpy as np

with open('inputday4_board.txt') as f:
    input = f.readlines()

with open('inputday4_draw.txt') as h:
    draw_input = h.read()

input = list([s.replace('\n', '') for s in input])

def split(word):
    return word.split()

draw_list = draw_input.split(',')
draw = np.array(draw_list)

i = 0
board_list = []
while i < len(input):
    board_list.append(split(input[i]))
    i += 1

board_list = list(filter(lambda x: x, board_list))

boards = np.array(board_list)
boards = np.array_split(boards, 100)

board_rowcount = np.zeros([100,5])
board_ccount = np.zeros([100,5])

end_loop = False

board_nr = []

i = 0
while end_loop == False:
    h = 0
    while h < len(boards):
        j = 0
        while j < len(boards[0]):
            k = 0
            while k < len(boards[0]):

                if boards[h][j][k] == draw[i]:
                    boards[h][j][k] = 'x'
                    board_rowcount[h][j] += 1
                    board_ccount[h][k] += 1 

                    if board_rowcount[h][j] == 5:
                        if h in board_nr:
                            break
                        else:
                            board_nr.append(h)

                    elif board_ccount[h][k] == 5:
                        if h in board_nr:
                            break
                        else:
                            board_nr.append(h)

                    if len(board_nr) == 100:
                        end_draw = draw[i]
                        end_loop = True                
                k += 1
            j += 1
        h += 1
    i += 1

score = boards[board_nr[-1]].flatten()
score = np.delete(score, np.where(score == 'x'))
score = np.sum(np.int64(score))


print(score, int(end_draw), score * int(end_draw))