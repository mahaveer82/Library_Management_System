def listSplit():
    global bookname
    global authorname
    global quantity
    global price
    
    bookname=[]
    authorname=[]
    quantity=[]
    price=[]
    
    with open("collection.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    price.append(a.strip("$"))
                ind+=1
