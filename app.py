from unittest import result
from db_helpers import *


user_name = input("To begin, enter your username: ")
print("welcome to Innotech blog  " + user_name + ",")

print("what will you like to do: ")
print("1. write a post")
print("2. see all posts")
print("3. exit app")


action = input()

if action == "1":
    content_post = input("please write your post: ")
elif action == "2":
  
  print("showing all posts:")
else:
  print("Invalid Entry")


run_query("INSERT into command_line_post (username, content) VALUES (?,?)",[user_name, content_post])

users= run_query("SELECT * from command_line_post")
print(users)
