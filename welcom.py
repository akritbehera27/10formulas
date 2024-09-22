import os

columns, rows = os.get_terminal_size()
def mark_adder(Text):
    
    if Text != " ":
        place = ((columns - len(Text))//2)-2
        Test_text = "##"+" "*place + Text
        Final_text = Test_text + ((columns - len(Test_text))-2)*" " + "##"
    else:
        Final_text = "##" + (columns - 4)*" " + "##"
    
    return Final_text

def tb(val):
    border = "#"
    tb_border = border*columns*2

    if val==0:
        print(tb_border + mark_adder(" ") + mark_adder(" "))
    else:
        print(mark_adder(" ") + mark_adder(" ") + tb_border)


def final():
    Head_line = mark_adder("Welcom to 10formulas")
    Sub_Heading=mark_adder("10formulas : Your Ultimate Periodic Table Companion")+"\n"
    Body = "10formulas is an innovative educational program designed specifically for students to master the periodic table. Whether you're a high school student or a college undergrad, 10Formulas provides a comprehensive and interactive approach to learning and memorizing chemical formulas and element names. This Program is still in Devloping Phase Sorry For any Bug's" + "\n"
    tb(0)
    print(Head_line)
    print(Sub_Heading)
    print(Body)
    tb(1)

if __name__ == "__main__":
    final()

