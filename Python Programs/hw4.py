import random

#expo======================================
# Purpose: takes the x value and raises it to the y power
# Input Parameter(s):
# X: the value to be multiplied
# Y: the number of times x will be multiplied
# Return Value(s): Int-the x raised to y power
#==========================================

def expo(x,y):
    i=0
    sum=1
    while i<y:
        total=0
        j=0
        while j<x:
            total+=sum
            j+=1
        sum=total
        i+=1
    return sum


#rps_round===================================
# Purpose: plays a round of rock paper scissors
# Input Parameter(s): none
# Return Value(s): Int: 1 for a win, 0 for a tie, -1 for a loss
#==========================================
def rps_round():
    human_move=input('Enter R, P, or S: ')
    while human_move!='R' and human_move!='S' and human_move!='P':
        print('Invalid Input')
        human_move=input('Enter R, P, or S: ')
    comp_move=random.choice('RPS')
    print('Computer selects',comp_move)
    if comp_move==human_move:
        print('Tie!')
        return 0
    elif comp_move=='P' and human_move=='S':
        print('Player wins!')
        return 1
    elif comp_move=='S' and human_move=='R':
        print('Player wins!')
        return 1
    elif comp_move=='R' and human_move=='P':
        print('Player wins!')
        return 1
    else:
        print('Computer wins!')
        return -1
        
#rps_game===================================
# Purpose: plays multiple rounds of rock paper scissors until a winner is decided
# Input Parameter(s):
# num_wins: Int, how many rounds is needed to be won to win
# Return Value(s): Int: 1 for a win for the player, -1 for a loss for the player
#==========================================

def rps_game(num_wins):
    human_wins=0
    computer_wins=0
    i=0
    while i<num_wins:
        x=rps_round()
        if x>0:
            human_wins+=1
            i=human_wins
        elif x<0:
            computer_wins+=1
            i=computer_wins
        print()
        print('Player wins: '+str(human_wins))
        print('Computer wins: '+str(computer_wins))
    print()
    if computer_wins>human_wins:
        return -1
    else:
        return 1
