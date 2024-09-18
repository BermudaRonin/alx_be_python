property_enum = ["high", "midium", "low"]
time_bound_enum = ["yes", "no"]

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

prefix = "Reminder" if time_bound == "yes" else "Note"
match priority:
    case "high" :
        print(f"{prefix} : '{task}' is a {priority} priority task that requires immediate attention today!")
    case "medium" | "low" :
        print(f"{prefix} : '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _ :
        print(f"Wrong priority, Must be one of {"/".join(property_enum)}")
