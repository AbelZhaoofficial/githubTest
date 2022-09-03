calculation_to_units = 24
name_of_unit ="hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        """this is how to comment, don't overuse comment"""
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, enter a positive number.")
        else:
            print("you entered a negtive number! use a positive one!")
    except ValueError:
        print("Use a positive number!")


user_input = "some text that is not exit"
# list calculate every same value.
# set not allow duplicate value.
my_list =["index0", "index1", "index2","index0"]
print(my_list[2])
my_list.append("index3")
print(my_list)
my_list.remove("index0")
print(my_list)

while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    print(set(user_input.split(",")))
    #for loop is used to iterate over a sequence like a list or set
    for num_of_days_element in set(user_input.split(",")):
        #之前validate_and_execute()里全用的是user_input,现在要改成num_of_days
        #input 获得的全都是string格式。
        #.split里面没东西的话，默认是空格来间隔元素
        validate_and_execute()

my_set = {"set0", "set1", "set2","set0"}
#set 只能添加删除元素，set是无序的。
for element in my_set:
    print(element)

my_set.add("set3")
print(my_set)
my_set.remove("set0")
print(my_set)

