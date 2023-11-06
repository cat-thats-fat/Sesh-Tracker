#Program Name: Dab Tracker
#Version: 0.3
#Author: cat-thats-fat
#Purpose: To track dabs taken and display stats on them.
#Update Date: 2021-11-05


#Importing the necessary libraries
import os
import glob
import datetime as dt

#Defining a function to clear the console
def clearconsole():
    os.system("cls" if os.name == "nt" else 'clear')
    return

#Defining a function to create a directory
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

#Defining a function to return to the home screen
def homeExit(lastAction = " "):
    try:
        print(f"{lastAction}\n1. Home\n2. Exit")
        choice = input()
    except TypeError:
        print("1. Home\n2. Exit")
        choice = input()

    if choice == "1":
        clearconsole()
        main()
    elif choice == "2":
        clearconsole()
        exit()
    else:
        clearconsole()
        homeExit()

#Defining a function to print the menu and return the user's choice
def menu():
    #Printing the menu
    print("\nMenu:\n1. Track a dab.\n2. Track a new dab.\n3. View data on dabs taken.(SOON)\n4. Exit.")
    #Asking the user to input their choice
    choice = input("Enter your choice: ")
    #Returning the choice
    return choice

#Defining a function to add a new dab to the database
def add_dab():
    clearconsole()
    #Get info
    dab_name = input("What's the name/strain of the dab?")
    dab_weight = input("And whats its weight?(0.5, 1, 1.2)")
    dabs_taken = input("How many dabs did you take?")

    clearconsole()

    dab_name += f" ({dab_weight}G)"

    #Check if the file exists
    if os.path.exists(f"{dab_name}.txt") == True:
            print(f"Another tracked dab was found with the same name, is this the same {dab_name}  last used on___?")
            ans = input("Y/N: ")

            clearconsole()

            #If the file exists, ask the user if they want to update the file
            if ans == "Y":
                with open(f"{dab_name}.txt", 'a') as dab_file:
                    dab_file.write(f"{dabs_taken}@{dt.datetime.now()}\n")
                    lastAction = "Tracker Updated."
                    homeExit(lastAction)

            #If the user doesn't want to update the file, create a new file with a number in the name
            else:
                n = 2
                while os.path.exists(f"{dab_name}({n}).txt") == True: 
                    n += 1
                with open(f"{dab_name}({n}).txt", 'a') as dab_file:
                    dab_file.write(f"{dabs_taken}@{dt.datetime.now()}\n")
                    lastAction = "New Dab Added."
                    homeExit(lastAction)
                 
    #If the file doesn't exist, create a new file
    elif os.path.exists(f"{dab_name}.txt") == False:
                 with open(f"{dab_name}.txt", 'a') as dab_file:
                    dab_file.write(f"{dabs_taken}@{dt.datetime.now()}\n")
                    lastAction = "New Dab Added."
                    homeExit(lastAction)
    else:
             print("An error occurred when looking for a file.")    
             return

#Defining a function to update a dab count in the database
def dab_db():
    print("Most Recent Dabs:")
    dirlist = glob.glob("*.txt")
    for n in range(len(dirlist)):
        dabprint = (dirlist[n].replace(".txt", ""))
        print(f'{n+1}. {dabprint}')
    dab = int(input("Which dab would you like to update?: ")) - 1

    clearconsole()

    dabs_taken = input("How many dabs did you take?")

    clearconsole()
    
    #Open the file and write the new data
    with open(dirlist[dab], 'a') as dab_file:
        dab_file.write(f"{dabs_taken}@{dt.datetime.now()}\n")
    

    lastAction = "Tracker Updated."
    homeExit(lastAction)
    return


#Defining a function to view the data on dabs taken <----
def dabs_view():
    print("Most Recent Dabs:")
    dirlist = glob.glob("*.txt")

    #Print the list of dabs
    for n in range(len(dirlist)):
        dabprint = (dirlist[n].replace(".txt", ""))
        print(f'{n+1}. {dabprint}')
    
    #Ask the user which dab they want to view
    dab2view = int(input("Which dab's stats would you like to see?: ")) - 1
    dab_name = dirlist[dab2view].replace(".txt", "")
    clearconsole()

    #Open the file and read the data then split it into a list
    with open(dirlist[dab2view], 'r') as dab_stats:
        dab_stats = dab_stats.read().splitlines()
        dabs_taken = []
        dates = []

        #split around @ to divide dabs and date
        for n in range(0, len(dab_stats), 2):
            stat = dab_stats[n]
            temp = stat.split("@")
            dabs_taken.append(int(temp[0]))
            dates.append(temp[1])
            
        
        dates.sort()
        total_dabs = sum(dabs_taken)

        #set the strings to datetime objects
        try:
            first_dab = dt.datetime.strptime(dates[0], "%Y-%m-%d %H:%M:%S.%f")
            last_dab = dt.datetime.strptime(dates[-1], "%Y-%m-%d %H:%M:%S.%f")
        except IndexError:
            lastAction = f"Not enough data for {dab_name} yet."
            homeExit(lastAction)
            return

        #print the stats
        print(f"{dab_name} Stats:\nTotal Dabs: {total_dabs}\nFirst Dab: {first_dab}\nLast Dab: {last_dab}")
        print(f"Time Lasted: {(last_dab - first_dab).days} days & {(last_dab - first_dab).seconds//3600} hours.")
        print()
    lastAction = "Stats Found"
    homeExit(lastAction)

    return

def main():
    choice = menu()
    clearconsole()
    if choice == "1":
        clearconsole()
        dab_db()
    elif choice == "2":
        clearconsole()
        add_dab()
    elif choice == "3":
        clearconsole()
        dabs_view()
    elif choice == "4":
        clearconsole()
        exit()
    else:
        print("Invalid choice.")
        main()

create_directory()
main()