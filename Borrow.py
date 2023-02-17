import os.path
import date_time
import collectsplit

def borrowbook():
    success = False
    while(True):
        firstname = input("Enter The Borrower First Name: ")
        if firstname.isalpha():
            break
        print("Enter The Name Range Between A-Z")
    
    while(True):
        secondname = input("Enter The Borrower Last Name: ")
        if secondname.isalpha():
            break
        print("Enter The Name Range Between A-Z")

    directory = './User_Data/'
    filename = firstname+".txt"
    t = os.path.join(directory, filename)
    with open(t,"w+") as f:
        f.write("Library Management System")
        f.write("Borrowed By: "+firstname+" "+secondname+"\n")
        f.write("Date: "+date_time.date()+"\tTime: "+date_time.time()+"\n")
        f.write("S.N. \t\t  Bookname \t     Authorname \n" )

    while success == False:
        print("Please select a option below: ")
        for i in range(len(collectsplit.bookname)):
            print("Enter", i, " to Borrow Book:", collectsplit.bookname[i])

        try:
            a = int(input())
            try:
                if(int(collectsplit.quantity[a])>0):
                    print("Book is Available")
                    with open(t, "a") as f:
                        f.write("1. \t\t"+collectsplit.bookname[a]+"\t\t  "+collectsplit.authorname[a]+"\n")
                    
                    collectsplit.quantity[a]=int(collectsplit.quantity[a])-1
                    with open("collection.txt", "w+") as f:
                        for i in range(3):
                            f.write(collectsplit.bookname[i]+","+collectsplit.authorname[i]+","+str(collectsplit.quantity[i])+","+"$"+collectsplit.price[i]+"\n")


                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Do You Want to Buy More Books In Library Press Yes For Y: "))
                        if (choice.upper() == "Y"):
                            count=count+1
                            print("Please select a option below")
                            for i in range(len(collectsplit.bookname)):
                                print("Enter",i, "to borrow book", collectsplit.bookname[i])
                            a = int(input())
                            if(int(collectsplit.quantity[a])>0):
                                print("Book is Available")
                                with open(t,"a") as f:
                                    f.write(str(count)+". \t\t"+ collectsplit.bookname[a]+"\t\t  "+collectsplit.authorname[a]+"\n")

                                collectsplit.quantity[a] = int(collectsplit.quantity[a])-1
                                with open("collection.txt","w+") as f:
                                    for i in range(3):
                                        f.write(collectsplit.bookname[i]+","+collectsplit.authorname[i]+","+str(collectsplit.quantity[i])+","+"$"+collectsplit.price[i]+"\n")
                                        success = False
                            else:
                                loop = False
                                break
                        elif(choice.upper() == "N"):
                            print("Thankyou So much for borrowing book from us")
                            print("")
                            loop = False
                            success = True
                        else:
                            print("Please choose Intruction Carefully")
                else:
                    print("Book is not available")
                    borrowbook()
                    success=False

            except IndexError:
                print("")
                print("please choose book according to their number")

        except ValueError:
            print("")
            print("Please Choose Another Option")




        
        
