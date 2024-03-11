# Player Dictionary Representing the Players Stats
player = {
    "money": 0,
    "weapon": 0,
    "won_game": False
}

# Weapons List
weapons = [
    {"name": "teeth", "price": 0, "generates": 1},
    {"name": "rusty scissors", "price": 5, "generates": 5},
    {"name": "push lawnmower", "price": 25, "generates": 50},
    {"name": "battery lawnmower", "price": 250, "generates": 100},
    {"name": "students", "price": 500, "generates": 250},
]

# print(f'{weapons[player['weapon']]['generates']}')

def get_input():
    print(f'you are currently using {weapons[player['weapon']]['name']} and have ${player["money"]}')
    print("do you want to [a]ttack, [u]pgrade, or [q]uit")
    result = input("")

    if(result == "a"):
        attack()
        return print(f'you have ${player["money"]}')

    if(result == "u"):
        upgrade()
        return 2

    if(result == "q"):
        quit_game()
        return 3
    
    print("no valid options given")
    get_input()

def attack():
    print("you attacked")
    player['money'] = player['money'] + weapons[player['weapon']]['generates']
    win()

def upgrade():
    print("you updated")
    player["weapon"] += 1
    print(weapons[player["weapon"]])
    win()

def quit_game():
    print("game ends")

def win():
    if(player["money"] == 1000 and player["weapon"] == 4):
        print("you win!")
    get_input()

get_input()