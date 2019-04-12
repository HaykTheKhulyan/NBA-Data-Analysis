import csv

# this is for cleaning the data from https://www.basketball-reference.com

#with open("2017_2018_game_history.csv","r", newline="") as source:
#    reader = csv.reader(source)
#    with open("2017_2018_game_history_clean.csv","w", newline="") as result:
#        writer = csv.writer(result)
#        for row in reader:
#            writer.writerow((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[11]))

from TeamClass.Team import Team

import pandas as pd

if __name__ == "__main__":
    # dict of all teams with keys of team name
    teams = {}

    # creates a dataframe with the csv data
    df = pd.read_csv("2017_2018_game_history_clean.csv")
    
    # fills team_set with every team in the data
    for row in df.itertuples(False):
        # sets team_name equal to the team name in the 6th column of the csv data
        team_name = row[5]

        # if the current team hasn't been added yet, add it
        if team_name not in teams:
            teams[team_name] = Team(row[5])
    
    # adds each game to each team's game history
    for row in df.itertuples(False):
        pass            

    print(len(team_name_set))
    print(len(team_set))
