import random
import os, platform

# Dictionary containing information about the first 18 elements of the periodic table
elements = {
    1: {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "electronic_config": "1", "valency": 1},
    2: {"name": "Helium", "symbol": "He", "atomic_number": 2, "electronic_config": "2", "valency": 0},
    3: {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "electronic_config": "2 1", "valency": 1},
    4: {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "electronic_config": "2 2", "valency": 2},
    5: {"name": "Boron", "symbol": "B", "atomic_number": 5, "electronic_config": "2 3", "valency": 3},
    6: {"name": "Carbon", "symbol": "C", "atomic_number": 6, "electronic_config": "2 4", "valency": 4},
    7: {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "electronic_config": "2 5", "valency": 3},
    8: {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "electronic_config": "2 6", "valency": 2},
    9: {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "electronic_config": "2 7", "valency": 1},
    10: {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "electronic_config": "2 8", "valency": 0},
    11: {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "electronic_config": "2 8 1", "valency": 1},
    12: {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "electronic_config": "2 8 2", "valency": 2},
    13: {"name": "Aluminium", "symbol": "Al", "atomic_number": 13, "electronic_config": "2 8 3", "valency": 3},
    14: {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "electronic_config": "2 8 4", "valency": 4},
    15: {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "electronic_config": "2 8 5", "valency": 3},
    16: {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "electronic_config": "2 8 6", "valency": 2},
    17: {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "electronic_config": "2 8 7", "valency": 1},
    18: {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "electronic_config": "2 8 8", "valency": 0},
    19: {"name": "Potassium", "symbol": "K", "atomic_number": 19,},
    20: {"name": "Calcium", "symbol": "Ca", "atomic_number": 20,},
    21: {"name": "Scandium", "symbol": "Sc", "atomic_number": 21,},
    22: {"name": "Titanium", "symbol": "Ti", "atomic_number": 22,},
    23: {"name": "Vanadium", "symbol": "V", "atomic_number": 23,},
    24: {"name": "Chromium", "symbol": "Cr", "atomic_number": 24,},
    25: {"name": "Manganese", "symbol": "Mn", "atomic_number": 25,},
    26: {"name": "Iron", "symbol": "Fe", "atomic_number": 26,},
    27: {"name": "Cobalt", "symbol": "Co", "atomic_number": 27,},
    28: {"name": "Nickel", "symbol": "Ni", "atomic_number": 28,},
    29: {"name": "Copper", "symbol": "Cu", "atomic_number": 29},
    30: {"name": "Zinc", "symbol": "Zn", "atomic_number": 30,}
}

poi=6
def ask_question():
    global poi
    # Randomly select an element from the first 18 elements
    element_number = random.randint(1, 30)
    element = elements[element_number]
    
    # Ask questions about the element
    print(f"\nWhat is the symbol of the element with atomic number {element['atomic_number']}?")
    symbol_answer = input("Symbol: ")

    if symbol_answer.lower() != element['symbol'].lower():
        print(f"Wrong! The correct symbol is '{element['symbol']}'")
        poi-=2
    else:
        poi+=5
    
    #other set
    element_number = random.randint(1, 30)
    element = elements[element_number]

    print(f"\nWhat is the atomic number of the element with name '{element['name']}'?")
    atomic_number_answer = input("Atomic Number: ")

    if atomic_number_answer != str(element['atomic_number']):
        print(f"Wrong! The correct atomic number is {element['atomic_number']}")
        poi-=2
    else:
        poi+=5

def ask_electronic_configuration():
    global poi
    # Randomly select an element from the first 18 elements
    element_number = random.randint(1, 18)
    element = elements[element_number]
    
    # Ask for the electronic configuration of the element
    print(f"\nElectronic configuration of '{element['name']}'")
    config_answer = input("Electronic Configuration: ")
    
    # Check answer
    if config_answer != element['electronic_config']:
        print(f"Wrong! The correct electronic configuration is '{element['electronic_config']}'")
        poi-=2
    else:
        poi+=5

def ask_valency():
    global poi
    # Randomly select an element from the first 30 elements
    element_number = random.randint(1, 18)
    element = elements[element_number]
    
    # Ask for the valency of the element
    print(f"\nWhat is the valency of '{element['symbol']}'?")
    try:
        valency_answer = int(input("Valency: "))
    except:
        valency_answer = 0
    
    # Check answer
    if valency_answer != element['valency']:      
        print(f"Wrong! The correct valency is '{element['valency']}'")
        poi-=2
    else:
        poi+=5

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


print("Deafult will (no input) will run it on infinite loop")
try:
    no_of_sets=int(input("Please Specify the no of Sets : "))
except:
    no_of_sets=0
    
if no_of_sets>0:
    for nset in range(0,no_of_sets):
        clear()
        print(f"Hear Is your {nset+1} Set:")
        ask_question()   
        ask_electronic_configuration()
        ask_valency()
    clear()
    print(f"\nHear is Your Final Score :: {poi}")

else:
    while True:
        ask_question()   
        ask_electronic_configuration()
        ask_valency()

        clear()
        print(f"\nHear is Your Current Score :: {poi}")