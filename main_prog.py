######################################
#TO DO: 
#- COMMENTS!
#- Fuzzing
#- consolidate delete function somehow
#- delete function loops an extra time for some reason
#- if app not closed properly DB will not be pickle, fix this
#- Handle issue if userdb_file.txt is deleted (recreate/load)

#NEEDED FEATURES:
#- show users from within deletion function (done but needs refining)
#- Search by first/last name
#- Exit funtion to be able to exit entire program from any where
#- when exiting from search function, needs to go to main menu and not try to quit the program
######################################

from functions import *

userdb = load_userdb() #load the existing database of users

flag = 'y'

while flag == 'y':
	main(userdb)
	flag = input("\nDo you want to continue using program? (y)es or (n)o: ")

store_userdb(userdb) #pickling database into text file

