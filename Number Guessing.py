import random

def play_game():
    random_number = random.randint(1, 100)
    number = int(input("Guess the number between 1 and 100: "))
    guesses = 1
    while number != random_number:
        if number < random_number:
            print('Too Low 👇 Try Again!')
        else:
            print('Too High 👆 Try Again!')
        number = int(input("Guess the number between 1 and 100: "))
        guesses += 1
    print(f'Congrats!🥳 You guessed the number in {guesses} tries.')
    print(f'The number was {random_number}.')

# Game loop
play_again = 'yes'
while play_again == 'yes':
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
