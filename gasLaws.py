
# choose relevant law
def choose_law():
    law = input("Choose gas law: ")
    if law == "boyle":
        return boyle()
    if law == "combined":
        return combined()
    else:
        print("Please enter a valid law ")
        return choose_law()


# boyle's gas law
def boyle():
    print("Enter data, input n for the unknown variable")
    v1 = input("Please input v1(L): ")
    v2 = input("Please input v2(L): ")
    p1 = input("Please input p1(atm): ")
    p2 = input("Please input p2(atm): ")
    if p2 == "n":
        p2 = int(p1) * (int(v1) / int(v2))
        print("The final pressure is {0}".format(format(str(p1), '.4')))
    elif v2 == "n":
        v2 = (int(p1) * int(v1)) / int(p2)
        print("The final volume is {0}".format(format(str(v2), '.4')))
    elif v1 == "n":
        v1 = (int(p2) * int(v2)) / int(p1)
        print("The initial volume is {0}".format(format(str(v1), '.4')))
    elif p1 == "n":
        p1 = (int(p2) * int(v2)) / int(v1)
        print("The initial pressure is {0}".format(format(str(p1), '.4')))
    else:
        print("Please enter valid data")


# combined gas law
def combined():
    print("Enter data, input n for the unknown variable")
    v1 = input("Please input v1(L): ")
    v2 = input("Please input v2(L): ")
    p1 = input("Please input p1(atm): ")
    p2 = input("Please input p2(atm): ")
    t1 = input("Please input t1(K): ")
    t2 = input("Please input t2(K): ")
    if t2 == "n":
        t2 = (int(p2) * int(v2) / ((int(p1) * int(v1)) / int(t1)))
        print("The final temperature is: {0}".format(format(str(t2), '.4') + "K"))
    elif p2 == "n":
        p2 = (int(v2) / int(t2))


# re-run beginning function
def redo():
    retry = input("Enter y to continue: ")
    if retry == "y":
        return beginning()
    else:
        print("Have a nice day!")


def beginning():
    choose_law()
    redo()


beginning()
