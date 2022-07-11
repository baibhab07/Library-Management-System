def start():
    print("-----------------Welcome to Library Management System-----------")
    print()
    print("Book ID\tBook Name\tAuthor\tQuantity\tPrice")
    print()
    file = open("file.txt", "r")
    a = 1

     #reading and displaying the details to the user
    for line in file:
        print(" ", a, "\t"+line.replace(",", "\t"))
        a = a+1


    #Assigning values to dictionary
    file = open("file.txt", "r")
    d = {}
    s = 1
    for line in file:
        line = line.replace("\n", "")
        d[s] = line.split(",")
        s = s+1
    return d

start()