########
#import modules
#######
#This game is called Find Chicken and you look in a house/appertment that has 5 room and you look for Chicken because he lost and my son. Chicken is in the closet so when you find him you win. You lose if it take more that 4 mintues and each room is a minute.
#global variable is time and it controls the time that makes you lose the game 
########
#define functions
#######
def start():
    print("Welcome! Your now helping look for my son Chicken but you only have 4 mintues so hurry please")
    start_screen = input("Where do you want to start searching? Chose one of these rooms:\n\tliving room\n\tkitchen\n\tcloset\n\tbathroom\n\tbedroom\n")
    if start_screen == "living room":
        living_room()
    elif start_screen == "kitchen":
        kitchen()
    elif start_screen == "closet":
        closet()
    elif start_screen == "bathroom":
        bathroom()
    elif start_screen == "bedroom":
        bedroom()
    else:
        print ("Sorry there is no room with that name try again please")
        start()

def check_time():
    global time
    time = time +1
    if time > 3:
        print ("Sorry you lost")
        exit()
    else:
        print("\n",time,"mintues down")

def living_room():
    print("\nYou are in the living room. Chicken isn't here sorry.")
    check_time()
    move = input("\nWhere do you want to go next? Chose one of these rooms:\n\tliving room\n\tkitchen\n\tcloset\n\tbathroom\n\tbedroom\n")
    if move == "living room":
        living_room()
    elif move == "kitchen":
        kitchen()
    elif move == "closet":
        closet()
    elif move == "bathroom":
        bathroom()
    elif move == "bedroom":
        bedroom()
    else:
        print ("Sorry there is no room with that name try again please")
        living_room()

def kitchen():
    print("\nYou are in the kitchen. Chicken isn't here sorry.")
    check_time()
    move = input("\nWhere do you want to go next? Chose one of these rooms:\n\tliving room\n\tkitchen\n\tcloset\n\tbathroom\n\tbedroom\n")
    if move == "living room":
        living_room()
    elif move == "kitchen":
        kitchen()
    elif move == "bathroom":
        bathroom()
    elif move == "bedroom":
        bedroom()
    else:
        print("Sorry there is no room with that name try again please")
        kitchen()

def closet():
    print("\nYou are in the closet. Chicken is here you found him. Thank You!\n\nGame Over")
    
def bathroom():
    print("\nYour in the bathroom. Chicken isn't here sorry.")
    check_time()
    move = input("\nWhere do you want to go next? Chose one of these rooms:\n\tliving room\n\tkitchen\n\tcloset\n\tbathroom\n\tbedroom\n")
    if move == "living room":
        living_room()
    elif move == "kitchen":
        kitchen()
    elif move == "bathroom":
        bathroom()
    elif move == "bedroom":
        bedroom()
    else:
        print("Sorry there is no room with that name try again please")
        bathroom()

def bedroom():
    print("\nYour in the bedroom. Chicken isn't here sorry.")
    check_time()
    move = input("\nWhere do you want to go next? Chose one of these rooms:\n\tliving room\n\tkitchen\n\tcloset\n\tbathroom\n\tbedroom\n")
    if move == "living room":
        living_room()
    elif move == "kitchen":
        kitchen()
    elif move == "bathroom":
        bathroom()
    elif move == "bedroom":
        bedroom()
    else:
        print("Sorry there is no room with that name try again please")
        bedroom()


########
#main
#######
#TODO: Add some global variables
time = 0 
start ()