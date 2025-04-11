import random
import os, platform

# Dictionary containing information about the first 18 elements of the periodic table
def greeting_e():
    Body = r'''
 _____ _                           _       
| ____| | ___ _ __ ___   ___ _ __ | |_ ___ 
|  _| | |/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
| |___| |  __/ | | | | |  __/ | | | |_\__ /
|_____|_|\___|_| |_| |_|\___|_| |_|\__|___/

'''
    print(Body)

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

points=6
def ask_question():
    global points
    # Randomly select an element from the first 18 elements
    element_number = random.randint(1, 30)
    element = elements[element_number]
    
    # Ask questions about the element
    print(f"\nWhat is the symbol of the element with atomic number {element['atomic_number']}?")
    symbol_answer = input("Symbol: ")

    if symbol_answer.replace(" ", "").lower()=="q":
            os._exit(0)
    if symbol_answer.lower() != element['symbol'].lower():
        print(f"Wrong! The correct symbol is '{element['symbol']}'")
        points-=2
    else:
        points+=5
    
    #other set
    element_number = random.randint(1, 30)
    element = elements[element_number]

    print(f"\nWhat is the atomic number of the element with name '{element['name']}'?")
    atomic_number_answer = input("Atomic Number: ")

    if atomic_number_answer.replace(" ", "").lower()=="q":
            os._exit(0)
    if atomic_number_answer.replace(" ", "") != str(element['atomic_number']):
        print(f"Wrong! The correct atomic number is {element['atomic_number']}")
        points-=2
    else:
        points+=5

def extract_numbers(input_string):
    return ''.join(char for char in input_string if char.isdigit())

def ask_electronic_configuration():
    global points
    # Randomly select an element from the first 18 elements
    element_number = random.randint(1, 18)
    element = elements[element_number]
    
    # Ask for the electronic configuration of the element
    print(f"\nElectronic configuration of '{element['name']}'")
    config_answer = input("Electronic Configuration: ")
    
    # Check answer
    if config_answer.replace(" ", "").lower()=="q":
        os._exit(0)
    if extract_numbers(config_answer) != extract_numbers(element['electronic_config']):
        print(f"Wrong! The correct electronic configuration is '{element['electronic_config']}'")
        points-=2
    else:
        points+=5

def ask_valency():
    global points
    # Randomly select an element from the first 30 elements
    element_number = random.randint(1, 18)
    element = elements[element_number]
    
    # Ask for the valency of the element
    print(f"\nWhat is the valency of '{element['symbol']}'?")
    vinput=input("Valency: ")
    if vinput.replace(" ", "").lower()=="q":
        os._exit(0)
    else:
        try:
            valency_answer = int(vinput)
        except:
            valency_answer = 0
        else:
            # Check answer
            valency_answer = int(vinput)
            if valency_answer != element['valency']:      
                print(f"Wrong! The correct valency is '{element['valency']}'")
                points-=2
            else:
                points+=5

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


def run_elements():
    clear()
    greeting_e()
    print("Deafult will (no input or any other ) will run it on infinite loop")
    no_of_sets_main=input("Please Specify the no of Sets : ")

    if no_of_sets_main.lower()=="q" or "q" in no_of_sets_main.lower():
            os._exit(0)
    else:
        try:
            no_of_sets=int(no_of_sets_main)
        except:
            no_of_sets=0
        
    if no_of_sets>0:
        no_of_sets=int(no_of_sets_main)
        for nset in range(0,no_of_sets):
            clear()
            print(f"Hear Is your {nset+1} Set:")
            ask_question()   
            ask_electronic_configuration()
            ask_valency()
        clear()
        print("========================================")
        print(f"Your Final score is : {points} pt")
        print("========================================")

    else:
        while True:
            ask_question()   
            ask_electronic_configuration()
            ask_valency()

            clear()
            print("-----------------------------------------")
            print(f"Your Current score is : {points} pt")
            print("-----------------------------------------")

if __name__ == "__main__":
    run_elements()