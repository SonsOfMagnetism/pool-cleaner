##############
# Game State #
##############

# This is where we stiore the current state of the game
game = {"tool": 0, "money": 0}

# This is a list of tools the player can use
tools = [
    {"name": "Small Net", "profit": 10, "cost": 0},
    {"name": "Big Net", "profit": 100, "cost": 100},
]

########################
# Game Option Function #
########################

# This function allows the player to clean a pool and make money
def clean_pool():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about cleaning a pool and make money
    print(f"You clean a pool with your {tool['name']} and make {tool['profit']}")
    # Update the player's money
    game["money"] += tool["profit"]
    
# This function allows the player to see their stats (money and tool)
def check_stats():
    # Get the current tool being used by the player
    tool = tools[game["tool"]]
    # Print the message about the player's tool and money
    print(f"You currently have {game['money']} and are using a {tool['name']}")
    
# This function allows the player to upgrade their tool
def upgrade():
    # Check if there are no more upgrades available
    if (game["tool"] >= len(tools) - 1):
        print("no more upgrades")
        return 0
    # Get the next tool the player can upgrade to
    next_tool = tools[game["tool"]+1]
    # Check if the next tool is not available
    if (next_tool == None):
        print("There is no more tools")
        return 0
    # Check if the player has enough money to upgrade
    if (game["money"] < next_tool["cost"]):
        print('Not enough to buy tool')
        return 0
    # Print the message about upgrading the tool
    print("You are upgrading your tool")
    # Deduct the cost of the upgrade from the player's money
    game["money"] -= next_tool["cost"]
    # Increase the player's tool to the next level
    game["tool"] += 1

# This function checks if the player has won the game
def win_check():
    # Check if the player has upgraded to the big net and has at least 1000 money
    if(game['tool'] == 1 and game["money"] >= 1000):
        print("You Win")
        # Return True if the player has won
        return True
    # Return False if the player has not won
    return False

##############
# Game Loop #
##############

while (True):
    # Prompt the player to choose an option
    i = input("[1] Clean Pool [2] Check Stats [3] Upgrade [4] Quit")
    # Convert the input to integer
    i = int(i)
    # Execute the chosen option
    if (i == 1):
        clean_pool()
    if (i == 2):
        check_stats()
    if (i == 3):
        upgrade()
    if (i == 4):
        # Quit the game if the player chooses option 4
        print("You quit the game")
        break 
    # Check if player has won the game
    if (win_check()):
        break