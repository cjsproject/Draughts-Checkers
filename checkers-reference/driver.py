#!/bin/sh
#echo DEFANGED.2800
#exit
#!/usr/bin/env python

import sys,os,time,random
import math
from imp import find_module, new_module, load_compiled, PY_SOURCE, PY_COMPILED


#The following function is used to output the current board(after move)
#and the parent board (before move), if the parent board is provided
def BoardPrint(board,move=[],name="====== The current board is: ======",parent_board = None,num =0 ):
    if parent_board:
        #print("The parent board is:", name)
        print("The parent board(",num - 1,") is:", "====== The current board(",num,")is: ======")
        if move:
            print("move = ",move)
        for i in [7,6,5,4,3,2,1,0]:
            print(i,":", end=" ")
            for j in range(8):
                print(parent_board[i][j], end=" ")
            print("\t     |\t  ",i,":", end=" ")
            for j in range(8):
                print(board[i][j], end=" ")
            print()
        print("   ",0,1,2,3,4,5,6,7,"\t     |\t     ",0,1,2,3,4,5,6,7)
    else:
        #print(name)
        print("====== The current board(",num,")is (after move): ======")
        if move:
            print("move = ",move)
        for i in [7,6,5,4,3,2,1,0]:
            print(i,":", end=" ")
            for j in range(8):
                print(board[i][j], end=" ")
            print()
        print("   ",0,1,2,3,4,5,6,7)
    print("")

def BoardCopy(board):
    new_board = [[]]*8
    for i in range(8):
        new_board[i] = [] + board[i]
    return new_board

#========================================================
def Parse_Move(move):
    print(type(move))
    return True

def legal(move,state,player):
    if version == 0:
        return True
    else:
        if not move:
            return True
        else:
            new_state = doit(move,state)
            if new_state in successors(state,player):
                return True
            else:
                return 0

def doit(move,state):
    new_state = BoardCopy(state)
    #print("player",player)
    #Move one step
    if len(move) == 2 and abs(move[1][0] - move[0][0]) == 1:         
        new_state[move[0][0]][move[0][1]] = '.'
        if state[move[0][0]][move[0][1]] == 'b' and move[1][0] == 7:
            new_state[move[1][0]][move[1][1]] = 'B'
        elif state[move[0][0]][move[0][1]] == 'r' and move[1][0] == 0:
            new_state[move[1][0]][move[1][1]] = 'R'
        else:
            new_state[move[1][0]][move[1][1]] = state[move[0][0]][move[0][1]]
    #Jump
    else:
        step = 0;
        new_state[move[0][0]][move[0][1]] = '.'
        while step < len(move)-1:
            new_state[int(math.floor((move[step][0]+ move[step+1][0])/2))][int(math.floor((move[step][1]+ move[step+1][1])/2))] = '.'                        
            step = step+1
        if state[move[0][0]][move[0][1]] == 'b' and move[step][0] == 7:
            new_state[move[step][0]][move[step][1]] = 'B'
        elif state[move[0][0]][move[0][1]] == 'r' and move[step][0] == 0:
            new_state[move[step][0]][move[step][1]] = 'R'
        else:
            new_state[move[step][0]][move[step][1]] = state[move[0][0]][move[0][1]]
    return new_state

        
