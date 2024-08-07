import random
import os , platform
from time import sleep

compounds_dict = {
"Sulphuric Acid" : "H2SO4",
"Hydrocloric Acid": "HCL",
"Nitric Acid": "HNO3",
"Acetic Acid":"CH3COOH",
"Formic Acid":"HCOOH",
"Qucik Lime":"CaO",
"Slaked Lime":"Ca(OH)2",
"Lime Stone Is made of":"CaCO3"
}

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def ask_for_formulas(dictionary):
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

def run_compounds():
    clear()
    while True:
        ask_for_formulas(compounds_dict)
        sleep(1)
        print("Do You Want to REPEAT:")
        ask_to_continue = str(input("type y/N : "))

        if ask_to_continue.upper()=="N":
            break
        else:
            clear()
            continue

if __name__ == "__main__":
    run_compounds()