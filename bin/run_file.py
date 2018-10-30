chlist={'1':"Student Class",'2':"Teacher Class",'3':"School Class"}


def run():
    while True:
        print('''----Welcome to the Class System----

    1.Student's System
    2.Teacher's System
    3.School's System
    q.Exit Class System

Please input your choice >> ''')

        choice=input()
        if (choice == 'q'):
            print("Exit successfully, thanks for using our system!")
            break

        if (chlist.get(choice)):
               print (chlist.get(choice))
        else:
            print("Invalid Input. Please try again.")







run()