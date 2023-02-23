from os import system

class Board:
    def __init__(self, position: list[list[int]]):
        self.state = position

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
    def update_state(self, state: list[list[int]]):
        self.state = state

    def find_possible_moves(self):
        # Stores Tuples as (Row, Column)
        possible_moves = []

        for row_number, row in enumerate(self.state):
            for column_number, marker in enumerate(row):
                if marker == 0: possible_moves.append((row_number, column_number))

        return possible_moves

if __name__ == "__main__":
    board = Board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    computer = Computer()

    while not board.check_win():
        computer.update_state(board.state)
        board.draw_board()

        row = int(input("Row: "))
        column = int(input("Column: "))
        marker = int(input("Marker: "))

        board.add_marker(row, column, marker)
