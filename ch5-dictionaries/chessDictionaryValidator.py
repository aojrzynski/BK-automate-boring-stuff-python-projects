#! python3
# chessDictionaryValidator.py - Checks is submitted dictionary has valid chess board moves.

def isValidChessBoard(board):
    pieceNames = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    bking=0
    wking=0
    white = 0
    black = 0
    whitePawns = 0
    blackPawns = 0

    for chessPiece in board.values():
        # Check if chess piece name is valid.
        if chessPiece[0] != "b" and chessPiece[0] != "w":
            return False
        elif chessPiece[1:] not in pieceNames:
            return False 

        # Count the kings.
        if chessPiece == 'bking':
            bking += 1
        if chessPiece == 'wking':
            wking += 1

        # Count the white and black pieces.
        if chessPiece[0] == 'w':
            white += 1
        elif chessPiece[0] == 'b':
            black += 1

        # Count number of pawns.
        if chessPiece == 'wpawn':
            whitePawns += 1
        elif chessPiece == 'bpawn':
            blackPawns += 1
    
    # Check if location is valid.
    boardSpaceLetters = ['a','b','c','d','e','f','g','h']
    boardSpaceNumbers = ['1','2','3','4','5','6','7','8',]
    for space in board.keys():
        if space[0] not in boardSpaceLetters:
            if space[1] not in boardSpaceNumbers:
                return False
     
    if bking != 1 or wking != 1:
        return False         
    if white > 16 or white > 16:
        return False     
    if whitePawns > 8 or blackPawns > 8:
        return False  
        
    return True

print(isValidChessBoard({"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking"})) # True.
print(isValidChessBoard({"a1": "bpawn", "a2": "wking"}))  # False.
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop"}))  # False.
print(isValidChessBoard({"a1": "bking", "z9": "wking"}))  # False.
print(isValidChessBoard({'a1':'bking','a2':'wking','h1':'bpawn','h2':'bpawn','h3':'bpawn','h4':'bpawn','h5':'bpawn','h6':'bpawn','h7':'bpawn','h8':'bpawn','g7':'bpawn','g8':'bpawn'}))#False.
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop", "c4": "bking"})) # False.