from Casino_game import Player, Casino

Peppa_Pig = Player("Peppa Pig")
Suzy_Sheep = Player("Suzy Sheep")
Rebecca_Rabbit = Player("Rebecca Rabbit")
Miss_Rabbit = Player("Miss Rabbit")
Mrs_Donkey = Player("Mrs Donkey")
Zoe_Zebra = Player("Zoe Zebra")
Pedro_Pony = Player("Pedro Pony")

players = [Peppa_Pig, Suzy_Sheep, Rebecca_Rabbit,
           Miss_Rabbit, Mrs_Donkey, Zoe_Zebra, Pedro_Pony]

casino = Casino(players)


def test_game_results_calculation(monkeypatch):

    def arrange_dices_simple():
        # 0 (no pairs and no duplicates)
        Peppa_Pig.dice_arrangement = [1, 2, 4, 3]

    def arrange_dices_evens():
        Suzy_Sheep.dice_arrangement = [4, 2, 6, 2]  # 16 (because of evens)

    def arrange_dices_odds():
        Rebecca_Rabbit.dice_arrangement = [1, 3, 5, 1]  # 13 (because of odds)

    def arrange_dices_dublicates():
        Miss_Rabbit.dice_arrangement = [6, 4, 6, 4]  # 22 (because of evens)

    def arrange_dices_dublicates_evens():
        Mrs_Donkey.dice_arrangement = [6, 6, 6, 2]  # 24 (because of tripple 6)

    def arrange_dices_dublicates_odds():
        Zoe_Zebra.dice_arrangement = [5, 5, 5, 3]  # 21 (because of odds)

    def arrange_dices_24():
        # (same as Mrs_Donkey's score of 24 to check if it is a draw)
        Pedro_Pony.dice_arrangement = [4, 4, 4, 4]  # 24

    monkeypatch.setattr(
        Peppa_Pig, 'throw_dices', arrange_dices_simple)
    monkeypatch.setattr(
        Suzy_Sheep, 'throw_dices', arrange_dices_evens)
    monkeypatch.setattr(
        Rebecca_Rabbit, 'throw_dices', arrange_dices_odds)
    monkeypatch.setattr(
        Miss_Rabbit, 'throw_dices', arrange_dices_dublicates)
    monkeypatch.setattr(
        Mrs_Donkey, 'throw_dices', arrange_dices_dublicates_evens)
    monkeypatch.setattr(
        Zoe_Zebra, 'throw_dices', arrange_dices_dublicates_odds)
    monkeypatch.setattr(
        Pedro_Pony, 'throw_dices', arrange_dices_24)

    casino.play_game()

    assert Peppa_Pig.score == 0
    assert Suzy_Sheep.score == 16
    assert Rebecca_Rabbit.score == 13
    assert Miss_Rabbit.score == 22
    assert Mrs_Donkey.score == 24
    assert Zoe_Zebra.score == 21
    assert Pedro_Pony.score == 24


def test_game_winner(monkeypatch):

    def arrange_dices_simple():
        # 0 (no pairs and no duplicates)
        Peppa_Pig.dice_arrangement = [1, 2, 4, 3]

    def arrange_dices_evens():
        Suzy_Sheep.dice_arrangement = [4, 2, 6, 2]  # 16 (because of evens)

    def arrange_dices_odds():
        Rebecca_Rabbit.dice_arrangement = [1, 3, 5, 1]  # 13 (because of odds)

    def arrange_dices_dublicates():
        Miss_Rabbit.dice_arrangement = [6, 4, 6, 4]  # 22 (because of evens)

    def arrange_dices_dublicates_evens():
        Mrs_Donkey.dice_arrangement = [6, 6, 6, 2]  # 24 (because of tripple 6)

    def arrange_dices_dublicates_odds():
        Zoe_Zebra.dice_arrangement = [5, 5, 5, 3]  # 21 (because of odds)

    def arrange_dices_24():
        # (same as Mrs_Donkey's score of 24 to check if it is a draw)
        Pedro_Pony.dice_arrangement = [4, 4, 4, 4]  # 24

    monkeypatch.setattr(
        Peppa_Pig, 'throw_dices', arrange_dices_simple)
    monkeypatch.setattr(
        Suzy_Sheep, 'throw_dices', arrange_dices_evens)
    monkeypatch.setattr(
        Rebecca_Rabbit, 'throw_dices', arrange_dices_odds)
    monkeypatch.setattr(
        Miss_Rabbit, 'throw_dices', arrange_dices_dublicates)
    monkeypatch.setattr(
        Mrs_Donkey, 'throw_dices', arrange_dices_dublicates_evens)
    monkeypatch.setattr(
        Zoe_Zebra, 'throw_dices', arrange_dices_dublicates_odds)
    monkeypatch.setattr(
        Pedro_Pony, 'throw_dices', arrange_dices_24)

    casino.play_game()  # wins 24
    # Draw because Pedro_Pony and Mrs_Donkey have 24
    assert casino.game_result() == None
    casino.remove_player(Pedro_Pony)
    casino.play_game()
    assert casino.game_result() == Mrs_Donkey  # Now only Mrs_Donkey has 24
    casino.remove_player(Mrs_Donkey)
    casino.play_game()
    assert casino.game_result() == Miss_Rabbit  # Now only Miss_Rabbit has 22
    casino.add_player(Pedro_Pony)
    casino.play_game()
    assert casino.game_result() == Pedro_Pony  # Now only Pedro_Pony has 24


def test_no_winner(monkeypatch):

    def arrange_dices_simple():
        # 0 (no pairs and no duplicates)
        Peppa_Pig.dice_arrangement = [1, 2, 4, 3]

    def arrange_dices_evens():
        Suzy_Sheep.dice_arrangement = [4, 2, 6, 1]  # 0

    def arrange_dices_odds():
        Rebecca_Rabbit.dice_arrangement = [1, 3, 5, 2]  # 0

    def arrange_dices_dublicates():
        Miss_Rabbit.dice_arrangement = [2, 2, 6, 6]  # 18

    def arrange_dices_dublicates_evens():
        Mrs_Donkey.dice_arrangement = [3, 3, 3, 3]  # 18

    def arrange_dices_dublicates_odds():
        Zoe_Zebra.dice_arrangement = [1, 2, 3, 4]  # 0

    def arrange_dices_24():
        Pedro_Pony.dice_arrangement = [6, 5, 4, 3]  # 0

    monkeypatch.setattr(
        Peppa_Pig, 'throw_dices', arrange_dices_simple)
    monkeypatch.setattr(
        Suzy_Sheep, 'throw_dices', arrange_dices_evens)
    monkeypatch.setattr(
        Rebecca_Rabbit, 'throw_dices', arrange_dices_odds)
    monkeypatch.setattr(
        Miss_Rabbit, 'throw_dices', arrange_dices_dublicates)
    monkeypatch.setattr(
        Mrs_Donkey, 'throw_dices', arrange_dices_dublicates_evens)
    monkeypatch.setattr(
        Zoe_Zebra, 'throw_dices', arrange_dices_dublicates_odds)
    monkeypatch.setattr(
        Pedro_Pony, 'throw_dices', arrange_dices_24)

    casino.play_game()
    assert casino.game_result() == None
    casino.remove_player(Miss_Rabbit)
    casino.remove_player(Mrs_Donkey)
    casino.play_game()
    assert casino.game_result() == None
    casino.add_player(Mrs_Donkey)
    casino.play_game()
    assert casino.game_result() == Mrs_Donkey
