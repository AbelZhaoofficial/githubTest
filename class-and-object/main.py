from user import *
from post import *
# now use the class blueprint to create new user object
app_user_one = User("able@able.com", "Able", "pwd", "Sec Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("InfoSec trainer")
app_user_one.get_user_info()

app_user_two = User("abel@abel.com", "Abel", "pwd0", "InfoSec Engineer")
app_user_two.get_user_info()

new_post = Post("Abel is a good worker", app_user_two.name)

new_post.get_post_info()
