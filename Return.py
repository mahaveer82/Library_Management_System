import os.path
import collectsplit
import date_time
def returnBook():
    name=input("Enter name of borrower: ")
    a = "./User_data/"+name+".txt"
    # print(a)
    try:
        with open(a, "r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        # print(type(a))
        returnBook()

    directory = './Return_user_Data/'
    b = name+".txt"
    t = os.path.join(directory, b)
    with open(t,"w+")as f:
        f.write("Library Management System \n")
        f.write("Returned By: "+ name+"\n")
        f.write("Date: " + date_time.date()+"    Time:"+ date_time.time()+"\n\n")
        f.write("S.N.\t\tBookname\t\tPrice\n")

    total=0.0
    for i in range(3):
        if collectsplit.bookname[i] in data:
            with open(t,"a") as f:
                f.write(str(i+1)+"\t\t"+collectsplit.bookname[i]+"\t\t$"+collectsplit.price[i]+"\n")
                collectsplit.quantity[i]=int(collectsplit.quantity[i])+1
            total+=float(collectsplit.price[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day
        with open(t,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    
    print("Final Total: "+ "$"+str(total)+"\n")
    with open(t,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("collection.txt","w+") as f:
            for i in range(3):
                f.write(collectsplit.bookname[i]+","+collectsplit.authorname[i]+","+str(collectsplit.quantity[i])+","+"$"+collectsplit.price[i]+"\n")
