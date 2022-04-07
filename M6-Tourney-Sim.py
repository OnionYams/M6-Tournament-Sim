
# M6 Tourney sim

from audioop import maxpp


f = open("results.csv", "w")
runSim = True
unSavedChanges = False
# maxPeople = 0

temp = -1
print("Welcome to Tournaments R Us\n============================")
while temp <= 0:
    try: 
        temp = int(input("Enter the number of participants: "))
        if temp <= 0:
            print("Must be a positive number greater than 0")
    except: 
        print("Must be an integer greater than 0\n")

maxPeople = temp
print(F"\nThere are {maxPeople} participant slots ready for sign-ups.\n")

def doSim():
    global unSavedChanges, maxPeople, runSim
    people = [None]*maxPeople
    print("Participant Menu\n================\n1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit")
    # not using switch statement bc want else output
    menuItem = -1
    while menuItem <= 0 or menuItem > 5:
        try: 
            menuItem = int(input(""))
            if menuItem <= 0 or menuItem > 5:
                print("Not a valid number")
        except: 
            print("Must be an integer")
    if menuItem == 1:
        name = str(input("Participant Sign Up\n====================\nParticipant Name: "))
        spot = int
    elif menuItem == 2:
        print
    elif menuItem == 3:
        print
    elif menuItem == 4:
        if input("Save Changes\n============\nSave your changes to CSV? [y/n] ").lower() == "y":
            f.write(people)
    elif menuItem == 5:
        if input("Exit\n=====\nAny unsaved changes will be lost.\nAre you sure you want to exit? [y/n]) ").lower() == "y":
            print("\nGoodbye!")
            runSim = False

# exits in sim program
while (runSim):
    doSim()

f.close()