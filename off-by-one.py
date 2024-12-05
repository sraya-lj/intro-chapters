number = 5
user_input = str(input("Would you like to play? ")).lower()
if user_input == 'y':
    user_pick = int(input("Pick a number: "))
    if number == user_pick:
        print("Wow, you guess it!")
    elif abs(number - user_pick == 1):
        print("Oof! You were off by 1!")
    else:
        print("Cold! Please play again! ")
