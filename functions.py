import pickle 

def create_user(db, user_amount): #determines how many users need to be created
	for num in range(1, user_amount + 1): 
		user = get_userinfo()  #calls function to get input data for new user
		db.update(user)   #adding user to existing database
		print ("\nUser created successfully\n")

def delete_user(db): #function to delete user
	while True:
			try:
				deletion_amount = int(input("\nEnter number of users that you want to delete: "))
			except ValueError:
				print ("Please enter a valid number")
				continue
			if deletion_amount <= 0:
				print ("Invalid number entered")
				continue
			else:
				break		
	print ("\n--- DELETION MENU ---" + "\n" \
			"- Enter 'show' to enter search menu \n" + \
			"- Enter 'exit' to close program")
	for num in range(1, deletion_amount + 1):
		user = input("\nEnter userid to remove: ")
		if user in db:
			confirm = input("\nAre you sure you want to delete user? - " + \
					db[user]['first'] + " " + db[user]['last'] + \
					"\nEnter (y)es || (n)o || (c)ancel: ")
			if confirm == 'y':  
				del db[user]   #removes user from database
				print ("\nUser has been deleted")
			elif confirm == 'n':
				while True:
					print ("\nEnter 'show' to enter search menu")
					user = input("Re-Enter userid to remove: ")
					if user in db:
						confirm = input("\nAre you sure you want to delete user? - " + \
						db[user]['first'] + " " + db[user]['last'] + \
						"\nEnter (y)es || (n)o || (c)ancel: ")
						if confirm == 'y':
							del db[user]
							print ("\nUser has been deleted")
						elif confirm == 'n':
							continue
						elif confirm == 'c':
							print ("User deletion has been cancelled")
							break
					elif user == 'show':
						search_users(db)
						delete_user(db)
					elif user == 'quit':
						break
					else:
						print ('ERROR: That user does not exist')
						flag = 'y'	
			elif confirm == 'c':
				print ("User deletion has been cancelled")		
		elif user == 'show':
			search_users(db)
			delete_user(db)
		elif user == 'exit':
			main(db)
		else:
			print ("\nERROR: That user does not exist\n")
			delete_user(db)
			
def get_userinfo(): #gets info when created new users
	user = {}
	fname = input("\nEnter First Name: ")
	lname = input("Enter Last Name: ")
	userid = input("Enter New User ID: ")
	password = input("Enter password: ")
	position = input("Enter position (optional): ")
	pay = input("Enter pay (optional): ")
	#creates dict of info for user 
	user[userid] = {'password': password, 'first': fname.title(), 'last': 
					 lname.title(), 'position': position.title(), 'pay': pay}
	return user
					
def load_userdb(): #loads pickled database into file
	infile = open('userdb_file.txt', 'rb')
	userdb_file = pickle.load(infile)
	return userdb_file
	infile.close()
		
	
def main(db):
	print ("\n***** ALPHA DIRECTORY *****")
	print ("--- Actions ---")
	question = input("Enter 's' for Search \nEnter 'c' to create user(s)\
				\nEnter 'd' to delete user(s) \nEnter 'q' to quit program \
			  	\nOption: ")
	if question == 'c': #Create Users
		users_needed = int(input("\nEnter number of users that you need to create: "))
		create_user(db, users_needed)
	elif question == 's': #Search Users
		search_users(db)
	elif question == 'd': #Delete Users
		delete_user(db)
	elif question == 'q': #Exit program
		exit("\nALPHA DIRECTORY HAS BEEN CLOSED")
	else:
		print ("\nERROR: That is not a valid command.\n")
		main(db)	
	
def search_users(db):
	print ("\n--- SEARCH MENU ---" + "\nNotes:")
	print ("- Enter 'all' for full list" + "\n- Enter 'exit' to quit search")
	flag = 'y'
	while flag == 'y':
		user_requested = input("\nEnter userid you wish to search: ")
		if user_requested in db: #display information of single user
			print ("\n***********************" + "\n-----RESULTS-----")
			print ("User ID: " + user_requested) 
			for key, value in db[user_requested].items():
				print (key.title() + ": " + value)
			print ("***********************")
		elif user_requested == "all": #displays all existing user info
			print ("\n***********************" + "\n-----RESULTS-----")
			for userid, info in db.items():
				print ("\nUser ID: " + userid)
				for key, value in info.items():
					print (key.title() + ": " + value)
			print ("***********************")
		elif user_requested == "exit":
			flag = 'exit'
		else:
			print ('\nERROR: That user does not exist.')
			
#def search_by_name(db):
			#####Search by users first/last name
		#elif user_requested in db[userid]['first']:
		#####
		
def store_userdb(db): #pickles database every time program is run
	userdb_file = open('userdb_file.txt', 'wb') 
	pickle.dump(db,userdb_file) 
	userdb_file.close()									
			
