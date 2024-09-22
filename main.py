import ions
import elements
import compounds
import welcom
import time

if __name__ == "__main__":
    welcom.final()
    time.sleep(2)

    while True:
        ions.clear()

        print("For quiting the program any time use : 'CTRL + C' ")
        print("\nPress 1 for asking elements ( Deafult )\nPress 2 for aksing ions\nPress 3 for aksing Formulas of Compounds\nPress 'Q' for quiting the program\n")
        
        try:
            user_choice = input(" : ")
        except:
            user_choice = str(user_choice)
        else:
            if user_choice=="1":
                elements.run_elements()
            elif user_choice=="2":
                ions.run_ions()

            elif user_choice=="3":
                compounds.run_compounds()

            elif user_choice.upper()=="Q":
                break
            
            else :
                continue
            