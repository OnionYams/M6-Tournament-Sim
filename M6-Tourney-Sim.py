
# M6 Tourney sim

from audioop import maxpp


f = open("results.csv", "w")
runSim = True
unSavedChanges = False
# maxPeople = 0

# get max participants, don't need temp but w/e
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
#fill array with dummy vals
people = [None]*maxPeople
print(F"\nThere are {maxPeople} participant slots ready for sign-ups.\n")

def doSim():
    global unSavedChanges, maxPeople, runSim, people
    
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
        # if no slots exit
        if people.count(None) == 0:
            print("No slots remaining")
            return
        name = str(input("Participant Sign Up\n====================\nParticipant Name: "))
        spot = -1
        while spot <= 0 or spot > maxPeople:
            try: 
                spot = int(input(F"Desired starting slot #[1-{maxPeople}]: "))
                if spot <= 0 or spot > maxPeople:
                    print("Not a valid number")
            except: 
                print("Must be an integer")
        # repeated while to get new values if bad entry
        while people[spot-1] != None:
            print(F"Error:\nSlot #{spot} is filled.  Please try again.\n")
            # get new val, otherwise next loop always eval true
            try: 
                    spot = int(input(F"Desired starting slot #[1-{maxPeople}]: "))
                    if spot <= 0 or spot > maxPeople:
                        print("Not a valid number")
            except: 
                    print("Must be an integer")

            while spot <= 0 or spot >= maxPeople:
                try: 
                    spot = int(input(F"Desired starting slot #[1-{maxPeople}]: "))
                    if spot <= 0 or spot > maxPeople:
                        print("Not a valid number")
                except: 
                    print("Must be an integer")
        people[spot-1] = name
        # print(name,spot,people)
        print(F"Success:\n{name} is signed up in starting slot #{spot}.")    
   #cancel entries
    elif menuItem == 2:
        # if no entries can't cancel
        if people.count(None) == len(people):
            print("Nothing to be cancelled")
            return
        print("Participant Cancellation\n====================")
        spot = -1
        runCancel = True
        while(runCancel):
            # get new spot for each loop
            try: 
                    spot = int(input(F"Starting slot #[1-{maxPeople}]: "))
                    if spot <= 0 or spot > maxPeople:
                        print("Not a valid number")
            except: 
                    print("Must be an integer")
            #annoying. need try catch for every input
            while spot <= 0 or spot > maxPeople:
                try: 
                    spot = int(input(F"Starting slot #[1-{maxPeople}]: "))
                    if spot <= 0 or spot > maxPeople:
                        print("Not a valid number")
                except: 
                    print("Must be an integer")
            name = input("Participant Name: ")
            if people[spot-1] != name:
                print(F"Error:\n{name} is not in that starting slot.")
            else:
                people[spot-1] = None
                print(F"Success:\n{name} has been cancelled from starting slot #{spot}.")
                runCancel = False
    #show values
    elif menuItem == 3:
        print("View Participants\n====================")
        spot = -1
        while spot <= 0 or spot > maxPeople:
            try: 
                spot = int(input(F"Starting slot #[1-{maxPeople}]: "))
                if spot <= 0 or spot > maxPeople:
                    print("Not a valid number")
            except: 
                print("Must be an integer")
        
        #get 5 lower and 5 higher if exist
        low = 0 if spot-5 < 0 else spot-5
        high = maxPeople if spot+5 > maxPeople else spot+5

        print("Starting Slot: Participant")
        for i in range(low, high):
            print(str(i+1) + ": " + (people[i] if people[i] is not None else "[empty]"))

    # write to csv
    elif menuItem == 4:
        if input("Save Changes\n============\nSave your changes to CSV? [y/n] ").lower() == "y":
            for i in range(len(people)):
                if people[i] == None:
                    people[i] = "None"
            # write each to a newline, this way preserves ordering
            f.write("\n".join(people))
            print("Written")
    #exit sim
    elif menuItem == 5:
        if input("Exit\n=====\nAny unsaved changes will be lost.\nAre you sure you want to exit? [y/n]) ").lower() == "y":
            print("\nGoodbye!")
            runSim = False

# exits in sim program
while (runSim):
    doSim()

f.close()