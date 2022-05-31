def get_string(m):
    my_string = input(m)
    return my_string

def print_fruit(L):
    for x in L:
        output = "Amy has {} {}".format(x[1], x[0])
        print(output)

def menu():
    fruit_list = [['Apples', '5'],
                  ['Pears', '2'],
                  ['Mangoes', '2'],
                  ['Kiwifruit', '9'],
                  ['Peaches', '3']]
    my_menu = '''
    R : Review
    Q : Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        user_choice = get_string("Please enter your choice -> ")
        if user_choice == "R":
            print_fruit(fruit_list)
        elif user_choice == "Q":
            run = False
            print("Thanks for looking through my program")
        else:
            print("Unrecognised entry")

menu()









