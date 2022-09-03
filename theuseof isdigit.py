calculation_to_units = 24
name_of_unit ="hours"
'''else的后面是不能加条件语句的。if 最后是可以没有else的'''
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
#indentation is important#
    elif num_of_days == 0:
        return "you entered a 0, enter a positive one."
    else:
        return "you entered a negative value. don't do that, enter a positive one"
user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
'''遇到需要分辨文件类型的情况，使用.isdigit(),学会之类的函数。'''
if user_input.isdigit():
    calculated_value = days_to_units(int(user_input))
    print(calculated_value)
else:
    print("Use a number!")

