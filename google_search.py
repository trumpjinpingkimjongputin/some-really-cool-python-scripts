import webbrowser

def mark_1():
	logo ="""
   ___                _                    
  / __|___  ___  __ _| |___   __ ___ _ __  
 | (_ / _ \/ _ \/ _` | / -_)_/ _/ _ \ '  \ 
  \___\___/\___/\__, |_\___(_)__\___/_|_|_|
                |___/                                                                         
********************************************************
	"""
	print(logo)
	# print("What to search today ?")
	while True:	
		mySearch = input("What to search today ? \n")

		print("Opening now!")
		chrome_path = "https://www.google.com/search?q="
		webbrowser.open(chrome_path+mySearch)

mark_1()


