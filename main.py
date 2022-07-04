from random import sample
from time import sleep

def _players_generator(rounds):
    rounds = rounds
    options = ["R", "P", "S"]
    for i in range(rounds):
        player1 = sample(options*rounds, rounds)
        player2 = sample(options*rounds, rounds)
    
    return player1, player2

def check_results(rounds):
    player1, player2 = _players_generator(rounds)

    player1_wins = 0
    player2_wins = 0
    n = 0

    while rounds != 0:
        results = [player1[n], player2[n]]
        print(f'Round {n+1}:')
        rounds -= 1
        n += 1

        #Tie cases
        if results[0] == "S" and results[1] == "S":
            print("TIE\n")
        elif results[0] == "P" and results[1] == "P":
            print("TIE\n")
        elif results[0] == "R" and results[1] == "R":
            print("TIE\n")
        
        #Player1 wins cases
        elif results[0] == "S" and results[1] == "P":
            print("Player 1 WINS this round\n")
            player1_wins += 1
        elif results[0] == "R" and results[1] == "S":
            print("Player 1 WINS this round\n")
            player1_wins += 1
        elif results[0] == "P" and results[1] == "R":
            print("Player 1 WINS this round\n")
            player1_wins += 1
        
        #Player2 wins cases
        elif results[0] == "S" and results[1] == "R":
            print("Player 2 WINS this round\n")
            player2_wins += 1
        elif results[0] == "P" and results[1] == "S":
            print("Player 2 WINS this round\n")
            player2_wins += 1
        elif results[0] == "R" and results[1] == "P":
            print("Player 2 WINS this round\n")
            player2_wins += 1

        sleep(0.8)
        
    if player1_wins > player2_wins:
        print(f'PLAYER 1 WINS BY {player1_wins}|{player2_wins}\n')
    elif player1_wins < player2_wins:
        print(f'PLAYER 2 WINS BY {player2_wins}|{player1_wins}\n')
    elif player1_wins == player2_wins:
        print(f'TIE BY {player1_wins}|{player2_wins}\n')

def play():
    rounds = input("How many rounds do you want?\nNumber of rounds: ")
    check_results(int(rounds))

if __name__ == '__main__':
    play()
