
while True:
    tm = 80 
    english=int(input("enter the english\n"))
    if english>tm:
        print(f" * ENTER VALID MARKS BELOW {tm} * ")
        break
    maths=int(input("enter the marks for maths\n"))
    if maths>tm:
        print(f" * ENTER VALID MARKS BELOW {tm} * ")
        break
    science= int(input("enter the marks for science\n"))
    if science>tm:
        print(f" * ENTER VALID MARKS BELOW {tm}* ")
        break
    computer=int(input("enter the marks for computer\n"))
    if computer>tm:
        print(f" * ENTER VALID MARKS BELOW {tm}* ")
        break
    sst=int(input("enter the marks for sst\n "))
    if sst>tm:
        print(f" * ENTER VALID MARKS BELOW {tm} * ")
        break
    total= english+maths+science+computer+sst
    totalsubmarks= 400 
    percentage= (total/totalsubmarks)*100
    grades = ""
    if percentage>90:
        grades= "A++"
    elif percentage>80:
        grades= "A+"
    elif percentage>70:
        grades= "A"
    elif percentage>60:
        grades = "B"
    elif percentage>50:
        grades = "C"
    elif percentage>40:
        grades = "D"
    else:
        grades = "Fail"

    print(f" -->your grade out of {totalsubmarks} is {grades}   \n **your total percentage is {percentage}**")
    if percentage>40:
        print("** congo u are passed **")
    else:
        print(" sorry you are fial ")
    break