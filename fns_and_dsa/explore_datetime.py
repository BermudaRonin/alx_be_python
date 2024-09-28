from datetime import datetime, timedelta

def display_current_datetime():
    print(f"Current date and time: {datetime.now()}")

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))