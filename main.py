import Fun
import time
from Classes import Mage, Knight, Priest, Rouge

print(">" * 20 + " Game rules " + "<" * 20)
Fun.print_rules()
print(">" * 16 + " Choose your Class! " + "<" * 16)
print("\33[35m-\33[0m" * 23 + " \33[35mMage\33[0m " + "\33[35m-\33[0m" * 23)
Fun.show_character_parameters(Mage())
Fun.show_attacks(Mage())
print("\33[32m-\33[0m" * 22 + "\33[32m Knight \33[0m" + "\33[32m-\33[0m" * 22)
Fun.show_character_parameters(Knight())
Fun.show_attacks(Knight())
print("\33[36m-\33[0m" * 22 + "\33[36m Priest \33[0m" + "\33[36m-\33[0m" * 22)
Fun.show_character_parameters(Priest())
Fun.show_attacks(Priest())
print("\33[33m-\33[0m" * 23 + "\33[33m Rogue \33[0m" + "\33[33m-\33[0m" * 22)
Fun.show_character_parameters(Rouge())
Fun.show_attacks(Rouge())

Player1_name = input("\33[1;30;42m>>>> Player 1 - enter your name: \33[0m").title()
Player1 = Fun.choose_character(Player1_name)
if Player1 == 'M':
    Player1 = Mage(Player1_name)
elif Player1 == 'K':
    Player1 = Knight(Player1_name)
elif Player1 == 'P':
    Player1 = Priest(Player1_name)
elif Player1 == 'R':
    Player1 = Rouge(Player1_name)

Player2_name = input("\33[1;30;42m>>>> Player 2 - enter your name: \33[0m").title()
Player2 = Fun.choose_character(Player2_name)
if Player2 == 'M':
    Player2 = Mage(Player2_name)
elif Player2 == 'K':
    Player2 = Knight(Player2_name)
elif Player2 == 'P':
    Player2 = Priest(Player2_name)
elif Player2 == 'R':
    Player2 = Rouge(Player2_name)

round_count = 1
print(">" * 13 + " Let may the fight begin! " + "<" * 13 + "\n")
while True:
# for i in range(3):
    if round_count < 10:
        print("=" * 21 + f" Round 0{round_count} " + "=" * 21 + "\n")
    else:
        print("=" * 21 + f" Round {round_count} " + "=" * 21 + "\n")
    Player1_initiative_roll = Fun.initiative_roll(Player1)
    Player2_initiative_roll = Fun.initiative_roll(Player2)
    print(f"{Player1.name}'s initiative: {Player1_initiative_roll}")
    print(f"{Player2.name}'s initiative: {Player2_initiative_roll}")
    time.sleep(.5)
    if Player1_initiative_roll > Player2_initiative_roll:
        Fun.attacking(Player1, Player2)
        if Player2.life < 0:
            break
        Fun.attacking(Player2, Player1)
        if Player1.life < 0:
            break
    elif Player2_initiative_roll > Player1_initiative_roll:
        Fun.attacking(Player2, Player1)
        if Player1.life < 0:
            break
        Fun.attacking(Player1, Player2)
        if Player2.life < 0:
            break
    else:
        if Player1.initiative > Player2.initiative:
            Fun.attacking(Player1, Player2)
            if Player2.life < 0:
                break
            Fun.attacking(Player2, Player1)
            if Player1.life < 0:
                break
        else:
            Fun.attacking(Player2, Player1)
            if Player1.life < 0:
                break
            Fun.attacking(Player1, Player2)
            if Player2.life < 0:
                break

    Fun.regeneration(Player1)
    Fun.regeneration(Player2)
    print("\n" + "-" * 11 + "End of round stats players': " + "-" * 11 + "\n")
    Fun.show_character_base_attributes_oneline(Player1)
    Fun.show_character_base_attributes_oneline(Player2)
    round_count += 1


if Player1.life > 0 >= Player2.life:
    print("\n" + ">" * 18 + f" {Player1.name} wins! " + 18 * "<")
else:
    print("\n" + ">" * 18 + f" {Player2.name} wins! " + 18 * "<")