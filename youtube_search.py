import webbrowser

logo="""
 __   __        _        _                        
 \ \ / /__ _  _| |_ _  _| |__  ___   __ ___ _ __  
  \ V / _ \ || |  _| || | '_ \/ -_)_/ _/ _ \ '  \ 
   |_|\___/\_,_|\__|\_,_|_.__/\___(_)__\___/_|_|_|
                                                  
"""
print(logo+"\n")
def mark_1():
    while True:
        mySearch = input("What to search today ?\n")
        youtube_path="https://www.youtube.com/results?search_query="
        print("Opening Now !")
        webbrowser.open(youtube_path+mySearch)
mark_1()
