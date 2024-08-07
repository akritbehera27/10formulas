import ions
import elements
import compounds

if __name__ == "__main__":
    print("\nPress 1 for asking elements ( Deafult )\nPress 2 for aksing ions\nPress 3 for aksing Formulas of Compounds\n")
    try:
        user_choice = int(input(" : "))
        
        if user_choice==1:
            elements.run_elements()
        elif user_choice==2:
            ions.run_ions()

        elif user_choice==3:
            compounds.run_compounds()
        else:
            print("Please Enter a Valid Input")
    except:
        print("Please Choose A Branch")