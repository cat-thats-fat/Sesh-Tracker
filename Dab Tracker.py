#V0.01

#Importing the necessary libraries
import os
import glob
import datetime as dt

def clearconsole():
    os.system("cls" if os.name == "nt" else 'clear')
    return

#Creating a function to create a new directory
def create_directory():
    try:
        #Creating a new directory
        os.mkdir("dab data")
        #Changing the current working directory to the new directory
        os.chdir("dab data")
    except FileExistsError :
        #The folder already exists so the current working directory is changed to the folder
        os.chdir("dab data")
    return  

def homeExit(lastAction):
    clearconsole()
    try:
        print(f"{lastAction}\n1. Home\n2. Exit")
        choice = input()
    except TypeError:
        print("1. Home\n2. Exit")
        choice = input()

    if choice == "1":
        main()
    elif choice == "2":
        clearconsole()
        exit()
    else:
        homeExit()

#Creating a function for the menu
def menu():
    #Printing the menu
    print("\nMenu:\n1. Track a dab.\n2. Track a new dab.\n3. View data on dabs taken.(SOON)\n4. Exit.")
    #Asking the user to input their choice
    choice = input("Enter your choice: ")
    #Returning the choice
    return choice


#Creating a function to add a new dab
def add_dab():
    clearconsole()
    dab_name = input("What's the name/strain of the dab?")
    dab_weight = input("And whats its weight?(0.5, 1, 1.2)")
    dabs_taken = input("How many dabs did you take?")
    dab_name += f" ({dab_weight}G)"
    if os.path.exists(f"{dab_name}.txt") == True:
        print(f"Another tracked dab was found with the same name, is this the same {dab_name}  last used on___?")
        ans = input("Y/N: ")
        if ans == "Y":
          dab_file = os.open(f"{dab_name}.txt", os.O_WRONLY | os.O_CREAT)
          os.write(dab_file, (f"{dabs_taken}@{dt.datetime.now()}\n").encode())
          os.close(dab_file)
          lastAction = "Tracker Updated."
          homeExit(lastAction)
        else:
            n = 1
            while True:
                try:
                    n += 1
                    dab_name += f"({n})"
                    dab_file = os.open(f"{dab_name}.txt", os.O_WRONLY | os.O_CREAT)
                    os.write(dab_file, (f"{dabs_taken}@{dt.datetime.now()}\n").encode())
                    os.close(dab_file)
                    lastAction = "Tracker Updated."
                    homeExit(lastAction)
                except FileExistsError:
                    continue
    elif os.path.exists(f"{dab_name}.txt") == False:
        dab_file = os.open(f"{dab_name}.txt", os.O_WRONLY | os.O_CREAT)
        os.write(dab_file, (f"{dabs_taken}@{dt.datetime.now()}\n").encode())
        os.close(dab_file)
        lastAction = "Tracker Updated."
        homeExit(lastAction)
    else:
        print("An error occurred when looking for a file.")

            
            
                

          
    
def dab_db():
    print("Most Recent Dabs:")
    dirlist = glob.glob("*.txt")
    for n in range(len(dirlist)):
        dabprint = (dirlist[n].replace(".txt", ""))
        print(f'{n+1}. {dabprint}')
    dab = int(input("Which dab would you like to update?: ")) - 1
    dabs_taken = input("How many dabs did you take?")
    dab_file = os.open(dirlist[dab], os.O_WRONLY | os.O_CREAT)
    os.write(dab_file, (f"{dabs_taken}@{dt.datetime.now()}\n").encode())
    homeExit()
    clearconsole()

    return

def dabs_view():
    
    return

def main():
    choice = menu()
    if choice == "1":
        dab_db()
    elif choice == "2":
        add_dab()
    elif choice == "3":
        dabs_view()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice.")
        main()

create_directory()
main()