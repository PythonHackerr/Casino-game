import random

DICE_AMOUNT = 4
ODDS_ONLY_BONUS = 3
EVENS_ONLY_BONUS = 2
PAIR_MULTIPLAYER = 2
THREE_MULTIPLAYER = 4
FOUR_MULTIPLAYER = 6


def calculate_score_by_duplicates(number, amount):
    if (amount == 2):
        return number * PAIR_MULTIPLAYER
    elif (amount == 3):
        return number * THREE_MULTIPLAYER
    elif (amount == 4):
        return number * FOUR_MULTIPLAYER
    else:
        return 0


class Player():

    def __init__(self, player_name):
        self.player_name = player_name
        self.dice_arrangement = []
        self.score = 0

    def throw_dices(self):
        self.dice_arrangement = []
        for i in range(DICE_AMOUNT):
            self.dice_arrangement.append(random.randint(1, 6))

    def calculate_result(self):
        score_by_duplicates = 0
        score_by_odd_even = 0
        start_division_remainder = -1
        give_odds_evens_bonus = True

        result_dict = dict([(i, self.dice_arrangement.count(i))
                           for i in set(self.dice_arrangement)])

        for number, amount in result_dict.items():
            score_by_duplicates += calculate_score_by_duplicates(
                number, amount)

        for dice_number in self.dice_arrangement:
            if (start_division_remainder == -1):
                start_division_remainder = dice_number % 2
            if (dice_number % 2 != start_division_remainder):
                give_odds_evens_bonus = False
            score_by_odd_even += dice_number
        if (give_odds_evens_bonus == True):
            if (start_division_remainder == 1):
                score_by_odd_even += ODDS_ONLY_BONUS
            else:
                score_by_odd_even += EVENS_ONLY_BONUS
        else:
            score_by_odd_even = 0
        self.score = max(score_by_odd_even, score_by_duplicates)
        return max(score_by_odd_even, score_by_duplicates)


class Casino():

    def __init__(self, players):
        self.players = players
        self.game_winner = None

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def play_game(self):
        for player in self.players:
            player.throw_dices()
            player.calculate_result()

    def game_result(self):
        largest_score = 0
        for player in self.players:
            if (player.calculate_result() > largest_score):
                largest_score = player.calculate_result()
                game_winner = player

        players_score_list = []
        for player in self.players:
            players_score_list.append(player.score)
        sorted_player_scores = sorted(players_score_list)

        second_largest_score = sorted_player_scores[-2]

        if (largest_score == second_largest_score):
            game_winner = None
        return game_winner
