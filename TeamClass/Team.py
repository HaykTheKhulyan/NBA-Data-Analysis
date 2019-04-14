class Team:

    def __init__(self, name):
        self.name = name
        self.game_history = set()

        self.total_points = 0
        self.point_average = 0

        self.num_wins = 0
        self.num_losses = 0
        self.num_draws = 0
    
    def add_game(self, game):
        self.game_history.add(game)

        if game.result == 1:
            self.num_wins += 1
        elif game.result == -1:
            self.num_losses += 1
        else:
            self.num_draws += 1
        
        self.total_points += game.my_points
        self.point_average = self.total_points / len(self.game_history)

    def __str__(self):
        #print(f'Team: {self.name}')
        pass