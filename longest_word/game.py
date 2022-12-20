import string
import random

def by_letter_count(string):
    by_letter_count  = {}
    for letter in string :
        count = by_letter_count.get(letter, 0) + 1
        by_letter_count[letter] = count
    return by_letter_count



class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        grid = []
        for i in range(0,8) :
            letter = random.choice(string.ascii_letters).lower()
            grid.append(letter)
        self.set_grid(grid)

    def set_grid(self, grid):
        self.grid = grid
        self.by_letter_count = by_letter_count(grid)


    def is_valid(self, word: str) -> bool:

        tested_word_by_letter_count=   by_letter_count(word)
        result = True
        for letter, count in tested_word_by_letter_count.items():
            result = result & self.by_letter_count.get(letter, 0) >= count

        return result
