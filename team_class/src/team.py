class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
            else:
                return False
