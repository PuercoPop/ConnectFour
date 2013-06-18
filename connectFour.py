#!/usr/bin/env python
"""
Connect 4 for Python
"""


class ConnectFour(object):
    def __init__(self, columns=7, column_size=6):
        self.board = Board(columns, column_size)

    def checkWinner(self):
        return (self.board.checkHorizontal() or
                self.board.check_vertical_diagonal())

    def checkValidInput(self, userInput):
        valid = False
        try:
            userInput = int(userInput)
        except ValueError:
            pass
        else:
            if userInput in range(1, self.board.columns + 1):
                valid = True
        if type(userInput) is str and userInput.lower() == 'q':
            valid = True
        return valid

    def play(self):
        player = 'P'
        counter = 1
        while True:
            print self.board
            msg = player + "'s turn. "
            d = raw_input(msg + "Enter a column number to move: ")
            if self.checkValidInput(d):
                try:
                    d = int(d)
                except ValueError:
                    pass
                if type(d) is int:
                    for index, row in enumerate(self.board.board):
                        if self.board.checkEmpty(index, d-1):
                            self.board.board[index][d-1] = player
                            if player == 'P':
                                player = 'C'
                            elif player == 'C':
                                player = 'P'
                            break
                else:
                    if d.lower() == 'q':
                        break
            potentialWinner = self.checkWinner()
            if potentialWinner:
                print str(potentialWinner) + " won the game!"
                print self.board
                break


class Board(object):
    def __init__(self, columns=7, column_size=6):
        self.columns = columns
        self.column_size = column_size
        self.resetBoard()

    def checkEmpty(self, x, y):
        return self.board[x][y] == '_'

    def resetBoard(self):
        self.board = [['_' for j in range(self.columns)]
                      for i in range(self.column_size)]

    def __str__(self):
        columnNumbers = ""
        for i in range(self.columns + 1):
            if i != 0:
                columnNumbers += str(i) + " "
        output = "\n" + columnNumbers + "\n"
        for row in reversed(self.board):
            rowString = ""
            for elem in row:
                rowString += str(elem) + " "
            output += rowString + "\n"
        return output

    def checkHorizontal(self):
        for row in self.board:
            pw = None
            if row.count('C') >= 4:
                pw = 'C'
            elif row.count('P') >= 4:
                pw = 'P'
            if pw:
                winCounter = 1
                prev_index = 0
                for index, val in enumerate(row):
                    if val == pw:
                        if prev_index + 1 == index:
                            winCounter += 1
                        prev_index = index
                if winCounter == 4:
                    return pw
        return False

    def check_vertical_diagonal(self):
        """
        >>> 1 + 1
        3

        """
        for rowIndex, row in enumerate(self.board):
            maxLength = len(self.board) - 4
            if rowIndex <= maxLength:
                for index, val in enumerate(row):
                    if val == 'C' or val == 'P':
                        if self.check_vertical_winning_condition(val,
                                                                 rowIndex,
                                                                 index):
                            return val
                        if self.check_diagonal_winning_condition(val,
                                                                 index,
                                                                 rowIndex,
                                                                 maxLength):
                            return val
        return False

    def check_vertical_winning_condition(self, val, rowIndex, index):
        return (val == self.board[rowIndex + 1][index] and
                val == self.board[rowIndex + 2][index] and
                val == self.board[rowIndex + 3][index])

    def check_diagonal_winning_condition(self, val,
                                         index, rowIndex, maxLength):
        return ((index <= maxLength and
                 val == self.board[rowIndex + 1][index + 1] and
                 val == self.board[rowIndex + 2][index + 2] and
                 val == self.board[rowIndex + 3][index + 3]) or
                (index >= maxLength and
                 val == self.board[rowIndex + 1][index - 1] and
                 val == self.board[rowIndex + 2][index - 2] and
                 val == self.board[rowIndex + 3][index - 3]))

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    game = ConnectFour()
    game.play()
