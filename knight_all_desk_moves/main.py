chess_board = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
knight_possible_moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
result_list = []
counter = 100

def letters_to_cords(word):
    return letters.index(word[0]), 8 - int(word[1])


def cords_to_letters(cords):
    return str(letters[cords[0]] + str(8 - cords[1]))


knight_cords = letters_to_cords(input().lower())
knight_moves = [knight_cords]


for b in range(8):
    chess_board.append([])
    for j in range(8):
        chess_board[b].append(False)


chess_board[knight_cords[0]][knight_cords[1]] = True


# noinspection PyTypeChecker
def evaluate(free_cells=63, x=int, y=int):
    global knight_moves, counter
    if free_cells != 0:
        var = 0
        for i in knight_possible_moves:
            move_cords = (i[0] + x, i[1] + y)
            if 0 <= move_cords[0] < 8 and 0 <= move_cords[1] < 8 and not chess_board[move_cords[0]][move_cords[1]]:
                chess_board[move_cords[0]][move_cords[1]] = True
                knight_moves.append(move_cords)
                var = evaluate(free_cells - 1, move_cords[0], move_cords[1])
                if var == 1 and counter > 0:
                    evaluate(free_cells - 1, move_cords[0], move_cords[1])
                if counter == 0:
                    break
                knight_moves.pop(-1)
                chess_board[move_cords[0]][move_cords[1]] = False
        return 0
    else:
        if knight_moves not in result_list:
            counter -= 1
            result_list.append(knight_moves.copy())
        return 1


# noinspection PyTypeChecker
print(evaluate(x=knight_cords[0], y=knight_cords[1]))
print(len(knight_moves))
for i in result_list:
    for j in i:
        print(cords_to_letters(j), end=" ")
    print()
