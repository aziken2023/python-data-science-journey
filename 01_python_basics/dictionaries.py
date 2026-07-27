#List of player information
player = {"name": "Cole Palmer", "Age": 21, "club": "Chelsea", "position": "Midfielder", "goals": 15, "assists": 15}

#print certain information about the player
print(player["name"])
print(player["club"])
print(player["goals"])

#basic modfiying
player["goals"] = 20
print(player["goals"])
player["Country"] = "England"
print(player["Country"])
del player["assists"]