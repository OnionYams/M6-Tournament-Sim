
# M6 Tourney sim

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
    global unSavedChanges, maxPeople
    people = {}
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

    runSim = False

# exits in sim program
while (runSim):
    doSim()

print("Simulation over")
f.close()