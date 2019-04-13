import pandas as pd
import csv

from TeamClass.Team import Team
from GameClass.Game import Game

# helper method to turn a team name into its acronym, for CSV cleaning
def acronym(name):
    if name == "Atlanta Hawks":
        return "ATL"
    elif name == "Brooklyn Nets":
        return "BKN"
    elif name == "Boston Celtics":
        return "BOS"
    elif name == "Charlotte Hornets":
        return "CHA"
    elif name == "Chicago Bulls":
        return "CHI"
    elif name == "Cleveland Cavaliers":
        return "CLE"
    elif name == "Dallas Mavericks":
        return "DAL"
    elif name == "Denver Nuggets":
        return "DEN"
    elif name == "Detroit Pistons":
        return "DET"
    elif name == "Golden State Warriors":
        return "GSW"
    elif name == "Houston Rockets":
        return "HOU"
    elif name == "Indiana Pacers":
        return "IND"
    elif name == "Los Angeles Clippers":
        return "LAC"
    elif name == "Los Angeles Lakers":
        return "LAL"
    elif name == "Memphis Grizzlies":
        return "MEM"
    elif name == "Miami Heat":
        return "MIA"
    elif name == "Milwaukee Bucks":
        return "MIL"
    elif name == "Minnesota Timberwolves":
        return "MIN"
    elif name == "New Orleans Pelicans":
        return "NOP"
    elif name == "New York Knicks":
        return "NYK"
    elif name == "Oklahoma City Thunder":
        return "OKC"
    elif name == "Orlando Magic":
        return "ORL"
    elif name == "Philadelphia 76ers":
        return "PHI"
    elif name == "Phoenix Suns":
        return "PHX"
    elif name == "Portland Trail Blazers":
        return "POR"
    elif name == "Sacramento Kings":
        return "SAC"
    elif name == "San Antonio Spurs":
        return "SAS"
    elif name == "Toronto Raptors":
        return "TOR"
    elif name == "Utah Jazz":
        return "UTA"
    elif name == "Washington Wizards":
        return "WAS"            

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
                writer.writerow((row[0], row[1], row[2], row[3], row[4], acronym(row[5]), row[6], acronym(row[7]), row[8], row[11]))

if __name__ == "__main__":
    # continously asks whether the user wants to clean a file, then cleans the given file
    while (input("Would you like to clean a file? (y/n)") == "y"):
        clean_csv(input("Enter the name of the CSV to clean: "))

    # dict of all teams with keys of team name
    teams = {}

    # an alphabetically ordered list of teams
    ordered_team_list = []

    # creates a dataframe with the csv data
    df = pd.read_csv("Data/Clean_Data/2017_2018_game_history_clean.csv")

    # fills team_set with every team in the data
    for row in df.itertuples(False):
        # sets team_name equal to the team name in the 6th column of the csv data
        team_name = row[5]

        # if the current team hasn't been added yet, add it
        if team_name not in teams:
            team = Team(row[5])
            teams[team_name] = team
            ordered_team_list.append(team)

    # orders the teams by team name
    ordered_team_list.sort(key=lambda team: team.name)

    # adds each game to each team's game history
    for row in df.itertuples(False):
        # adds the game to the visitor's history of games
        teams[row[5]].add_game(Game(row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8]))

        # adds the game to the home team's history of games
        teams[row[7]].add_game(Game(row[0], row[1], row[2], row[3], row[4], row[8], row[5], row[6]))

    # prints the average points for each team
    for team in ordered_team_list:
        total_points = 0

        # looks at each game for the team's history and adds up its points
        for game in team.game_history:
            total_points += game.my_points

        # calculates and prints the mean points
        print(team.name, "{0:.2f}".format((total_points / len(team.game_history))))
