calculation_to_units = 24
name_of_unit ="hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

my_var = days_to_units(20)
#if you use (=a function) you make sure the function has return  in it)
print(my_var)

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

print(user_input)