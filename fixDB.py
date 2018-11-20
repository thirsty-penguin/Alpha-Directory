# This can be used if the "userdb_file.txt" somehow gets deleted 
# this will recreate the file and require one user to be created (so the file is not empty)
# Then the main_prog can be run as normal

import pickle

user = {}
fname = input("\nEnter First Name: ")
lname = input("Enter Last Name: ")
userid = input("Enter New User ID: ")
password = input("Enter password: ")
position = input("Enter position (optional): ")
pay = input("Enter pay (optional): ")
user[userid] = {'password': password, 'first': fname.title(), 'last': 
					 lname.title(), 'position': position.title(), 'pay': pay}
					 
userdb_file = open('userdb_file.txt', 'wb') 
pickle.dump(user,userdb_file) 
userdb_file.close()




