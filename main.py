def get_string(m):
    my_string = input(m)
    return my_string

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def print_fruit(L):
    for x in L:
        output = "Amy has {} {}".format(x[1], x[0])
        print(output)

def print_fruit_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} : {:10} {:10}".format(i, l[i][0], l[i][1])
        print(output)

def add_fruit(l):
    print_fruit_with_indexes(l)
    choice = get_integer("Please enter the index number of the fruit you would like to add to -> ")
    quantity = get_integer("How many {} would you like to add? -> ".format(l[choice][0]))
    l[choice][1] += quantity
    confirmation = "You now have {} {}".format(l[choice][1], l[choice][0])
    print(confirmation)

def remove_fruit(l):
    print_fruit_with_indexes(l)
    choice = get_integer("Please enter the index number of the fruit you would like to remove -> ")
    quantity = get_integer("How many {} would you like to remove? -> ".format(l[choice][0]))
    l[choice][1] -= quantity
    confirmation = "You now have {} {}".format(l[choice][1], l[choice][0])
    print(confirmation)

def add_new_fruit(l):
    print("You have selected to add new entry")
    fruit = get_string("Please enter the new fruit -> ")
    quantity = get_string("Please enter the quantity -> ")
    new_list = [fruit, quantity]
    l.append(new_list)
    confirmation = "You have added {} {}".format(quantity, fruit)
    print(confirmation)

def menu():
    fruit_list = [['Apples', 5],
                  ['Pears', 2],
                  ['Mangoes', 2],
                  ['Kiwifruit', 9],
                  ['Peaches', 3]]
    my_menu = '''
    R : Review
    A : Add To Existing fruit
    D : Delete
    N : Add New Fruit
    Q : Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        user_choice = get_string("Please enter your choice -> ")
        if user_choice == "R":
            print_fruit(fruit_list)
        elif user_choice == "A":
            add_fruit(fruit_list)
        elif user_choice == "D":
            remove_fruit(fruit_list)
        elif user_choice == "N":
            add_new_fruit(fruit_list)
        elif user_choice == "Q":
            run = False
            print("Thanks for looking through my program")
        else:
            print("Unrecognised entry")

menu()


