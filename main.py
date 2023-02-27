from copy import deepcopy
from os import system
from random import random
from time import sleep

class Board:
    def __init__(self, position: list[list[int]]):
        self.state = position

    def check_tie(self):
        markers = []

        for row in self.state:
            for marker in row:
                markers.append(marker)

        return 0 not in markers

    def check_win(self):
        # Check Lines
        for index in range(3):
            row = self.state[index]
            column = [row[index] for row in self.state]

            if row[0] == row[1] == row[2]: return row[0]
            if column[0] == column[1] == column[2]: return column[0]

        # Check Diagonals
        diagonal_one = [self.state[index][index] for index in range(3)]
        diagonal_two = [self.state[index][2 - index] for index in range(3)]

        if diagonal_one[0] == diagonal_one[1] == diagonal_one[2]: return diagonal_one[0]
        if diagonal_two[0] == diagonal_two[1] == diagonal_two[2]: return diagonal_two[0]

        return 0

    def draw_board(self):
        system("clear")
        marker_coversions = {1: "X", -1: "O", 0: " "}

        for row_number, row in enumerate(self.state):
            markers = [marker_coversions[marker] for marker in row]

            print("       |       |       ")
            print(f"   {markers[0]}   |   {markers[1]}   |   {markers[2]}   ")
            print("       |       |       ")

            if (row_number !=2 ): print("-----------------------")

    def add_marker(self, row: int, column: int, marker: int):
        self.state[row][column] = marker

class Computer:
    def find_possible_moves(self, state: list[list[int]]):
        # Stores Tuples as (Row, Column)
        possible_moves = []

        for row_number, row in enumerate(state):
            for column_number, marker in enumerate(row):
                if marker == 0: possible_moves.append((row_number, column_number))

        return possible_moves

    def evaluate_state(self, state: list[list[int]], turn: int):
        score = 0

        for possible_move in self.find_possible_moves(state):
            dummy_board = Board(state)
            dummy_board.add_marker(possible_move[0], possible_move[1], turn)

            score -= dummy_board.check_win()
            score += self.evaluate_state(dummy_board.state, -turn)

        return score

    def find_best_move(self, state: list[list[int]], turn: int):
        best_move = None
        best_score = None

        for possible_move in self.find_possible_moves(state):
            possible_state = deepcopy(state)
            possible_state[possible_move[0]][possible_move[1]] = turn

            possible_score = self.evaluate_state(possible_state, -turn)

            if best_score is None or possible_score > best_score:
                best_move = possible_move
                best_score = possible_score

        return best_move

if __name__ == "__main__":
    board = Board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    computer = Computer()
    turn = 1

    while not (board.check_tie() or board.check_win()):
        board.draw_board()

        if turn == 1:
            row = int(input("Row: "))
            column = int(input("Column: "))
        else: 
            sleep(random() * 2)
            row, column = computer.find_best_move(deepcopy(board.state), turn)

        board.add_marker(row, column, turn)
        turn *= -1

    board.draw_board()
    print("                        ")
    print("       GAME OVER!       ")

    if board.check_win() == 1: print("        YOU WIN!        ")
    elif board.check_win() == -1: print("       YOU LOSE!        ")
    else: print("          TIE!          ")
