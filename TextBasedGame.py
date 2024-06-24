# Tashyra Adams

def show_instructions():
    print("Adventure Game")
    print("Collect all items to win the game, or be caught by the villain.")
    print("Move commands: go North, go South, go East, go West")
    print("Get item: get [item name]")


def show_status(current_room, inventory, current_item, available_directions):
    print(f"You are in the {current_room}")
    print(f"Inventory: {', '.join(inventory)}")
    if current_item:
        print(f"You see a {current_item}")
    print(f"Available directions: {', '.join(available_directions)}")
    print("----------------------")


def get_new_state(direction, current_room, rooms, inventory):
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        current_item = rooms[new_room].get('item', None)

        if current_item:
            print(f"You found a {current_item} in the {new_room}!")

        return new_room, current_item
    else:
        print("Invalid direction. Try again.")
        return current_room, None


def initialize_game():
    # Initialize the game world
    rooms = {
        'Living Room': {'East': 'Kitchen', 'South': 'Bedroom', 'item': 'Book'},
        'Kitchen': {'West': 'Living Room', 'item': 'Knife'},
        'Bedroom': {'North': 'Living Room', 'item': 'Pillow', 'South': 'Basement'},
        'Basement': {'South': 'Bedroom', 'item': 'Flashlight'}
    }

    items_to_collect = {'Book', 'Knife', 'Pillow', 'Flashlight'}

    return rooms, items_to_collect


def main():
    rooms, items_to_collect = initialize_game()
    inventory = []
    current_room = 'Living Room'
    villain_room = 'Basement'

    show_instructions()

    while True:
        current_item = rooms[current_room].get('item', None)
        available_directions = list(rooms[current_room].keys() - {'item'})

        show_status(current_room, inventory, current_item, available_directions)

        # Player input
        move = input("Enter your move: ").lower().split()

        if len(move) == 2:
            action, direction = move
            if action == 'go':
                current_room, item_found = get_new_state(direction.capitalize(), current_room, rooms, inventory)
                if current_room == villain_room:
                    print("NOM NOM...GAME OVER!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break
                elif item_found:
                    inventory.append(item_found)
                    print(f"You obtained {item_found}.")
            elif action == 'get':
                item_name = direction.capitalize()
                if item_name in rooms[current_room] and item_name == rooms[current_room]['item']:
                    item = rooms[current_room].pop('item')
                    inventory.append(item)
                    if set(inventory) == items_to_collect:
                        print("Congratulations! You have collected all items and defeated the villain!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        break
                    print(f"You obtained {item}.")
                else:
                    print("That item is not in this room. Try again.")
            else:
                print("Invalid command. Try again.")
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
