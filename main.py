import ions
import elements

if __name__ == "__main__":
    print("\nPress 1 for asking elements ( Deafult )\nPress 2 for aksing ions\n")
    try:
        user_choice = int(input(" : "))
        
        if user_choice==1:
            elements.run_elements()
        elif user_choice==2:
            ions.run_ions()
        else:
            print("Please Enter a Valid Input")
    except:
        print("Please Enter a Valid Input")