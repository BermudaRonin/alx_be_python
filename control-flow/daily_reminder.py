property_enum = ["high", "midium", "low"]
time_bound_enum = ["yes", "no"]

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

prefix = "Reminder" if time_bound == "yes" else "Note"

message = ""
match priority:
    case "high" :
        message = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    case "medium" | "low" :
        message = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _ :
        print(f"Wrong priority, Must be one of {"/".join(property_enum)}")

if time_bound == "yes":
    print("Reminder : " + message)
else:
    print("Note : " + message)
