import random


class Character:
    def __init__(self, name, life, energy, stamina, base_attack_pwr, initiative, attack, defence):
        self.name = name
        self.life = life
        self.energy = energy
        self.stamina = stamina
        self.base_attack_pwr = base_attack_pwr
        self.initiative = initiative
        self.attack = attack
        self.defence = defence

    def base_attack(self):
        return self.base_attack_pwr


class Mage(Character):
    def __init__(self, name='NotDefined', life=160, energy=200, stamina=0, base_attack_pwr=10, initiative=6, attack=8, defence=2):
        super().__init__(name, life, energy, stamina, base_attack_pwr, initiative, attack, defence)

    def ice_storm(self):
        if self.energy >= 50:
            self.energy -= 50
            return random.randint(5, 60)  # 5 k 12

        else:
            print('\n\33[1;31m>>> Not enough energy to cast!\33[m\n')
            return 'error'

    def fireball(self):
        if self.energy >= 30:
            self.energy -= 30
            return random.randint(5, 40)  # 5 k 8

        else:
            print('\n\33[1;31m>>> Not enough energy to cast!\33[m\n')
            return 'error'

    def lightning(self):
        if self.energy >= 20:
            self.energy -= 20
            return random.randint(5, 30)  # 5 k 6

        else:
            print('\n\33[1;31m>>> Not enough energy to cast!\33[m\n')
            return 'error'


class Knight(Character):
    def __init__(self, name='NotDefined', life=250, energy=0, stamina=150, base_attack_pwr=8, initiative=4, attack=3, defence=7):
        super().__init__(name, life, energy, stamina, base_attack_pwr, initiative, attack, defence)

    def knockdown(self):
        if self.stamina >= 50:
            self.stamina -= 50
            return random.randint(5, 40)  # 5 k 8

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform!\33[m\n')
            return 'error'

    def charge(self):
        if self.stamina >= 30:
            self.stamina -= 30
            return random.randint(5, 30)  # 5 k 6

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform!\33[m\n')
            return 'error'

    def power_attack(self):
        if self.stamina >= 20:
            self.stamina -= 20
            return random.randint(5, 20)  # 5 k 4

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform!\33[m\n')
            return 'error'


class Priest(Character):
    def __init__(self, name='NotDefined', life=200, energy=50, stamina=120, base_attack_pwr=7, initiative=5, attack=5, defence=5):
        super().__init__(name, life, energy, stamina, base_attack_pwr, initiative, attack, defence)

    def shield_thrust(self):
        if self.stamina >= 50:
            self.stamina -= 50
            return random.randint(5, 30)  # 5 k 6

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform!\33[m\n')
            return 0

    def thump(self):
        if self.stamina >= 30:
            self.stamina -= 30
            return random.randint(3, 18)  # 3 k 6

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform!\33[m\n')
            return 'error'

    def healing(self):
        if self.energy >= 50:
            self.energy -= 50
            self.life += 20
            return 1

        else:
            print('\n\33[1;31m>>> Not enough energy to cast!\33[m\n')
            return 'error'


class Rouge(Character):
    def __init__(self, name='NotDefined', life=180, energy=0, stamina=200, base_attack_pwr=10, initiative=8, attack=7, defence=3):
        super().__init__(name, life, energy, stamina, base_attack_pwr, initiative, attack, defence)

    def attack_from_behind(self):
        if self.stamina >= 50:
            self.stamina -= 50
            return random.randint(5, 50)  # 5 k 10

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform\33[m\n')
            return 'error'

    def sneaky_attack(self):
        if self.stamina >= 30:
            self.stamina -= 30
            return random.randint(4, 32)  # 4 k 8

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform\33[m\n')
            return 'error'

    def scrape(self):
        if self.stamina >= 20:
            self.stamina -= 20
            return random.randint(4, 24)  # 4 k 6

        else:
            print('\n\33[1;31m>>> Not enough stamina to perform\33[m\n')
            return 'error'