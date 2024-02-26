import random

print("*** Welcome to Rock, Paper, Scissor Game *** \n")

player_name = input("Enter your name: ").title()
print("Hello " + player_name + ", let's start the game")

user_wins = 0
computer_wins = 0

while True:
    print()

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    print(f"Current Score: {user_wins}||{computer_wins}")

    user_choice = int(input("What go you choose? "
                            "\nType 0 for Rock, 1 for Paper or 2 for Scissors or 3 for quit: "))

    computer_choice = random.randint(0, 2)

    answers = [rock, paper, scissors]

    if user_choice == 3:
        print(f"""
              Your Score: {user_wins} || {computer_wins}: Computer Score
              """)
        if user_wins == 0 and computer_wins == 0:
            print("Game stop with no score")
        elif user_wins > computer_wins:
            print(f"You Win! with {user_wins - computer_wins} scores.")
        else:
            print(f"Computer wins {computer_wins - user_wins} scores.")
        break

    if user_choice == computer_choice:
        print(f"""
              You: {answers[0]}
              Computer: {answers[0]}
              Draw the game!
              """)

    elif user_choice == 0 and computer_choice == 2:
        user_wins += 1
        print(f"""
              You: {answers[0]}
              Computer: {answers[2]}
              You wing buddy!
              """)

    elif computer_choice == 0 and user_choice == 2:
        computer_wins += 1
        print(f"""
              Computer: {answers[0]}
              You: {answers[2]}
              Computer win!!
              """)

    elif user_choice == 1 and computer_choice == 0:
        user_wins += 1
        print(f"""
              You: {answers[1]}
              Computer: {answers[0]}
              You win!!
              """)

    elif computer_choice == 1 and user_choice == 0:
        computer_wins += 1
        print(f"""
              Computer: {answers[1]}
              You: {answers[0]}
              Computer win!!
              """)

    elif user_choice == 2 and computer_choice == 1:
        user_wins += 1
        print(f"""
              You: {answers[2]}
              Computer: {answers[1]}
              You win!!
              """)

    elif computer_choice == 2 and user_choice == 1:
        computer_wins += 1
        print(f"""
              Computer: {answers[2]}
              You: {answers[1]}
              Computer win!!
              """)

print(f"See you again {player_name}!")



