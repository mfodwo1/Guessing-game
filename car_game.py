
while True:
    user_input = []
    command = input("> ").lower()
    user_input.append(command)
    if command == "start":
        print("Car start... Ready to go")
    elif command == "stop" and command not in user_input:
        print("Car stopped")
    #elif command == "stop" and command in user_input:
     #   print("Car has already stopped")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To quit the game
        """)
    elif command == "quit":
        break
