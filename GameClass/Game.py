import datetime

class Game:

    def __init__(self, day, month, day_number, year, start_time, home_team, home_points, visitor_team, visitor_points):
        self.game_datetime = datetime.datetime(year, month, day_number, start_time[0:1], start_time[:-2])
        
        self.home_team = home_team
        self.home_points = home_points
        self.visitor_team = visitor_team
        self.visitor_points = visitor_points