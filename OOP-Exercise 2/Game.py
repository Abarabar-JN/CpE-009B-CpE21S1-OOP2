import random
from Character import Character
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

def select_role(): #Allows the players to select their roles based on the type of game chosen or whether it is granted access to be used
    roles = {"1": Swordsman, "2": Archer, "3": Magician} #Choices or roles sorted by number
    print("Select your role:\n1. Swordsman\n2. Archer\n3. Magician") 
    choice = input("Enter the number for your choice of role: ") #Allows the user to choose by number input
    return roles.get(choice, Novice)

def battle(player, opponent):
    while player.getHp() > 0 and opponent.getHp() > 0: #Inittiates the while loop
        for current, target in [(player, opponent), (opponent, player)]: #Sets the turn order for the player or the npc, but the player always goes first
            if current == player: #Checks if its the player's turn and allows the player to choose their form of attack which can vary on their role
                action = input(f"{current.getUsername()}'s Turn! Choose action (1: Basic Attack, 2: Special Attack): ")
                if action == '1':
                    current.basicAttack(target)
                elif action == '2':
                    if isinstance(current, Swordsman):
                        current.slashAttack(target)
                    elif isinstance(current, Archer):
                        current.rangedAttack(target)
                    elif isinstance(current, Magician):
                        current.magicAttack(target)
                else:
                    print("Invalid action. Turn skipped.") #Skips the turn if the incorecct value is placed
            else:
                action = random.choice(['basic', 'slash', 'magic']) #Sets the attack randomly choce for the monster 
                getattr(current, f"{action}Attack")(target)
                
#If single player is chosen, creates and sets the boss as monster and allows the player to input their own username
def player_vs_computer():
    player_wins = 0 
    while True:
        print("\n--- Single Player Mode ---")
        player = Novice(input("Enter username: "))
        monster = Boss("Monster")
        battle(player, monster) #Initiates the fight between the two
        
#Sets the win condition of the player and also sets the condition of allowing role selection once two wins is achieved.
        if monster.getHp() <= 0:
            player_wins += 1
            print(f"{monster.getUsername()} has been defeated! Your wins: {player_wins}")
            if player_wins >= 2:
                player = select_role()(player.getUsername())
        
        if input("Play again? (y/n): ").lower() != 'y': #Allows the player to play again or quit
            break

def player_vs_player():
    wins = {"Player 1": 0, "Player 2": 0}#Keeps track of players wins
    while True: #Starts and continues loop until it is ended by the players 
        print("\n--- Player vs Player Mode ---")
        player1 = select_role()(input("Enter Player 1 username: "))
        player2 = select_role()(input("Enter Player 2 username: "))
        battle(player1, player2)

        if player2.getHp() <= 0:#Sets the win conditions and displays whoever wins and also allows players to choose to end or continue
            wins["Player 1"] += 1
            print(f"{player2.getUsername()} has been defeated! Current Wins: Player 1: {wins['Player 1']}, Player 2: {wins['Player 2']}")
        else:
            wins["Player 2"] += 1
            print(f"{player1.getUsername()} has been defeated! Current Wins: Player 1: {wins['Player 1']}, Player 2: {wins['Player 2']}")

        if input("Play again? (y/n): ").lower() != 'y':
            break
#Prompts mode selection to toggle between pvp or solo player depending on the value chosen
if __name__ == "__main__":
    mode = input("Select mode (1: Single Player, 2: Player vs Player): ")
    if mode == '1':
        player_vs_computer()
    elif mode == '2':
        player_vs_player()
    else:
        print("Invalid mode selected.")


