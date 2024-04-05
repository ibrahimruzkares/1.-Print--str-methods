command = ""
started = False
print("Welcome to Meribo Race!\n Write your command: ")
while command != "quit":
    command = input(">>>").lower()
    if command == "start":
        if started:
            print("Car already started, go ahead")
        else:
            started = True
            print("Car started, buckle up!")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped, waiting for orders.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break

    else:
        print("Sorry, I do not understand...")