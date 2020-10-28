import numpy as np


# ECE 105: Programming for Engineers II (Spring, 2020)
# HW : DNA Word Search
# Student name:     Zohair Hasan  <------------ FIXED
# Email ID:         zh393              <------------ FIXED


# --- COMPLETE THE FIND FUNCTION BELOW --------------------------------------
# return True if the string "word" is in the input array "board", else False
def find(word):
    if checkVertical(word) or checkHorizontal(word) or checkDiagonal(word):
        return True
    else:
        return False


# --- COMPLETE THE FIND FUNCTION ABOVE --------------------------------------

def checkVertical(word):  # --checks every coulmn, both forward and reverse

    found = False
    # ===========================================
    # --checks every column in forward direction
    # ===========================================
    for current_column in range(board.shape[1]):
        # --goes through all the columns in array
        if found:
            break

        for current_rows in range(board.shape[0] - len(word) + 1):
            # --goes through the first element of set of rows to be checked
            if found:
                break
            current_word = ""
            # --initialize word being checked

            for i in range(current_rows, current_rows + len(word)):
                current_word += board[i, current_column]
                #  --form the first word using the first element of set of rows
                # to be checked and the next rows after it

            if current_word == word:
                found = True
                break
                #  --check whether the word formed is the same as the search
    # ============================================
    # --checks every column in reverse direction
    # ============================================
    for current_column in range(board.shape[1]):
        # --goes through all the columns in array
        if found:
            break

        for current_rows in range(board.shape[0], len(word) - 1, -1):
            # --goes through the first element of set of rows to be checked

            if found:
                break

            current_word = ""
            # --initialize word being checked
            for i in range(current_rows - 1, current_rows - len(word) - 1, -1):
                current_word += board[i, current_column]
                # --form the first word using the last element of set of rows
                # to be checked and the rows before it
            if current_word == word:
                found = True
                break
                # --check whether the word formed is the same as the search
    return found


def checkHorizontal(word):  # --checks every row, both forward and reverse

    found = False

    # =========================================
    # --checks every row in forward direction
    # =========================================
    for current_row in range(board.shape[0]):
        # --goes through all the rows in the array
        if found:
            break

        for current_columns in range(board.shape[1] - len(word) + 1):
            # --goes through first element of set of columns to be checked
            if found:
                break

            current_word = ""
            # -- initialize word being checked

            for i in range(current_columns, current_columns + len(word)):
                current_word += board[current_row, i]
                #  --form the first word using the first element of set of rows
                # to be checked and the next rows after it
            if current_word == word:
                found = True
                break
                #  --check whether the word formed is the same as the search

    # =========================================
    # --checks every row in reverse direction
    # =========================================

    for current_row in range(board.shape[0]):
        # --goes through all the rows in array
        if found:
            break

        for current_columns in range(board.shape[1], len(word) - 1, -1):
            # --goes through the first element of set of rows to be checked

            if found:
                break

            current_word = ""
            # --initialize word being checked
            for i in range(current_columns - 1, current_columns - len(word) - 1, -1):
                current_word += board[current_row, i]
                # --form the first word using the last element of set of rows
                # to be checked and the rows before it
            if current_word == word:
                found = True
                break
                # --check whether the word formed is the same as the search

    return found


def checkDiagonal(word):  # --checks every row, both forward and reverse

    found = False

    # ========================================
    # --checks diagonals in normal direction
    # ========================================
    for offset in range(np.negative(board.shape[0]) + 1, board.shape[1]):
        list_diagonals = list(board.diagonal(offset))
        string_diagonals = "".join(list_diagonals)
        rvsdword = word[::-1]
        if word in string_diagonals or rvsdword in string_diagonals:
            found = True
            break

    # =========================================
    # --checks diagonals in reverse direction
    # =========================================

    if not found:
        boardflip = np.fliplr(board)
        for offset in range(np.negative(boardflip.shape[0]) + 1, boardflip.shape[1]):
            list_diagonals = list(boardflip.diagonal(offset))
            string_diagonals = "".join(list_diagonals)
            rvsdword = word[::-1]
            if word in string_diagonals or rvsdword in string_diagonals:
                found = True
                break

    return found


# --- YOU MAY TEST YOUR CODE BELOW ------------------------------------------
if __name__ == '__main__':   # check if run this script as the main file
    # If run this Python script file as the main file, then do following tests
    # else (e.g. when import this script into another file), the following
    #   code will be skipped.

    # --- Example test setup 1: for testing the whole function "find"

    board = np.array([['A', 'A', 'A', 'T'],
                      ['A', 'G', 'G', 'C'],
                      ['A', 'T', 'G', 'C'],
                      ['A', 'A', 'T', 'A'],
                      ['A', 'T', 'A', 'A']])
    word = 'ACCT'  # Expect True, ACCT is at the last column, read upward
    # word = 'CTT'  # Expect True, CTT is at anti diag, SouthWest direction
    # word = 'ATTA'  # Expect True, ATTA is at diag, SouthEast direction
    # word = 'AAA' # Expect True, found in many directions and locations
    # word = 'TTTA' # Expect False, not anywhere
    # word = 'TTTAGCTA' # Expect False, not anywhere, also too long

    print('=== Test case starts ===========================================')
    result = find(word)
    print(board)
    print('*** Target word:', word, '\tResult:', result)
    print('=== Test case ends ===========================================')

    # --- Example test setup 2: for testing individual subtasks
    #     such as "checkDiagFor" function (if you have one)
    # board = np.array([['A','A','A','T'],
    # ['A','G','G','C'],
    # ['A','T','G','C'],
    # ['A','A','T','A'],
    # ['A','T','A','A'],
    # ['B','D','C','F']])

    # print('*** Result 1: ', checkVertical('FAACCAAAAAAA') ) # TrueS
    # print('*** Result 2: ', checkHorizontal('AATA') ) # False
    # print('*** Result 3: ', checkDiagonal('TTC') )  # True
