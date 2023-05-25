import random
import time
from Classes import Mage, Knight, Priest, Rouge


def initiative_roll(character):
    return character.initiative + random.randint(1, 20)


def attack_roll(character):
    return character.attack + random.randint(1, 20)


def defence_roll(character):
    return character.defence + random.randint(1, 20)


def show_character_parameters(character):
    print(f'\33[1;30;47mLife:                 {character.life}\n'
          f'Energy:               {character.energy}\n'
          f'Stamina:              {character.stamina}\n'
          f'Base attack power:    {character.base_attack_pwr} (can be used whit 0 cost)\n'
          f'Initiative:           +{character.initiative}\n'
          f'Attack:               +{character.attack}\n'
          f'Defence:              +{character.defence}\n\33[0m')


def show_attacks(character):
    if isinstance(character, Mage):
        print(f'\33[35mSpecial abilities list:\33[0m\n'
              f'Ice Storm - \33[31mDamage:\33[0m 5\33[31md\33[0m12 | \33[34mCost:\33[0m 50 energy\n'
              f'Fireball  - \33[31mDamage:\33[0m 5\33[31md\33[0m8  | \33[34mCost:\33[0m 30 energy\n'
              f'Lightning - \33[31mDamage:\33[0m 5\33[31md\33[0m6  | \33[34mCost:\33[0m 20 energy\n'
              )
    elif isinstance(character, Knight):
        print(f'\33[32mSpecial abilities list:\n\33[0m'
              f'Knockdown    - \33[31mDamage:\33[0m 5\33[31md\33[0m8  | \33[34mCost:\33[0m 50 stamina\n'
              f'Charge       - \33[31mDamage:\33[0m 5\33[31md\33[0m6  | \33[34mCost:\33[0m 30 stamina\n'
              f'Power Attack - \33[31mDamage:\33[0m 5\33[31md\33[0m4  | \33[34mCost:\33[0m 20 stamina\n'
              )
    elif isinstance(character, Priest):
        print(f'\33[36mSpecial abilities list:\n\33[0m'
              f'Shield Thrust - \33[31mDamage:\33[0m 5\33[31md\33[0m6  | \33[34mCost:\33[0m 50 stamina\n'
              f'Thump         - \33[31mDamage:\33[0m 3\33[31md\33[0m6  | \33[34mCost:\33[0m 30 stamina\n'
              f'Healing       - \33[34mHeals : 20HP\33[0m | \33[34mCost:\33[0m 50 energy\n'
              )
    elif isinstance(character, Rouge):
        print(f'\33[33mSpecial abilities list:\n\33[0m'
              f'Attack from Behind - \33[31mDamage:\33[0m 5\33[31md\33[0m10 | \33[34mCost:\33[0m 50 stamina\n'
              f'Sneaky Attack      - \33[31mDamage:\33[0m 4\33[31md\33[0m8  | \33[34mCost:\33[0m 30 stamina\n'
              f'Scrape             - \33[31mDamage:\33[0m 4\33[31md\33[0m6  | \33[34mCost:\33[0m 20 stamina\n'
              )


def show_character_parameters_oneline(character):
    print(f'L: {character.life}, E: {character.energy}, S: {character.stamina}\n'
          f'BA: {character.base_attack_pwr}, I: +{character.initiative}, A: +{character.initiative}, D: +{character.defence}\n')


def show_character_base_attributes_oneline(character):
    print(f'\33[3m{character.name}:\33[0m \33[3;31mL: {character.life}\33[0m, \33[3;34mE: {character.energy}\33[0m, '
          f'\33[3;35mS: {character.stamina}\33[0m\n')