#======================================================================
Initial_Board = [ ['b','.','b','.','b','.','b','.'],\
                  ['.','b','.','b','.','b','.','b'],\
                  ['b','.','b','.','b','.','b','.'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','r','.','r','.','r','.','r'],\
                  ['r','.','r','.','r','.','r','.'],\
                  ['.','r','.','r','.','r','.','r'] \
                ]

Test_Board1 =   [ ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','B','.','.','.','R'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','.','.','R','.','.'],\
                  ['.','.','.','.','.','.','.','.'],\
                  ['.','.','.','.','.','.','.','.'] \
                ]

Test_Board2 = [ ['.','.','.','.','.','.','b','.'],\
    ['.','.','.','b','.','b','.','b'],\
    ['b','.','.','.','.','.','b','.'],\
    ['.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','b','.','.','.'],\
    ['.','.','.','.','.','B','.','.'],\
    ['b','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','r'],\
    ]

Test_Board3 = [ ['.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.'],\
    ['.','.','B','.','.','.','b','.'],\
    ['.','.','.','b','.','B','.','.'],\
    ['.','.','.','.','R','.','.','.'],\
    ['.','.','.','b','.','B','.','.'],\
    ['.','.','b','.','.','.','b','.'],\
    ['.','.','.','.','.','.','.','.'],\
    ]


def IsBoardLegal(test_board):
    legal = 1
    red_num = 0
    black_num = 0
    
    for i in range(8):
        for j in range(8):
            if (i+j) %2 == 0:
                if test_board[i][j] == 'r' or test_board[i][j] == 'R':
                    red_num += 1
                elif test_board[i][j] == 'b' or test_board[i][j] == 'B':
                    black_num += 1
                elif test_board[i][j] != '.':
                    print("Position (",i,j,") is wrong and it should be one of '.', 'b', 'B', 'r' or 'R' ")
                    legal = 0
            else:
                if test_board[i][j] != '.':
                    print("Position (",i,j,") is wrong and it should be '.'")
                    legal = 0

    if red_num > 12:
        print("The number of red pieces should less than or equal to 12, now it is", red_num)
        legal = 0

    if black_num > 12:
        print("The number of black pieces should less than or equal to 12, now it is", black_num)
        legal = 0

    return legal        
    

def play(file_A, file_B,start_state = Initial_Board):
#    exec("import " + file_A + " as Aplayer")
#    exec("import " + file_B + " as Bplayer")
#    Aplayer = imp.load_source(file_A, file_A + ".py")
#    Bplayer = imp.load_source(file_B, file_B + ".py")

    Aplayer = import_script(file_A)
    Bplayer = import_script(file_B)

    A = Aplayer.GameEngine('r')
    B = Bplayer.GameEngine('b')
    
    currPlayer = A
    state = start_state    

    previous_states_list = []
    draw_flag = 0
    board_num = 0
    n_repeat_allowed = 10;
    
    print("'r': ", file_A," is ready")
    print("'b': ", file_B," is ready")
    print()
    
    BoardPrint(state,name="====== The initial board (0) is: ======")
    
    while True:
        print("It is ", currPlayer ,"'s turn")

        start = time.time()
        move = currPlayer.nextMove(state)
        elapse = time.time() - start

        if not move:
            break

        #Check draw
        if currPlayer == A:
            player_name = 'r'
        else:
            player_name = 'b'
            
        state_with_player = [state, player_name]
        
        if state_with_player in previous_states_list:
            n_repeat_allowed -= 1
            
            ind = previous_states_list.index(state_with_player)
            ind = board_num - len(previous_states_list) + ind ;
            
            n_r = 0
            n_R = 0
            n_b = 0
            n_B = 0
                
            for i in [7,6,5,4,3,2,1,0]:
                for j in range(8):
                    if state[i][j] == 'r':
                        n_r += 1
                    elif state[i][j] == 'R':
                        n_R += 1
                    elif state[i][j] == 'b':
                        n_b += 1
                    elif state[i][j] == 'B':
                        n_B += 1
                        
            print("** The current board is the same as the", ind, "th board")
            print("You might need to create a better heutistic function")
            
            if n_r + n_R < n_b + n_B and currPlayer == A:
                if n_repeat_allowed <= 1:
                    print("** Both players are generating non-effective moves. The judgement is made by the number of remaining checkers.")
                    n_repeat_allowed = 0
            elif n_r + n_R > n_b + n_B and currPlayer == B:
                if n_repeat_allowed <= 1:
                    print("** Both players are generating non-effective moves. The judgement is made by the number of remaining checkers.")
                    n_repeat_allowed = 0
            elif n_r + n_R == n_b + n_B:
                draw_flag = 1
            
            if n_repeat_allowed == 0:
                break
        else:
        	n_repeat_allowed = 10;
        
        previous_states_list.append(state_with_player);
        if(len(previous_states_list) > 100):
            previous_states_list = previous_states_list[1:]

        print("The move is : ",move, end="")
        print(" (in %.2f s)" % elapse, end="")
        if elapse > 60.0:
            print("\n** '", currPlayer, "' took more than one minute!!")
            break
        print()
        parent = BoardCopy(state);
        if legal(move, state,currPlayer.str):
            state = doit(move,state)

        board_num = board_num + 1
        #BoardPrint(state,parent_board = parent, num = board_num)
        BoardPrint(state,num = board_num)

        if currPlayer == A:
            currPlayer = B
        else:
            currPlayer = A

    print("Game Over")
    if draw_flag:        
        print("It is a DRAW; black wins")
        print("The Winner is:",file_B, 'b')
    elif currPlayer == A:    
        print("The Winner is:",file_B, 'b')
    else:
        print("The Winner is:",file_A, 'r')


# import the user script
def import_script(name):
    fileobj, path, description = find_module(name)
	
    nofile = True
	
    if description[2] == PY_SOURCE:
        code = compile(fileobj.read(), path, "exec")
        nofile = False

        expected = list(EXPECTED)
        for const in code.co_consts:
            if isinstance(const, type(code)) and const.co_name in expected:
                expected.remove(const.co_name)
        if expected:
            raise ImportError("missing expected function: {}".format(expected))

        module = new_module(name)
        exec(code, module.__dict__)
        sys.modules[name] = module
        return module
        
    elif description[2] == PY_COMPILED:
        module = load_compiled(name,path)
        nofile = False
        return module
    
    if nofile:
        raise ImportError("no source file found")


# global variables
EXPECTED = ( "evalFun", "cutoff" )


# main script
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: python", sys.argv[0], "<Aplayer name> <Bplayer name>\n")
        sys.exit()

    Aplayer = sys.argv[1]
    Bplayer = sys.argv[2]

    #if version = 0, we will not check the correctness of a move
    version = 0
    
    print(os.uname())
    print()
    
    random.seed()
    p_coin = random.random()
    print("Determining the colors by coin flipping...[", ("%.1f" % p_coin).lstrip('0'), end="")
    
    game_start = time.time()
    if p_coin > 0.5:
    	print(" > .5 ]: head")
    	print()
    	play(Aplayer,Bplayer)
    else:
    	print(" < .5 ]: tail")
    	print()
    	play(Bplayer,Aplayer)
    	
    game_elapse = time.time() - game_start
    print(" (Game took %.2f s)" % (game_elapse))
    
    # sample function calls
    #play("checkers","???checkers")
    #play("???checkers","checkers")
    
    #play("checkers","checkers",start_state = Test_Board1)
    #play("checkers","checkers",start_state = Test_Board2)
    #play("checkers","checkers",start_state = Test_Board3)
    
    #if IsBoardLegal(Test_Board1):
    #    print("The board is legal")
    #else:
    #    BoardPrint(Test_Board1)
    #    print("The board is not legal")
    
"""
CHANGELOG
(09/18/2014 by charmgil)
- def import_script(name) is added

(09/23/2013 by charmgil)
- time#9,187,189,215-218: time measurement is added 

(09/15/2013: ported by charmgil)
- 'print' has been replaced with 'print()'
- line#7-8: 'imp, math' is added
- line#81: list index has been modified
- line#168-169: 'imp.load_source()' replaced 'exec(...)' statement
"""
