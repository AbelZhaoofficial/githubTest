from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")
#at this point input is still a string (by default)
goal = input_list[0]
deadline = input_list[1]
# the first datetime is a module,
# the second datetime is a class in the module
# The strptime() is s method creating a datetime object from the given string.
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
#if use %y, we have 12.07.21, if use %Y, we have 12.07.2021
print(type(datetime.strptime(deadline, "%d.%m.%Y")))
today_date = datetime.today()
print(datetime.today())
time_till = deadline_date - today_date
print(f"Dear User! Time remaining for your goal: {goal} is {time_till.days} days")
print(f"Dear User! Time remaining for your goal: {goal} is {int(time_till.total_seconds() / 60 / 60)} hours")
