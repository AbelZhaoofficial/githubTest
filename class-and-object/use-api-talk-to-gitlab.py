
import requests

response = requests.get("http://gitlab.com/api/v4/users/nanuchi/projects")
# it is a dictionary but with .text command it is changed to a string.
print(response.text)
print(type(response.text))


# json is a data type used for transporting data over the web.
# json() function converts data from json into Python data type
# for example, if response is a list json() will turn json into a list.
print(response.json())
print(type(response.json()))
print(response.json()[0])

my_projects = response.json()

for project in my_projects:
    # access key in a dictionary is using project["name"]
    print(f"Project name: {project['name']} Project Url: {project['web_url']} ")