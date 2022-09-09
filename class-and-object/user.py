class User:
    # class use captial letter like User. file name use low case letter like user.py
    def __init__(self, email, name, password, current_job_title):
        # constract objects in user class
        # the email in () just means this class need parameter, it doesn't need to be "email"
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # below is the constracted object, we created class definition
    # functions belongs to class is called a method, here is two methods ""
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}, and you can contact him at {self.email}")
'''
# now use the class blueprint to create new user object
app_user_one = User("able@able.com", "Able", "pwd", "Sec Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("InfoSec trainer")
app_user_one.get_user_info()

app_user_two = User("abel@abel.com", "Abel", "pwd0", "InfoSec Engineer")
app_user_two.get_user_info()
'''