# Daniel Collins

def show_instructions():
    print('Jedi Knight Adventure Game')
    print('Collect 5 items and save Senator Padme to win the game, or be destroyed by Tyrannus.')
    print('Move commands: go South, go North, go East, go West')
    print('Add to Inventory: get "item name"\n')


def main():
    show_instructions()
    rooms = {'Great Hall': {'South': 'Sand Room', 'North': 'Private Study', 'West': 'Atrium',
                            'East': 'Kitchen', 'item': None},
             'Sand Room': {'North': 'Great Hall', 'East': 'Dungeon', 'item': 'Keys'},
             'Dungeon': {'West': 'Sand Room', 'item': 'Darth Tyrannus'},
             'Secret Room': {'South': 'Kitchen', 'item': 'Ancient Texts'},
             'Private Study': {'East': 'Master Bedroom', 'South': 'Great Hall', 'item': 'Map'},
             'Atrium': {'East': 'Great Hall', 'item': 'Lightsaber'},
             'Master Bedroom': {'West': 'Private Study', 'item': 'Healing Potion'},
             'Kitchen': {'West': 'Great Hall', 'North': 'Secret Room', 'item': None}
             }

    current_room = 'Great Hall'
    inventory = []

    while True:
        if current_room == 'Dungeon':
            print("\nYou're in the", current_room)
            print("You see Darth Tyrannus!")
            if len(inventory) == 5:
                print("\nYou have defeated Darth Tyrannus and rescued Senator Padme!")
                print("Looks like Sith Lords are your specialty.")
            else:
                print("\nIt's over Anakin, I have the high ground...GAME OVER!")
                print("Looks like Sith Lords are not your specialty.")
            break

        print("\nYou're in the ", current_room)

        if rooms[current_room]['item'] is not None:
            print("You see a", rooms[current_room]['item'])
            ask_item = input("get " + rooms[current_room]['item'] + "? (Y/N): ").upper()
            while ask_item not in ['Y', 'N']:
                print("Invalid input, please try again")
                ask_item = input("Get " + rooms[current_room]['item'] + "? (Y/N): ").upper()
            if ask_item == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            print("Hmm already collected item or nothing in this room")

        print("Inventory: ", inventory)

        direction = input("Which direction to move? (East,West,North,South): ").title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        while direction not in directions:
            print("Invalid input direction from " + current_room + ". Try again")
            direction = input("Which direction to move?(East,West,North,South): ").title()

        next_room = rooms[current_room][direction]
        print("You have just moved to", next_room)
        print("----------------------------------------")

        current_room = next_room

    print("\nThanks for playing; try again if your dare.")


main()
