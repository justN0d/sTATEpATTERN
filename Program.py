from Account import *
from State import *

name = "Eldin"
print(f"Welcome {name}")
teamsAccount = UserAccount()
teamsAccount.alert()

choice: int = -1

while(choice != 0):
    choice = int(input("\nDo you want to:\n0.Logout\n1.Set status to...\n-------------------"))

    match(choice):
        case 0:
            print("Goodbye")
            break
        case 1:
            state = int(input("Set status to:\n1.Online\n2.Busy\n3.Do not disturb\n4.Away\n5.In a meeting\n6.Offline\n-------------------"))
            match(state):
                case 1:
                    teamsAccount.setState(Online())
                case 2:
                    teamsAccount.setState(Busy())
                case 3:
                    teamsAccount.setState(DnD())
                case 4:
                    teamsAccount.setState(Away())
                case 5:
                    teamsAccount.setState(Meeting())
                case 6:
                    teamsAccount.setState(Offline())

# teamsAccount.alert()
