#Team Members: Elijah Palmer, Maddox Swift, Adam Cammack , Zachary Worthington

import random

# ============================================================
# Maddox: Create the Move class
# ============================================================

class Move:
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        
        #Initialize instance variables
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info(self):
        # Return formatted string:
        # "<move name> (Type: <elemental type>): <low> to <high> Attack Points"
        return f'{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points'

    def generate_attack_value(self):
        # TODO: Return a random int between low_attack_points and high_attack_points (inclusive)
        return random.randint(self.low_attack_points, self.high_attack_points)


# ============================================================
# PERSON 2: Create the Pokemon class
# ============================================================

class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    def get_info(self):
        return f'{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}'

    def heal(self):
        self.hit_points += 15
        print(f'{self.name} has been healed to {self.hit_points} hit points.')


# ============================================================
# ADAM: Create Move objects, list, and loop (Part 1 logic)
# ============================================================

# TODO: Create 9 Move objects using the table below:

tackle = Move("Tackle","Normal",5,20)       
quick_attack = Move("Quick Attack","Normal",6,25)
slash = Move("Slash","Normal",10,30)
flamethrower = Move("Flamethrower","Fire",5,30)
ember = Move("Ember","Fire",10,20)
water_gun = Move("Water Gun","Water",5,15)
hydro_pump = Move("Hydro Pump","Water",20,25)
vine_whip = Move("Vine Whip","Grass",10,25)
solar_beam = Move("Solar Beam","Grass",18,27)

# TODO: Put all 9 Move objects into a list
moves_list = [tackle,quick_attack,slash,flamethrower,ember,water_gun,hydro_pump,vine_whip,solar_beam]

# TODO: Loop 3 times:

for i in range(3):
    
    #   - Randomly select a move from moves_list
    move = random.choice(moves_list)
    
    #   - Print the result of get_info() on the selected move
    print(move.get_info())
    
    #   - Print "Generated attack value: " + the result of generate_attack_value()
    print(f'Generated attack value: {move.generate_attack_value()}')
    
    #   - Delete the selected move from the list (so it can't be picked again)
    moves_list.remove(move)

input("Press enter to continue...")


# ============================================================
# PERSON 4: Create Pokemon objects and run Part 2 logic
# ============================================================

# TODO: Create 3 Pokemon objects:
bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)

print(charmander.get_info())
charmander.heal()
print(charmander.get_info())

pokemon_list = [bulbasaur, charmander, squirtle]

for pokemon in pokemon_list:
    print(pokemon.get_info())