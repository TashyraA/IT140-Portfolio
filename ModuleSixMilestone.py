# Tashyra Adams

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

def display_room(current_room):
    """Displays the current room to the player."""
    print(f'You are in the {current_room}.')

def move_player(current_room, direction):
    """Moves the player to the new room based on the direction."""
    new_room = rooms[current_room].get(direction)
    if new_room:
        return new_room
    else:
        print("Invalid direction. Try again.")
        return current_room

def main():
    # Initial room
    current_room = 'Great Hall'

    while current_room != 'exit':
        # Display current room
        display_room(current_room)

        # Get player input
        command = input('Enter a command (e.g., "go North", "exit"): ')
        command_parts = command.split()

        if len(command_parts) == 2 and command_parts[0] == 'go':
            # Handle move command
            direction = command_parts[1]
            current_room = move_player(current_room, direction)
        elif command == 'exit':
            # End the game
            current_room = 'exit'
        else:
            # Invalid command
            print("Invalid command. Try again.")

    print('Thanks for playing!')

if __name__ == "__main__":
    main()
