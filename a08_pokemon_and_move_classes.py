#Team Members: Elijah Palmer, Maddox Swift, [Name 3], [Name 4]

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
        return f'{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points}'

    def generate_attack_value(self):
        # TODO: Return a random int between low_attack_points and high_attack_points (inclusive)
        return random.randint(self.low_attack_points, self.high_attack_points)


# ============================================================
# PERSON 2: Create the Pokemon class
# ============================================================

class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        # TODO: Initialize instance variables
        pass

    def get_info(self):
        # TODO: Return formatted string:
        # "<name> - Type: <elemental_type> - Hit Points: <hit_points>"
        pass

    def heal(self):
        # TODO: Add 15 to hit_points, then print:
        # "<name> has been healed to <hit_points> hit points."
        # Do NOT return anything
        pass


# ============================================================
# ADAM: Create Move objects, list, and loop (Part 1 logic)
# ============================================================

# TODO: Create 9 Move objects using the table below:

tackle = Move("Tackle","Normal",5,20)       
quick_attack = Move("Quick attack","Normal",6,25)
slash = Move("Slash","Normal",10,30)
flamethrower = Move("Flamethrower","Fire",5,30)
ember = Move("Ember","Fire",10,20)
water_gun = Move("Water Gun","Water",5,15)
hydro_pump = Move("Hydro Pump","Water",20,25)
vine_whip = Move("Vine Whip","Grass",10,15)
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
# Name       | Type  | Hit Points
# Bulbasaur  | Grass | 60
# Charmander | Fire  | 55
# Squirtle   | Water | 65

bulbasaur = None      # Replace None with Pokemon(...)
charmander = None
squirtle = None

# TODO: Print get_info() for Charmander
# TODO: Call heal() on Charmander
# TODO: Print get_info() for Charmander again (hit points should be higher)

# TODO: Put the 3 Pokemon objects in a list
pokemon_list = []

# TODO: Loop through pokemon_list and print get_info() for each one