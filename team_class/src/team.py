class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        # self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
            else:
                return False

   
   # solution from classnotes
    # def has_players(self, players):
    #     return self.players.count(players) > 0

    #     if (self.players.count(player) > 0):
    #         return True
    #     else:
    #         return False

# def play_game(self, game_won):
#     if game_won:
#         self.points += 3