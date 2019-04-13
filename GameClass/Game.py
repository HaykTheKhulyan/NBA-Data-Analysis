import datetime

# helper method that converts month name into a number
def month_name_to_number(name):
    if name == "Jan":
        return 1
    elif name == "Feb":
        return 2
    elif name == "Mar":
        return 3
    elif name == "Apr":
        return 4
    elif name == "May":
        return 5
    elif name == "Jun":
        return 6
    elif name == "Jul":
        return 7
    elif name == "Aug":
        return 8
    elif name == "Sep":
        return 9
    elif name == "Oct":
        return 10
    elif name == "Nov":
        return 11
    elif name == "Dec":
        return 12

class Game:

    def __init__(self, day, month, day_number, year, start_time, my_points, other_team, other_team_points):
        hour = start_time[0:2]

        if hour[1] == ":":
            hour = hour[0]

        self.game_datetime = datetime.datetime(int(year), month_name_to_number(month), int(day_number), int(hour), int(start_time[-3:-1]))
        
        self.my_points = my_points
        self.other_team = other_team
        self.other_team_points = other_team_points

        # sets the result equal to 1 if I won, 0 if I drew, and -1 if I lost
        if my_points > other_team_points:
            self.result = 1
        elif my_points < other_team_points:
            self.result = -1
        else:
            self.result = 0
    