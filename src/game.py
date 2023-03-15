import random

class Game:
    """Simulates a single game between two opponents"""

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.winner = None

    def calculate_winner(self):
        """Sets self.winner to the winner and returns the winner"""

        home_win_probability = self.get_team_win_probability(self.home_team)
        away_win_probability = self.get_team_win_probability(self.away_team)

        if home_win_probability > away_win_probability:
            self.winner = self.home_team
        elif away_win_probability > home_win_probability:
            self.winner = self.away_team
        else:
            self.winner = self.__calculate_tie_breaker()

        return self.winner

    def __calculate_tie_breaker(self):
        tie_breaker = random.randint(0, 100)
        if tie_breaker > 50:
            return self.home_team
        return self.away_team

    def get_team_win_probability(self, team):
        team_str_length = len(team)
        random.seed(team_str_length)
        return random.randint(0, 100)
