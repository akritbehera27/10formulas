import random
import os , platform
from time import sleep

ions_dict = {
"Sodium" : "Na+",
"Potassium" : "K+",
"Silver" : "Ag+",
"Copper (I)" : "Cu+",
"Magnesium" : "Mg2+",
"Calcium" : "Ca2+",
"Zinc" : "Zn2+",
"Iron (II)" : "Fe2+",
"Copper (II)" : "Cu2+",
"Aluminium" : "Al3+",
"Iron (III)" : "Fe3+",
"Hydrogen" : "H+",
"Hydride" : "H-",
"Chloride" : "Cl-",
"Bromide" : "Br-",
"Iodide" : "I-",
"Oxide" : "O2-",
"Sulphide" : "S2-",
"Nitride" : "N3-",
"Ammonium" : "NH4+",
"Hydroxide" : "OH-",
"Nitrate" : "NO3-",
"Hydrogen carbonate" : "HCO3-",
"Carbonate" : "CO3 2-",
"Sulphite" : "SO3 2-",
"Sulphate" : "SO4 2-",
"Phosphate" : "PO4 3-"
}

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def ask_for_values(dictionary):
    score = 0
    keys = list(dictionary.keys())
    random.shuffle(keys)
    
    no_of_question_asked=0
    for key in keys:
        value = str(input(f"Enter a formula for '{key}': "))
        no_of_question_asked += 1

        if value.replace(" ", "").upper()==dictionary[key].replace(" ", "").upper():
            score += 1
        else:
            print(f"Your Answer is wrong, Correct answer is : {dictionary[key]}")

        if no_of_question_asked == 10:
            no_of_question_asked = 0
            clear()
            print("-----------------------------------------")
            print(f"Your Current score is : {score} pints")
            print("-----------------------------------------")
            sleep(1)

    clear()
    sleep(1)
    print("========================================")
    print(f"Your Final score is : {score} pints")
    print("========================================")
# Example usage:
if __name__ == "__main__":
    print()
    while True:
        ask_for_values(ions_dict)
        sleep(1)
        print("Do You Want to REPEAT the questions:")
        ask_to_continue = str(input("type y/N : "))

        if ask_to_continue.upper()=="N":
            break
        else:
            clear()
            continue