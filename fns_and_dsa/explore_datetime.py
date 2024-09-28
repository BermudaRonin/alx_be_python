from datetime import datetime, timedelta

current_date = datetime.now()

print(f"Current date and time: {current_date}")

days = int(input("Enter the number of days to add to the current date: "))
future_date = current_date + timedelta(days=days)

print("Future date:", future_date.strftime("%Y-%m-%d"))