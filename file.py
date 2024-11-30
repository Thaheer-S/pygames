print("Select a game to play:")
print("1. Snake Game")
print("2. Car Race Game")
print("3. Tic Tac Toe Game")

choice = input("Enter your choice (1 or 2 or 3): ")

if choice == "1":
    import snake_game

elif choice == "2":
    import car_game

elif choice == '3':
    import tic_tac_toe

else:

    print("Invalid choice. Please enter 1 or 2 or 3.")
