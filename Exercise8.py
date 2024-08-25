import random

sissors = 0
rock = 1
papper = 2
player_count = 0
computer_count = 0

rad = [sissors, rock, papper]

for i in range(2):
    randomm = random.choice(rad)
    player_entery = input(" Choose rock(1) papper(2) or sissors(0):")
    entery = int(player_entery)
    print(f" Computer choice: {randomm}")
    print(f" Player choice: {entery}\n")
    if 0 <= randomm <= 2 and 0 <= entery <= 2:
        if randomm == sissors and entery == papper\
           or randomm == papper and entery == rock \
           or randomm == rock and entery == sissors:
            computer_count += 1
            print(f"player score: {player_count}")
            print(f"Computer score: {computer_count}\n")
            print("Computer wins this round 💻\n")
        elif  entery == sissors and randomm == papper\
           or entery == papper and randomm == rock \
           or entery == rock and randomm == sissors:
            player_count += 1
            print(f"player score: {player_count}")
            print(f"Computer score: {computer_count}\n")
            print("Player wins this round 😎\n")
        else:
            print("A tie 💪")
            print(f"player score: {player_count}")
            print(f"computer score: {computer_count}\n")
    else:
        print("Number must be from 0-2")
print(f"player Total score: {player_count}")
print(f"Computer Total score: {computer_count}\n")
if player_count > computer_count:
    print("Player wins overall")
elif player_count < computer_count:
    print("Computer wins overall")
else:
    print("Tie in both rounds, Play again")
