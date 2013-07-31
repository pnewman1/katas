#!/usr/bin/python

game_board = [ 
["x", "x", "x", "x", "", "o", "", "x"],
["", "x", "", "", "o", "", "", "o"],
["", "", "x", "o", "", "", "", "o"],
["", "", "o", "x", "", "", "", "o"],
["", "", "", "", "", "", "", "o"],
["", "", "x", "x", "x", "x", "", ""],
["", "o", "o", "o", "o", "", "", ""],
["o", "", "", "", "", "", "", ""]
]

def recurse_four(start_i, start_j, follow_i, follow_j, match_piece, game_board, match_count):
    
    if start_j+follow_j < len(game_board[start_i]) and start_i+follow_i < len(game_board) and start_j+follow_j >= 0 and start_i + follow_i >= 0:
        if game_board[start_i + follow_i][start_j + follow_j] == match_piece:
            #print game_board[start_i + follow_i][start_j + follow_j]
            i = start_i+follow_i
            j = start_j+follow_j
            match_count+=1
            if match_count < 4:
                recurse_four(i, j, follow_i, follow_j, match_piece, game_board, match_count)
            else:
                print "four in a row! of %s" % match_piece
                print "ending at", i, j
                return
        else:
           return
    else:
        return

for i in range(0, len(game_board)):
    for j in range(0, len(game_board[i])):
        #print i, j, game_board[i][j]
        current_piece = game_board[i][j]
        if current_piece == "x" or current_piece == "o": 
            #find horizontal matches
            recurse_four(i, j, 0, 1, current_piece, game_board, 1)
            #find vertical matches
            recurse_four(i, j, 1, 0, current_piece, game_board, 1)
            #diaganol matches
            recurse_four(i, j, 1, 1, current_piece, game_board, 1)
            #diaganol matches going the other way
            recurse_four(i, j, 1, -1, current_piece, game_board, 1)
        
