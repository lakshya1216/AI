environment_status = {
    'A': input("Enter room status of A: "),
    'B': input("Enter room status of B: ")
}


current_location = input("Enter the starting location (A/B): ")


def print_environment():
    print(f"Vacuum at: {current_location} | Room A: {environment_status['A']} | Room B: {environment_status['B']}")


while True:
    print_environment()

  
    if environment_status[current_location] == 'Dirty':
        print("Action: CLEAN")
        environment_status[current_location] = 'Clean'

    else:
        
        if current_location == 'A':
            print("Action: MOVE RIGHT")
            current_location = 'B'
        else:
            print("Action: MOVE LEFT")
            current_location = 'A'

   
    if environment_status['A'] == 'Clean' and environment_status['B'] == 'Clean':
        print_environment()
        print("Both rooms are clean. Stopping.")
        break
