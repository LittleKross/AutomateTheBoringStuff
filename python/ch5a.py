# Chess Dictionary Validator
# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function
# named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid
# space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight',
# 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.


def validatePosition(position):
    return (
        position[0:1] in ["1", "2", "3", "4", "5", "6", "7", "8"]
        and position[1:2] in ["a", "b", "c", "d", "e", "f", "g", "h"]
        and len(position) == 2
    )


def validatePiece(piece):
    return piece[0:1] in ["b", "w"] and piece[1:] in [
        "pawn",
        "knight",
        "bishop",
        "rook",
        "queen",
        "king",
    ]


# Requires a dict of dicts
def isValidChessBoard(board):
    blackCounter = 0
    whiteCounter = 0
    pawnCounter = 0
    for place, piece in board.items():
        if validatePosition(place) and validatePiece(piece):
            if piece[1:] == "b":
                blackCounter += 1
            else:
                whiteCounter += 1
        else:
            print(
                "Invalid position or piece: {"
                + place
                + ","
                + piece
                + "}, please ensure that all pieces are correct and held within the realm of reality... i.e. the plane of a chess board"
            )
    return True


def main():
    chessBoard = {"1a": "btext"}
    isValidChessBoard(chessBoard)


main()
