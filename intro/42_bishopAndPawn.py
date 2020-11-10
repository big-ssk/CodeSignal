def bishopAndPawn(bishop, pawn):
        
    bishop_x, bishop_y = ord(bishop[0]), int(bishop[1])
    pawn_x, pawn_y = ord(pawn[0]), int(pawn[1])
    
    return pawn_x - bishop_x == pawn_y - bishop_y or -pawn_x + bishop_x == pawn_y - bishop_y
