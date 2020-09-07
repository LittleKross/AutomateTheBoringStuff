# Chess Dictionary Validator
# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function
# named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid
# space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight',
# 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.


def validatePosition(position):
    return int(position[0:1]) <= 8 and int(position[0:1]) >= 1 and position[1:2] in ["a", "b", "c", "d", "e", "f", "g", "h"] and len(position) == 2


def validatePiece(piece):
    return piece[0:1] in ["b", "w"] and piece[1:] in ["pawn","knight","bishop","rook","queen","king",]

def isValidChessBoard(board):
    blackCounter = 0
    whiteCounter = 0
    pawnCounter = 0
    bkingPresent = False
    bqueenPresent = False
    wkingPresent = False
    wqueenPresent = False
    for place, piece in board.items():
        if validatePosition(place) and validatePiece(piece):
            if piece[0:1] == "b":
                blackCounter += 1
                if piece[1:] == "king":
                    kingsPresent += 1
                elif piece[1:] == "queen":
                    queensPresent += 1
            elif piece[0:1] == "w":
                whiteCounter += 1
                if piece[1:] == "king":
                    kingsPresent += 1
                elif piece[1:] == "queen":
                    queensPresent += 1
            print(
                "Invalid position or piece: {"
                + place
                + ","
                + piece
                + "}, please ensure that all pieces are correct and held within the realm of reality... i.e. the plane of a chess board"
            )
            return False
        elif blackCounter > 16 or whiteCounter > 16:
            print(
                "Invalid board: {"
                + place
                + ","
                + piece
                + "}, Too many pieces on the board."
            )
            return False
        elif (bkingPresent or bqueenPresent or wkingPresent or wqueenPresent):
            print(
                "Invalid board: {"
                + place
                + ","
                + piece
                + "}, More than one king or queen."
            )
            return False
        else:
            print("Invalid board: {" + place + "," + piece + "}, Unknown error")
            return False
    return True

def main():
    chessBoard = {
        "1a": "bking",
        "2a": "bqueen",
        "3a": "brook",
        "4a": "brook",
        "5a": "bknight",
        "6a": "bknight",
        "7a": "bbishop",
        "8a": "bbishop",
        "1b": "bpawn",
        "2b": "bpawn",
        "3b": "bpawn",
        "4b": "bpawn",
        "5b": "bpawn",
        "6b": "bpawn",
        "7b": "bpawn",
        "8b": "bpawn",
        "1c": "wking",
        "2c": "wqueen",
        "3c": "wrook",
        "4c": "wrook",
        "5c": "wbishop",
        "6c": "wbishop",
        "7c": "wknight",
        "8c": "wknight",
        "1e": "wpawn",
        "2e": "wpawn",
        "3e": "wpawn",
        "4e": "wpawn",
        "5e": "wpawn",
        "6e": "wpawn",
        "7e": "wpawn",
        "8e": "wpawn",
    }
    if isValidChessBoard(chessBoard):
        print("Valid board")
main()
