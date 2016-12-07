__author__ = 'Narendra'

notes = '''
This assignment covers comprehensions.
See: http://en.wikipedia.org/wiki/Scrabble_letter_distributions for more scrabble information.
'''

from placeholders import *

scrabble_scores = [(1, "EAOINRTLSU"), (2, "DG"), (3, "BCMP"),
                   (4, "FHVWY"), (5, "K"), (8, "JX"), (10, "QZ")]


#return a dict which contains a letter to score mapping.
#use dict comprehensions
def get_scrabble_scorer():
    score_dict = {}
    for score in scrabble_scores:
        score_num, score_word = score
        for char in score_word:
            score_dict[char] = score_num
    return score_dict


def test_scrabble_scorer():
    score_dict = get_scrabble_scorer()
    for score, letters in scrabble_scores:
        for letter in letters:
            assert score == score_dict.get(letter)


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___