def check():
    import random
    user_name = input("What is your name? ")
    print("Welcome " + user_name)

    game_still = True
    user_points = 0
    computer_points = 0
    
    while game_still:
        user_choice = input("What is your choice? 'rock' , 'paper' , 'scissors': ")
        print(f" You choose {user_choice}.")

        shapes = ["rock","paper","scissors"]

        computer_choice = random.choice(shapes)
        print(f" Computer choose {computer_choice}.")
        

        if user_choice == computer_choice:
            print("Draw!")
        elif user_choice == 'paper' and computer_choice == 'rock':
            user_points += 1
            print(f"    {user_name}'s points: {user_points}")
        elif user_choice == 'rock' and computer_choice == 'paper':
            computer_points += 1
            print(f"    Computer's points: {computer_points}")
        elif user_choice == 'scissors' and computer_choice == 'paper':
            user_points += 1
            print(f"    {user_name}'s points: {user_points}")
        elif computer_choice == 'scissors' and user_choice == 'paper':
            computer_points += 1
            print(f"    Computer's points: {computer_points}")
        elif computer_choice == 'rock' and user_choice == 'paper':
            user_points += 1
            print(f"    {user_name}'s points: {user_points}")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            user_points += 1
            print(f"    {user_name}'s points: {user_points}")
        else:
            computer_points += 1
            print(f"    Computer's points: {computer_points}")
        
        print(f"{user_points} / {computer_points}")

        if user_points >= 5 or computer_points >= 5:
            game_still = False

            while input("Do you want to start it again or not Type 'yes' or 'no': ").lower() == 'yes':
                check()

check()    