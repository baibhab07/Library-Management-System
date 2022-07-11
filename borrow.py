
def borrow():
    import display
    d = display.start()
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    time = datetime.datetime.now()
    name = input("Enter your name:")
    print("Hello", name,"," + " Welcome to Library Management System")
    num = 0

    success = False
    while success == False:
        try:
            num = int(input("Enter 1 to borrow \nEnter 2 to return \nEnter 3 to exit:"))
            if (num <= 0 or num > 3):
                print("Dear", name, ","+"Please enter either 1,2 or 3")
            else:
                success = True
        except:
            print("Dear", name,",You are allowed to input only integer value.")
            success = False


    if(num == 1):
        success1 = False
        while success1 == False:
            try:
                userinput = int(input("Enter a Book ID:"))
                if (userinput < 0 or userinput > 5):
                    print("Please enter a valid Book ID")
                else:
                    success1 = True
            except:
                print("Dear", name,",You are allowed to input only integer values.")

        success2 = False
        while success2 == False:
            try:
                stock = int(d[userinput][2])
                quantity = int(input("Enter quantity of books you want to borrow:"))
                if (stock < quantity or quantity == 0):
                    print("Dear", name,"the quantity you entered is currently not available")
                else:
                    success2 = True
            except:
                print("Dear", name, ",You are allowed to input only integer values.")
        eachprice = float(d[userinput][3].replace("$", ""))
        cost = quantity*eachprice
        print(name,"have borrowed ",quantity,"units of \""+d[userinput][0]+"\" on",year,"-",month,"-",day,"which costs "+"$",eachprice,"each.\nTotal cost for",name," is $",cost)

        d[userinput][2] = stock - quantity

        file = open("file.txt", "w")
        for values in d.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()

        file1 = open("Borrowed by"+" "+str(name)+".txt", "w")
        file1.write("Book borrowed details:\n")
        file1.write("\nBorrowed by:" + str(name))
        file1.write("\nBook Name: " + str(d[userinput][0]))
        file1.write("\nBook Author: " + str(d[userinput][1]))
        file1.write("\nQuantity of book borrowed: " + str(quantity))
        file1.write("\nDate and time of borrow:" + str(time))
        file1.write("\nPrice of the book:$" + str(eachprice))
        file1.write("\nTotal Cost:$" + str(cost))


    elif num == 2:
        import returnBook
        e = returnBook.bookreturn()


    else:
        print("Thank you for using Library Management System")
        quit()

    success3 = False
    while success3 == False:
        try:
            userContinue = input("Do you wish to continue?Press y for yes and n for no:")
            if (userContinue == "y"):
                return borrow()
                success3 = True

            elif (userContinue == "n"):
                print("Thank you for using Library Management System")
                break;

            else:
                print("Dear", name,",Please enter only y or n.")

        except:
            print("Dear", name,"Invalid input")
borrow()
