#Author:    Andrew Davidson
#Date:      05/07/2019
#
#This program allows the user to sign in with an existing login ID / password, create a new login ID / password,
#or change the password for an exisiting login ID. At program start: Login IDs and passwords are read in from a 
#file ("password.dat") and stored in a data dictionary (passwordDictionary). At program end: the Login IDs / passwords
#in passwordDictionary are written to password.dat. new Login IDs / passwords must be validated before they are created.

import os
clear = lambda : os.system('cls')
passwordDictionary = {}

def main():
    readFile()
    menu()
    writeFile()

def readFile():
    #Reads from password.dat and stores Login IDs / passwords in a data dictionary
    #if password.dat does not exist: creates password.dat file
    try:
        passFile = open("password.dat", "r")
    except:
        passFile = open("password.dat", "w+")

    iLogin = passFile.readline()
    iPass = passFile.readline()

    while iLogin != "" and iPass != "":
        iLogin = iLogin.rstrip("\n")
        iPass = iPass.rstrip('\n')

        passwordDictionary[iLogin] = iPass

        iLogin = passFile.readline()
        iPass = passFile.readline()

    passFile.close()

def menu():
    #Calls function based on option selected
    optionSelect = 0
    
    clear()
    print("Please select an option")
    
    optionSelect = optionInputAndValidation()

    if optionSelect == 1:
        optionSignIn()
    elif optionSelect == 2:
        optionCreate()
    elif optionSelect == 3:
        optionResetPassword()
    else: 
        clear()
        print("User signed out successfully.")
        print("\nProgram ending...\n")

def optionInputAndValidation():
    #Prompts user to enter 1-4. Loops until valid option is entered.
    option = 0
    errSw = True

    while errSw:
        print("1 - Sign in")
        print("2 - Create new user")
        print("3 - Reset password")
        print("4 - Exit Program")
        try:
            option = int(input())
            if option < 1 or option > 4:
                print("\nInvalid option. Please select 1-4")
            else:
                errSw = False
        except:
            print("\nInvalid option. Please select 1-4")

    return option

def optionSignIn():
    #Prompts the user to enter their login ID and password. Validates that login ID is in passwordDictionary.keys(),
    #and that password matches the login ID. Returns to menu if either login ID or password are invalid.
    clear()

    loginID = input("Enter Login ID:\n")
    if loginID in passwordDictionary.keys():
        password = input("\nEnter password:\n")
        if password == passwordDictionary[loginID]:
            clear()
            print("User logged in successfully!")
            rtn = input("\nPress Enter to return to main menu...")
            menu()
        else:
            print("\nError: Invalid password.")
            rtn = input("\nPress Enter to return to main menu...")
            menu()
    else:
        print("\nError: Invalid Login ID.")
        rtn = input("\nPress Enter to return to main menu...")
        menu()

def optionCreate():
    #Prompts the user to create a new Login ID / password. Validates Login ID and password.
    #Creates and stores new Login ID / password in passwordDictionary. (written to password.dat on program close)
    clear()
    
    loginID = validateLoginID()
    password = validatePassword(loginID)

    passwordDictionary[loginID] = password

    #Success message / return to menu
    clear()
    print("New Login ID and password created successfully.")
    rtn = input("\nPress Enter to return to main menu...")
    menu()

def validateLoginID():
    #Validates Login ID: 6 – 10 letters, 2 numbers, No white space, Must not exist in the password.dat file
    #loops until valid, returns valid Login ID
    errSw = True
    while errSw:
        num2 = 0
        letters = 0
        blankspace = False

        loginID = input("Enter a new login ID:\n")
        for char in loginID:
            if char.isdigit():
                num2 += 1
            elif char == " ":
                blankspace = True
            elif char.isalpha:
                letters += 1
            
        if letters < 6 or letters > 10:
            print("Error: Login ID must contain between 6 - 10 letters.")      
        elif num2 < 2:
            print("Error: Login ID must contain at least 2 numbers.")
        elif blankspace:
            print("Error: Login ID cannot contain blank spaces.")
        elif loginID in passwordDictionary.keys():
            print("Error: Login ID already exists.")
        else:
            errSw = False

    return loginID


def validatePassword(loginID):
    #Validates password: 6 – 12 length, 1 number, 1 upper case letter, 1 lower case letter, No white space, 
    #cannot contain login ID, must be a unique password.
    #loops until valid, returns valid password
    errSw = True
    while errSw:
        num1 = 0
        upper1 = 0
        lower1 = 0
        blankspace = False
        
        password = input("\nEnter a new password:\n")
        for char in password:
            if char.isdigit():
                num1 += 1
            elif char.isupper():
                upper1 += 1
            elif char.islower():
                lower1 += 1
            elif char == " ":
                blankspace = True

        if len(password) < 6 or len(password) > 12:
            print("Error: Password must be between 6 - 12 characters in length.")      
        elif num1 < 1:
            print("Error: Password must contain at least 1 number.")
        elif upper1 < 1:
            print("Error: Password must contain at least 1 Uppercase letter.")
        elif lower1 < 1:
            print("Error: Password must contain at least 1 lowercase letter.")
        elif blankspace:
            print("Error: Password cannot contain blank spaces.")
        elif loginID in password:
            print("Error: Password cannot contain the Login ID.")
        elif password in passwordDictionary.values():
            print("Error: Password must be unique.")
        else:
            errSw = False

    return password


def optionResetPassword():
    #Promps the user to validate their login ID / password. If valid, prompts user to create a new
    #password. Validates new password, then if valid: replaces the password for the login ID.
    clear()

    loginID = input("Validate Login ID:\n")
    if loginID in passwordDictionary.keys():
        password = input("\nValidate password:\n")
        if password == passwordDictionary[loginID]:
            newPassword = validatePassword(loginID)
            passwordDictionary[loginID] = newPassword

            clear()
            print("Password reset successfully.")
            rtn = input("\nPress Enter to return to main menu...")
            menu()
        else:
            print("\nError: Invalid password.")
            rtn = input("\nPress Enter to return to main menu...")
            menu()
    else:
        print("\nError: Invalid Login ID.")
        rtn = input("\nPress Enter to return to main menu...")
        menu()

def writeFile():
    #at program close, writes all keys / values from passwordDictionary to the password.dat file.
    passFile = open("password.dat", "w")
        
    for x in passwordDictionary.keys():
        passFile.write(x + "\n")
        passFile.write(passwordDictionary[x] + "\n")

    passFile.close()
main()