def choose_attack(character):
    show_attacks(character)
    if isinstance(character, Mage):
        attack = input(f"Choose your attack {character.name}!\n"
                       f"(enter special ability name initials or BA to use\n"
                       f"the Base Attack)\n"
                       f"\33[1;30;42m>>>> type your choice here: \33[0m").upper()
        if attack[0] == "I":
            x = character.ice_storm()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Ice Storm!\33[0m')
                return x
        elif attack[0] == "F":
            x = character.fireball()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Fireball!\33[0m')
                return x
        elif attack[0] == "L":
            x = character.lightning()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Lightning!\33[0m')
                return x
        elif attack[0] == 'B':
            print(f'\n\33[1;30;41m{character.name} attacks with Base Attack!\33[0m')
            return character.base_attack()
        else:
            print("Wrong input!")
            return choose_attack(character)

    elif isinstance(character, Knight):
        attack = input(f"Choose your attack {character.name}!\n"
                       f"(enter special ability name initials or BA to use\n"
                       f"the Base Attack)\n"
                       f"\33[1;30;42m>>>> type your choice here: \33[0m").upper()
        if attack[0] == "K":
            x = character.knockdown()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Knock Down!\33[0m')
                return x
        elif attack[0] == "C":
            x = character.charge()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Charge!\33[0m')
                return x
        elif attack[0] == "P":
            x = character.power_attack()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Power Attack!\33[0m')
                return x
        elif attack[0] == 'B':
            print(f'\n\33[1;30;41m{character.name} attacks with Base Attack!\33[0m')
            return character.base_attack()
        else:
            print("Wrong input!")
            return choose_attack(character)

    elif isinstance(character, Priest):
        attack = input(f"Choose your attack {character.name}!\n"
                       f"(enter special ability name initials or BA to use\n"
                       f"the Base Attack)\n"
                       f"\33[1;30;42m>>>> type your choice here: \33[0m").upper()
        if attack[0] == "S":
            x = character.shield_thrust()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Shield Thrust!\33[0m')
                return x
        elif attack[0] == "T":
            x = character.thump()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Thump!\33[0m')
                return x
        elif attack[0] == "H":
            x = character.healing()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} heals him/herself with 20 HP!\33[0m')
                return x

        elif attack[0] == 'B':
            print(f'\n\33[1;30;41m{character.name} attacks with Base Attack!\33[0m')
            return character.base_attack()
        else:
            print("Wrong input!")
            return choose_attack(character)

    elif isinstance(character, Rouge):
        attack = input(f"Choose your attack {character.name}!\n"
                       f"(enter special ability name initials or BA to use\n"
                       f"the Base Attack)\n"
                       f"\33[1;30;42m>>>> type your choice here: \33[0m").upper()
        if attack[0] == "A":
            x = character.attack_from_behind()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Attack from Behind!\33[0m')
                return x
        elif attack[0:1] == "SN":
            x = character.sneaky_attack()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Sneaky Attack!\33[0m')
                return x
        elif attack[0:1] == "SC":
            x = character.scrape()
            if x == 'error':
                return 0
            else:
                print(f'\n\33[1;30;41m{character.name} attacks with Scrape!\33[0m')
                return x
        elif attack[0] == 'B':
            print(f'\n\33[1;30;41m{character.name} attacks with Base Attack!\33[0m')
            return character.base_attack()
        else:
            print("Wrong input!")
            return choose_attack(character)


def choose_character(player_name):
    player = input(f"\33[1;30;42m>>> {player_name}, choose your class:\33[0m ").upper().strip()
    if player[0] == 'M':
        print(f">>> {player_name}, your choice is Mage!\n")
        return 'M'
    elif player[0] == 'K':
        print(f">>> {player_name}, your choice is Knight!\n")
        return 'K'
    elif player[0] == 'P':
        print(f">>> {player_name}, your choice is Priest!\n")
        return 'P'
    elif player[0] == 'R':
        print(f">>> {player_name}, your choice is Rouge!\n")
        return 'R'
    else:
        print("Wrong input!")
        return choose_character(player_name)


def player_action(player, opponent):
    while True:
        print(f"What would you like to do?\n"
              f"1. See your current attributes\n"
              f"2. See your opponent's attributes\n"
              f"3. Attack")
        action = input(f"\33[1;30;42m>>>Input the number respective to your action: \33[0m").strip()
        if action == '':
            player_action(player, opponent)
        elif action == '1':
            print("Your attributes:")
            show_character_base_attributes_oneline(player)
        elif action == '2':
            print("Your opponent's attributes:")
            show_character_base_attributes_oneline(opponent)
        elif action == '3':
            break

        else:
            print("Wrong input!")
            player_action(player, opponent)


def attacking(player, opponent):
    print("\n" + "-" * 17 + f" {player.name} attacks! " + "-" * 17)
    player_action(player, opponent)
    x = choose_attack(player)
    while x == 0:
        x = choose_attack(player)
    time.sleep(.5)
    if x > 1:
        player_attack_roll = attack_roll(player)
        opponent_defence_roll = defence_roll(opponent)
        print(f"\n{player.name}'s attack roll: {player_attack_roll}")
        print(f"{opponent.name}'s defence roll: {opponent_defence_roll}")
        time.sleep(.5)
        if player_attack_roll >= opponent_defence_roll:
            print(f"\n\33[1;30;41m{player.name} deals {x} damage to {opponent.name}\33[0m")
            opponent.life -= x
        else:
            print(f"\n\33[1;30;44m{opponent.name} parries the attack!\33[0m")
            pass
    elif x == 1:
        pass


def regeneration(player):
    if isinstance(player, Mage):
        player.energy += 10
        print(f'{player.name} regenerates 10 energy!')

    elif isinstance(player, Knight) or isinstance(player, Rouge):
        player.stamina += 10
        print(f'{player.name} regenerates 10 stamina!')

    elif isinstance(player, Priest):
        player.stamina += 10
        player.energy += 10
        print(f'{player.name} regenerates 10 energy & stamina!')


def print_rules():
    print(f"1. Players choose their character from four\n"
          f"   available classes: Mage, Knight, Priest & Rogue\n\n"
          f"2. Each class has different attributes, bonuses and\n"
          f"   unique special abilities\n\n"
          f"3. Using special ability consumes attributes. Stamina\n"
          f"   and energy attributes restores by 10 in the end of\n"
          f"   each round. Life does note restore (only Priest's\n"
          f"   special ability 'healing' can restore Life.\n\n"
          f"4. Bonuses are values that add up to respective\n"
          f"   roll. e.g. +6 Initiative bonus adds 6 to the\n"
          f"   Player's initiative roll (from 1 - 20) in the\n"
          f"   beginning of each round.\n\n"
          f"5. Special abilities has values representing their\n"
          f"   final value as a result of dices roll:\n"
          f"   e.g. 5d8 means that Players rolls 5 dices with\n"
          f"   8 walls each. The final value of the special\n"
          f"   ability will be in range from 5 (5x1) to 40 (5x8)\n\n"
          f"5. In the beginning of each round Players roll for\n"
          f"   Initiative - the result will be roll of 1d20\n"
          f"   increased by the Player's Initiative bonus.\n"
          f"   Player with higher Initiative will start!\n\n"
          f"6. Player can choose his/her actions from:\n"
          f"   - viewing his/her own stats,\n"
          f"   - viewing his/her opponent's stats,\n"
          f"   - attacking\n\n"
          f"   After selecting an attack - either from special\n"
          f"   abilities consuming the attributes or a Base\n"
          f"   Attack that deals specific amount of damage and\n"
          f"   consumes no attributes.\n\n"
          f"7. Attacking Player rolls for Attack (1d20 +\n"
          f"   Attack Bonus) and defending Player rolls for\n"
          f"   Defence (1d20 + Defence Bonus. If attacking\n"
          f"   Player's roll is higher than defending player's\n"
          f"   roll, the attack is effective and deals damage,\n"
          f"   otherwise the attack is parried and deals no\n"
          f"   damage. Than the roles swap.\n\n"
          f"8. Players fight against each other till one's life\n"
          f"   reaches 0. The one who's alive wins!\n")
