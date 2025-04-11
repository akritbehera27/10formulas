import random
import os , platform
from time import sleep
import welcom

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

def greeting_c():
    Body = r'''
  ____                                                  _     
 / ___|___  _   _ _ __ ___  _ __   ___  _   _ _ __   __| |___ 
| |   / _ \| | | | '_ ` _ \| '_ \ / _ \| | | | '_ \ / _` / __|
| |__| (_) | |_| | | | | | | |_) | (_) | |_| | | | | (_| \__/
 \____\___/ \__,_|_| |_| |_| .__/ \___/ \__,_|_| |_|\__,_|___/
                           |_|                                

'''
    print(Body)

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
        elif value.lower()=="q":
            os._exit(0)
        else:
            print(f"Your Answer is wrong, Correct answer is : {dictionary[key]}")

        if no_of_question_asked == 10:
            no_of_question_asked = 0
            clear()
            print("-----------------------------------------")
            print(f"Your Current score is : {score} pt")
            print("-----------------------------------------")
            sleep(1)

    clear()
    sleep(1)
    print("========================================")
    print(f"Your Final score is : {score} pt")
    print("========================================")

def run_compounds():
    clear()
    greeting_c()
    while True:
        ask_for_formulas(compounds_dict)
        sleep(1)
        print("Do You Want to REPEAT")
        print("type y/N ( default )")
        ask_to_continue = str(input(" : "))

        if ask_to_continue.upper()=="Y":
            clear()
            continue
        else:
            break

if __name__ == "__main__":
    welcom.final()
    run_compounds()