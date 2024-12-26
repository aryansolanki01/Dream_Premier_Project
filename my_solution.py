# A match of DPL is going on. Team Aravali has a made score of 195 for 7 in 20 overs and the opponent Team Shivalik is doing some analytics to find out what they need to do to win. You are the Data Scientist of the Team Shivalik and you have been asked to help them.

# Problem 1
# Team Shivalik has stored the runs made by Team Aravali players in the following dictionary.

aravali ={ "Dhoni":25, "Virat":31, "Pollard":11, "Rohit": 0, "Maxwell":12, "Sachin":59, "Sehwag":12 }

# Get the list of all players in Team Aravali

players_list = [p for p in aravali]
print(players_list)


# Problem 2
# By mistake, the runs made by Rohit was recorded as 0. Your next task is to figure out how many runs were made by Rohit and update the dictionary

# We know the total runs
total_runs = sum(aravali.values())

# Print runs scored by Rohit
Rohit_runs = 195 - total_runs

# Update the dictionary with correct value of runs
aravali.update({"Rohit": Rohit_runs})

# Problem 3
# Your next task is to find out who scored the second highest runs in Team Aravali

second_top = sorted(list(aravali.values()), reverse=True)[1]

for name in aravali:
    if aravali[name] == second_top:
        st_scorer = name 

print(f"The Second top scorer is : {st_scorer}")

# Problem 4
# Just out of curiosity, you want to find out the unique runs made by Team Aravali players.

run_set = set(aravali.values())
print(run_set)

# Problem 5
# Team Shivalik has 6 fixed players and 5 slots for players who are playing good currently. Create two collections using appropriate data structure to write this 6 fixed and 5 mutable players. You can choose any player you want.

# Available Players in the squad :
# ['Vijay', 'Lasith', 'Dravid', 'Smith', 'Ambati', 'Hardik', 'Sushant', 'Mandeep', 'Harbhajan', 'Yuvraj', 'Jadeja','Rajeev','Amrit']

fixed = ('Vijay', 'Lasith', 'Dravid', 'Smith', 'Ambati', 'Hardik')
mutable = ['Sushant', 'Mandeep', 'Harbhajan', 'Yuvraj', 'Jadeja']
print(fixed, mutable, sep=",")

# Problem 6
# Try changing fixed player and mutable players

# Change fixed player
# fixed.pop()                   #Can't be changed
# fixed.append("Rajeev")        #Can't be changed

# Change mutable player
mutable.pop()
mutable.append("Amrit")

# Problem 7
# Find out the runrate required for Team Shivalik to win (for 20 overs)

total_runs = 195
overs = 20

# runrate = total runs devided by total overs
runrate = (total_runs + 1) / overs

# Problem 8

# You have just received a secret message form your informant stating that some players of the other team are into match fixing. You have to decode a message and inform authorities about it.

# You received a string "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf vasuif KJSHFKJ aeuihvasf akjfhiufe" and index of "i" are going to be "no balls".

# Find the first and last no ball from the string.

#First no ball
message = "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf vasuif KJSHFKJ aeuihvasf akjfhiufe"

first_noball = message.find("i") + 1

# Last no ball
last_noball = message.rfind("i") + 1
