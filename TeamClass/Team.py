class Team:

    def __init__(self, name):
        self.name = name
        self.game_history = set()
    
    def add_game(self, game):
        self.game_history.add(game)
