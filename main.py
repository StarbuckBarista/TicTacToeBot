from os import system

class Board:
    def __init__(self, position: list[list[int]]):
        self.position = position

    def checkWin(self):
        # Check Lines
        for index in range(2):
            row = self.position[index]
            column = [row[index] for row in self.position]

            if row[0] == row[1] == row[2]: return row[0]
            if column[0] == column[1] == column[2]: return column[0]

        # Check Diagonals
        diagonal_one = [self.position[index][index] for index in range(3)]
        diagonal_two = [self.position[index][2 - index] for index in range(3)]

        if diagonal_one[0] == diagonal_one[1] == diagonal_one[2]: return diagonal_one[0]
        if diagonal_two[0] == diagonal_two[1] == diagonal_two[2]: return diagonal_two[0]

        return 0

    def addMarker(self, row: int, column: int, marker: int):
        self.position[row][column] = marker

if __name__ == "__main__":
    board = Board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    while not board.checkWin():
        system("clear")

        for row in board.position:
            print(row)

        row = int(input("Row: "))
        column = int(input("Column: "))
        marker = int(input("Marker: "))

        board.addMarker(row, column, marker)
