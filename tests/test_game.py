# tests/test_game.py
from longest_word.game import Game
class TestGame:
    def test_game_initialization(self):
        game = Game()
        assert type(game.grid) == list


    def test_set_grid(self):
        game = Game()
        game.set_grid(["a", "b"])
        assert game.grid == ["a", "b"]

    def test_is_valid(self):
        game = Game()
        game.set_grid(["a", "b"])
        assert game.is_valid("x") == False
        assert game.is_valid("a") == True
