class Team:

    def __init__(self, input_name, input_player, input_coach):
         self.name = input_name
         self.players = input_player
         self.coach = input_coach
         self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, player):
        for play in self.players:
            if play == player:
                return True
        return False
    
    def play_game(self, game):
        if game == True: 
            self.points += 3

