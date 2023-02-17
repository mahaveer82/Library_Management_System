import Borrow
import collectsplit
import Return

def start():
    while(True):
        print("     WelCome To The Library      ")
        print("***---------------------------***")
        print("Press 1 For Display The Books")
        print("Press 2 For Borrow The Books")
        print("Press 3 For Return The Books")
        print("Press 4 For Exit The Library")
        try:
            ch = int(input("Enter Your Choice: "))
            if(ch == 1):
                with open("collection.txt","r") as f:
                    lines = f.read()
                    print("")
                    print("All Books are here:-")
                    print(lines)
                    print()
            elif(ch == 2):
                collectsplit.listSplit()
                Borrow.borrowbook()
            elif(ch == 3):
                collectsplit.listSplit()
                Return.returnBook()
            elif(ch == 4):
                print("\nThankYou For Visiting!\n")
                break
            else:
                print("Choose The Valid Option")
        except ValueError:
            print("Choose As Input Suggested")
start()