# Defining class for MEMBERS
class Member:
    # Initialize the object with name and an empty list of workouts
    def __init__(self, name):
        self.name = name
        self.workouts = []

    # Method to add a workout for the member
    def add_workout(self, date, exercise, weight, sets, reps):
        # Create a dictionary of the workout details
        workout = {'date': date, 'exercise': exercise,
                   'weight': weight, 'sets': sets, 'reps': reps}
        # Append the workout dictionary to the list of workouts for the member
        self.workouts.append(workout)

    # Method to view all workouts for the member
    def view_workouts(self):
        print("\n Workouts for " + self.name + ":- ")
        # Iterate through each workout dictionary for the member and print the details
        for workout in self.workouts:
            print("Date: " + workout['date'] + ", Exercise: " + workout['exercise'] +
                  ", Weight: " + str(workout['weight']) + " kg, Sets: " + str(workout['sets']) +
                  ", Reps: " + str(workout['reps']))


class Gym:
    # Initialize the object with an empty list of members
    def __init__(self):
        self.members = []

    # Method to add a new member to the gym
    def add_member(self, name):
        # Create a new Member object with the given name and append it to the list of members
        member = Member(name)
        self.members.append(member)

    # Method to add a workout for a specific member
    def add_workout(self, name, date, exercise, weight, sets, reps):
        # Iterate through each member and find the one with the matching name
        for member in self.members:
            if member.name == name:
                # Add the workout to the matching member using the Member class method
                member.add_workout(date, exercise, weight, sets, reps)

    # Method to view all workouts for a specific member
    def view_workouts(self, name):
        # Iterate through each member and find the one with the matching name
        for member in self.members:
            if member.name == name:
                # View the workouts for the matching member using the Member class method
                member.view_workouts()


# Making the GYM
gym = Gym()

# Loop to prompt the user for options and input
while True:
    print("\n \n \nWelcome to the Gym Workout Tracker!\n"
          + "Please select an option:\n"
          + "1. Add a member\n"
          + "2. Add a workout\n"
          + "3. View workouts\n"
          + "4. Exit \n"
          + "=> Enter your Choice:-")

    # Take input from user
    choice = input()

       # Option to add a member
    if choice == "1":
        name = input("Enter member name: ")
        # Add the member to the Gym object using the Gym class method
        gym.add_member(name)
        print("Member added successfully! \n")

    # Option to add a workout
    elif choice == "2":
        name = input("Enter member name: ")
        date = input("Enter date of workout (DD/MM/YYYY): ")
        exercise = input("Enter exercise: ")
        weight = float(input("Enter weight lifted (kg): "))
        sets = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps: "))
        # Add the workout
        gym.add_workout(name, date, exercise, weight, sets, reps)
        print("Workout added successfully! \n")

    elif choice == "3":
        name = input("Enter member name: ")
        # List the workout
        gym.view_workouts(name)

    elif choice == "4":
        #Exit
        print("Exiting...")
        break

    else:
        # Prompt on wrong input
        print("Invalid input, please try again. \n \n")
