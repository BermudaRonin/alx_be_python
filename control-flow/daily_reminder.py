task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

prefix = "Note"
body = f""
separator = " "
message = "that requires immediate attention today!"

if time_bound == "yes":
    prefix = "Reminder"
    separator = " "
    message = "that requires immediate attention today!"
else:
    match priority:
        case "high":
            prefix = "Reminder"
            separator = " "
            message = "that requires immediate attention today!"
        case "medium":
            prefix = "Note"
            message = "schedule it for later"
        case "low":
            prefix = "Note"
            separator = ". "
            message = "Consider completing it when you have free time."

print(f"{prefix}: '{task}' is a {priority} priority task{separator} {message}")
