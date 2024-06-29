import webbrowser

user_input = input("Enter anything to search : ")
webbrowser.open(f"https://search.brave.com/search?q={user_input}&source=desktop")
