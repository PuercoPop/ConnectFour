#!/usr/bin/env python
"""
Connect 4 for Python
"""
import sys


class ConnectFour(object):
    def __init__(self, columns=7, column_size=6):
        self.board = Board(columns, column_size)

    def checkWinner(self):
        return (self.board.checkHorizontal() or
                self.board.check_vertical_diagonal())

    def checkValidInput(self, user_input):
        """Valid inputs are q plus the integers from 1 to ...
        """
        user_input = user_input.lower()

        if user_input in ([str(i) for i in range(1, self.board.columns + 1)] +
                          ['q']):
            return True
        else:
            return False


    def read_player_move(self, current_player):
        """Read Input until"""
        while True:
            move = raw_input(
                current_player + "'s turn. Enter a column number to move: ")
            if self.checkValidInput(move):
                try:
                    return int(move)
                except ValueError:
                    # Assuming it can only be q. Don't like this solution,
                    # quiting the project earlier would be cleaner but
                    # quiting the programing in the main loop seems more
                    # appropiate.
                    return move

    def play(self):
        player = 'P'
        counter = 1
        while True:
            print self.board
            move = self.read_player_move(player)
            if move == 'q':
                sys.exit(0)
            for index, row in enumerate(self.board.board):
                if self.board.checkEmpty(index, move - 1):
                    self.board.board[index][move - 1] = player
                    if player == 'P':
                        player = 'C'
                    elif player == 'C':
                        player = 'P'
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
    game = ConnectFour()
    game.play()
