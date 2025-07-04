from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return current_date

def calculate_future_date(no_of_days):
  current_date = datetime.now()
  future_date = current_date + timedelta(days=no_of_days)
  return future_date.strftime("%Y-%m-%d")

print(f"Current date and time: {display_current_datetime()}")
no_of_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(no_of_days)}")