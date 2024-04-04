#Sophia Alexander
#M02 Lab: GPA Eval
#App evaluates wether or not a student made the honor roll or dean's list
#Last Updated: 04/03/2024





#below are various pre-defined variables
conf = '0'
Mode = '0'
fName = '0'
lName = '0'
StuNum = '0'
GPA = '0.0'



def init():
    #the two print functions below are the input prompt and welcome statement which confirms initiation of the program.
    print("Welcome to the Student Qualifier!")

    #This next chuck is supposed to ask the user for a response to the previous input prompt
    Mode = input("First, would you like to check qualifications for 1.) Honor roll or 2.) Dean's List?")

    #This chunk will ask the user to confirm their choice
    print("You chose ",Mode)
    conf = input(" is this correct?  Y/N")
    
    

#This next bit of code is a function, like how init is a function. Notice the first line, this is how it is declared.
#The code inside this function will not run until it is called on inside the main code, that being the code
#outside the function
def StuInfo():
    fName = input("What is the student's first name?")
    lName = input("What is the student's last name?")
    if lName == 'ZZZ':
        exit()
    StuNum = input("What is the student number?")
    GPA = float(input("What is the student's GPA?"))


#this next block will compare the GPA given to the standard for Mode 1: Honor Roll and print the results

def Mode1():
    StuInfo()
    if GPA<3.25:
        print(fName," ",lName, "did not make the Honor Roll")
    
    elif GPA>=3.25:
        print("Congrats, ",fName," ",lName," did make the Honor Roll!")
        
        

#this next block will compare the GPA given to the standard for Mode 2: Dean's List and print the results

def Mode2():
    StuInfo()
    if GPA<3.5:
        print(fName," ",lName, "did not make the Dean's List")
    
    elif GPA>=3.5:
        print("Congrats, ",fName," ",lName," did make the Dean's List!")
    
    Menu = input("Would you like to go back to the main menu?  Y/N")
    
    if Menu == 'Y':
        init()
        
    elif Menu != 'Y' and Menu != 'N':
        while Menu != 'Y' and Menu != 'N':
            print("Sorry, I didn't get that.")
            Menu = input("Would you like to go back to the main menu?  Y/N")



#The rest of the code is the main section, this is what the computer reads, the functions above only being read if they are referenced



#This runs the above function, init, first thing when the program is run and is read as the first line of code
init()

#This if else statement should take the user input from the choice confirmation and re-run the init funciton
#if the confirmation is N or print the below statement if it isnt.
if conf == "N":
    init()

elif conf == "Y":
    print("Great! Let's get started!")
    
#This loop in particular means that if neither of the if or elif loops apply, this while loop is activated to keep asking
#either until the user gives a valid input or until the user enters END to end the loop    
else:
    while conf != 'Y' or conf != 'N':
        print("Sorry, I didn't get that, type END to end the program")
        print("You chose ",Mode)
        conf = input(" is this correct?  Y/N")
        if conf == 'END':
            break
        
        
if Mode == 1:
    Mode1()
    
elif Mode == 2:
    Mode2()
    
else:
    print("ERROR: Please choose a valid mode using the start menu")
    init()
        
        