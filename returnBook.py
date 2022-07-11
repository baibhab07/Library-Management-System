def bookreturn():
    import borrow
    fine = 0
    import display
    d = display.start()
    import datetime
    time1 = datetime.datetime.now()
    name2 = input("Enter the name of the borrower:")

    success4 = False
    while success4 == False:
        try:
            returnbook = int(input("Enter the Book ID of the book that you want to return:"))

            if (returnbook > 5 or returnbook <= 0):
                print("Please enter a valid Book ID.")
            else:
                success4 = True
        except:
            print("Only integer type value is allowed.")

    success5 = False
    while success5 == False:
        try:
            noOfreturns = int(input("Enter the number of books you want to return:"))
            if (noOfreturns <= 0):
                print("Please enter a positive value")
            else:
                success5 = True
        except:
            print("Only integer type value is allowed.")

        print(name2, "has returned the following book:")
        print("Book Name:", d[returnbook][0],"\nAuthor:", d[returnbook][1],"\nQuantity:", noOfreturns)

    success6 = False
    while success6 == False:
        try:
            daysBorrowed = int(input("How many days did you take the book:"))
            if (daysBorrowed >= 0):
                success6 = True
            else:
                success6 = False
                print("Dear user you need to enter 1 as minimum day.")
        except:
            print("Only integer type data is allowed.")

        if (daysBorrowed > 10):
            print("Borrow duration has exceeded.Fine of $0.5 will be added.")
            daysLate = daysBorrowed - 10
            fine = daysLate*0.5
            print("Your total fine is $",fine)
        else:
            print("No fine has been added to your name.\nThank you.")

        file2 = open("Returned by"+" "+str(name2)+".txt", "w")
        file2.write("Book returned details:\n")
        file2.write("\nReturned by:"+str(name2))
        file2.write("\nBook Name:"+str(d[returnbook][0]))
        file2.write("\nBook Author:" + str(d[returnbook][1]))
        file2.write("\nQuantity of books returned:"+str(noOfreturns))
        file2.write("\nDate and time of borrow:" + str(time1))
        file2.write("\nTotal fine  is $"+str(fine))

    stock = int(d[returnbook][2])
    d[returnbook][2] = stock + noOfreturns

    file = open("file.txt","w")
    for values in d.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]))
        file.write("\n")
    file.close()

bookreturn()
