calculation_to_units = 24
name_of_unit ="hours"
#将能装进def的东西，都装进def里。encapsulation.
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_number =int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, enter a positive number.")
#也可以不写对应的error type，直接except：，抓住所有的error。
#在其他语言里，叫try catch,很形象
#之所以知道叫ValueError是运行后的错误信息告诉我的。
    except ValueError:
        print("Use a positive number!")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

validate_and_execute()
