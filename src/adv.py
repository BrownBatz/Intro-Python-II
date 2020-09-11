from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while(True):
    print(f"Currently you are in: {player.room.name}")
    print(player.room.description)
    choice = input("What would you like to do? {You can enter cardinal directions, N, S, W, E or press Q to leave the game}")

    if (choice == "q"):
        print("You have chosen to quit playing the game. See you next time!")
        break
    elif (choice == "n"):
        try:
            player.moveRoom(player.room.n_to)
        except AttributeError:
            print("You can't move N from this room, try a different direction")
    elif (choice == "e"):
        try:
            player.moveRoom(player.room.e_to)
        except AttributeError:
            print("You can't move E from this room, try a different direction")
    elif (choice == "w"):
        try:
            player.moveRoom(player.room.w_to)
        except AttributeError:
            print("You can't move W from this room, try a different direction")
    elif (choice == "s"):
        try:
            player.moveRoom(player.room.s_to)
        except AttributeError:
            print("You can't move S from this room, try a different direction")
    else:
        print("You have entered an incorrect operator, please try again.")

