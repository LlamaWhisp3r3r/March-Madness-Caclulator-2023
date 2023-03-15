from game import Game
import pprint

class Bracket:

    def __init__(self, list_of_teams):
        self.__size = len(list_of_teams)
        self.__teams = list_of_teams
        self.bracket = {'Round 1': {}}
        self.__create_bracket()
        self.__current_round_number = 1

    def __create_bracket(self):
        round_1_bracket = self.bracket['Round 1']
        if self.__size % 2 == 0:
            previous_team = None
            for i in range(1, self.__size+1):
                if i % 2 == 0:
                    round_1_bracket[f'Game {int(i/2)}'] = [previous_team, self.__teams[i-1]]
                else:
                    previous_team = self.__teams[i-1]
        else:
            raise SyntaxError('Bracket size has to be even number')

    def calculate_next_round(self):
        round_label = f'Round {self.__current_round_number}'
        next_round_label = f'Round {self.__current_round_number+1}'
        next_round_games = {}
        count = 1
        previous_winner = None
        for game_number, teams in self.bracket[round_label].items():
            team1 = teams[0]
            team2 = teams[1]
            game = Game(team1, team2)
            winner = game.calculate_winner()
            if count % 2 == 0:
                next_round_games[f'Game {int(count/2)}'] = [previous_winner, winner]
            else:
                previous_winner = winner
            count += 1

        self.bracket[next_round_label] = next_round_games
        self.__current_round_number += 1

    def calculate_winner_of_bracket(self):
        # Make this a dynamic discovery of the least dividable number
        total_rounds = int(len(self.bracket['Round 1']) / 2)
        for i in range(total_rounds-1):
            self.calculate_next_round()

        final_teams = self.bracket[f'Round {total_rounds}']['Game 1']
        game = Game(final_teams[0], final_teams[1])
        final_winner = game.calculate_winner()
        self.bracket['Winner'] =  final_winner
        return final_winner


if __name__ == '__main__':
    south_bracket_teams = ['Alabama', 'Texas A&M-CC', 'Maryland', 'West Virginia', 'San Diego St.', 'Charleston',
                           'Virginia', 'Furman', 'Creighton', 'NC State', 'Baylor', 'UCSB', 'Missouri', 'Utah St.',
                           'Arizona', 'Princeton']
    south_bracket = Bracket(south_bracket_teams)
    south_bracket_winner = south_bracket.calculate_winner_of_bracket()
    # pprint(south_bracket.bracket)
    pprint.pprint(south_bracket.bracket)

    east_bracket_teams = ['Purdue', 'Texas Southern/FDU', 'Memphis', 'Florida Atlantic', 'Duke', 'Oral Roberts',
                          'Tennessee', 'Louisiana', 'Kentucky', 'Providence', 'Kansas St.', 'Montana St.',
                          'Michigan St.', 'USC', 'Marquette', 'Vermont']
    east_bracket = Bracket(east_bracket_teams)
    east_bracket_winner = east_bracket.calculate_winner_of_bracket()
    pprint.pprint(east_bracket.bracket)

    midwest_bracket_teams = ['Houston', 'Northern Ky.', 'Iowa', 'Auburn', 'Miami (FL)', 'Drake', 'Indiana', 'Kent St.',
                             'Iowa St.', 'Pittsburgh', 'Xavier', 'Kennesaw St.', 'Texas A&M', 'Penn St.', 'Texas',
                             'Colgate']
    midwest_bracket = Bracket(midwest_bracket_teams)
    midwest_bracket_winner = midwest_bracket.calculate_winner_of_bracket()
    pprint.pprint(midwest_bracket.bracket)

    west_bracket_teams = ['Kansas', 'Howard', 'Arkansas', 'Illinois', 'Saint Mary\'s', 'VCU', 'UConn', 'Iona', 'TCU',
                          'Arizona St./Nevada', 'Gonzaga', 'Grand Canyon', 'Northwestern', 'Boise St.', 'UCLA',
                          'UNC Asheville']
    west_bracket = Bracket(west_bracket_teams)
    west_bracket_winner = west_bracket.calculate_winner_of_bracket()
    pprint.pprint(west_bracket.bracket)

    # print(f'South: {south_bracket_winner}\nEast: {east_bracket_winner}\nMidwest: {midwest_bracket_winner}\nWest:'
    #       f' {west_bracket_winner}')

    south_east_winner = Game(south_bracket_winner, east_bracket_winner).calculate_winner()
    midwest_west_winner = Game(midwest_bracket_winner, west_bracket_winner).calculate_winner()
    print(f'\nFinals: {south_east_winner} vs {midwest_west_winner}\n')

    import random
    random.seed(len(south_east_winner))
    south_east_winner_score = random.randint(50, 120)
    random.seed(len(midwest_west_winner))
    midwest_west_winner_score = random.randint(50, 120)


    final_winner = Game(south_east_winner, midwest_west_winner).calculate_winner()
    print(f'March Madness Winner: {final_winner}\nScore: \n{south_east_winner}: {south_east_winner_score}\n{midwest_west_winner}: {midwest_west_winner_score}')

