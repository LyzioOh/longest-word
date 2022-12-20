# tests/test_game.py
from longest_word.game import Game
class TestGame:
    def test_game_initialization(self):
        game = Game()
        assert type(game.grid) == list


    def test_set_grid(self):
        game = Game()
        game.set_grid(["a", "b"])
        assert game.grid == ["A", "B"]

    def test_is_valid(self):
        game = Game()
        game.set_grid(["a", "b"])
        assert game.is_valid("x") == False
        assert game.is_valid("A") == True

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.set_grid(list('KWIENFUQW')) # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
