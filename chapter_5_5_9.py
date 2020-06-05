# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# 
# • If the list is empty, print the message We need to find some users!
# 
# • Remove all of the usernames from your list, and make sure the correct message is printed.

# exercise 5-8
# users = ["admin","user1","user2","user3","user4"]
users = []

if len(users) is 0:
    print("We need to find some users!")
else:
    for i in users:
        if i is "admin":
            print("Hello admin, do you want me to print a report?")
        else:
            print("Hello " + i + " welcome!")
