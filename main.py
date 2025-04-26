# Copyright (C) 2025 Akrit Behera

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import ions
import elements
import compounds
import welcom
import time
import os

if __name__ == "__main__":
    welcom.final()
    while True:

        ions.clear()
        print("=======> For quiting the program use : 'q' <======== ")
        print("\nPress 1 for asking elements\nPress 2 for aksing ions\nPress 3 for aksing Formulas of Compounds\n")

        user_choice_main = input(" : ")
        if user_choice_main.lower()=="q" or "q" in user_choice_main.lower():
            os._exit(0)
        else:
            try:
                user_choice = int(user_choice_main)
            except:
                print("\n === Please Enter a Valid Input ==== ")
                time.sleep(1)
            else:
                user_choice = int(user_choice_main)
                if user_choice==1:
                    elements.run_elements()
                elif user_choice==2:
                    ions.run_ions()
                elif user_choice==3:
                    compounds.run_compounds()
                else:
                    print("\n === Please Enter a Valid Input ==== ")
                    time.sleep(1)