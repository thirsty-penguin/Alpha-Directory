from functions import *

userdb = load_userdb() #load the existing database of users

flag = 'y'

while flag == 'y':
	main(userdb)
	flag = input("\nDo you want to continue using program? (y)es or (n)o: ")

store_userdb(userdb) #pickling database into text file

