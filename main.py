class Board:
    def __init__(self, position: list[list[int]]):
        self.position = position

    def checkWin(self):
        # Check Lines
        for index in range(2):
            row = self.position[index]
            column = [row[index] for row in this.position]

            if row[0] == row[1] == row[2]: return row[0]
            if column[0] == column[1] == column[2]: return column[0]

        # Check Diagonals
        diagonal_one = [this.position[index][index] for index in range(2)]
        diagonal_two = [this.position[index][2 - index] for index in range(2)]

        if diagonal_one[0] == diagonal_one[1] == diagonal_one[2]: return diagonal_one[0]
        if diagonal_two[0] == diagonal_two[1] == diagonal_two[2]: return diagonal_two[0]

        return 0
