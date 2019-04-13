import pandas as pd
import csv

from TeamClass.Team import Team
from GameClass.Game import Game

# this is for cleaning the data from https://www.basketball-reference.com
def clean_csv(file_name):
    with open("Data/Unclean_Data/" + file_name,"r", newline="") as source: 
        reader = csv.reader(source)

        with open("Data/Clean_Data/" + file_name[0:22] + "_clean.csv",      # the new file name
                  "w",                                                      # opens the file for writing
                   newline="") \
        as result:  
            writer = csv.writer(result)   
            for row in reader: 
                writer.writerow((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[11]))

if __name__ == "__main__":
    while (input("Would you like to clean a file? (y/n)") == "y"):
        clean_csv(input("Enter the name of the CSV to clean: "))

    # dict of all teams with keys of team name
    teams = {}

    # creates a dataframe with the csv data
    df = pd.read_csv("Data/Clean_Data/2017_2018_game_history_clean.csv")
    
    # fills team_set with every team in the data
    for row in df.itertuples(False):
        # sets team_name equal to the team name in the 6th column of the csv data
        team_name = row[5]

        # if the current team hasn't been added yet, add it
        if team_name not in teams:
            teams[team_name] = Team(row[5])
    
    # adds each game to each team's game history
    for row in df.itertuples(False):
        # adds the game to the visitor's history of games
        teams[row[5]].add_game(Game(row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8]))
        
        # adds the game to the home team's history of games
        teams[row[7]].add_game(Game(row[0], row[1], row[2], row[3], row[4], row[8], row[5], row[6]))
