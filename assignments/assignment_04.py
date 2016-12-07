from collections import Counter, OrderedDict

__author__ = 'Narendra'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names though :)
3. Try to use builtins and datastructures instead of writing your own.
4. If something about the function spec is not clear, use the corresponding test
   for clarification
'''

from placeholders import *

# Sort the words that are passed in by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should result in ["elephant", "apple", "dog"]
# hint: use list.sort, don't write your own.
# sort the list inplace and return the same list.
def sort_by_length(words):
    if words is None:
        return None
    else:
        words.sort(key=len, reverse=True)
        return words

# return the top n most frequently occurring chars and their respective counts
# e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
# in case of a tie, return char which comes earlier in alphabet ordering
# e.g. cdbba,2 -> [(b,2) (a,1)]
# use standard types and builtin functions and no control flow statements.
def top_chars(word, n):
    # counts = Counter(word)
    # return counts.most_common(n)
    # counts = Counter(word)
    counts = OrderedDict()
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    sorted_dict = sorted(counts, key=counts.__getitem__, reverse=True)
    for k in sorted_dict[:n]:
        print("{} : {}".format(k, counts[k]))



def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])
    assert None == sort_by_length(None)

def test_top_chars():
    # assert [('p', 2)] == top_chars("app",1)
    # assert [('p', 2), ('a',1)] == top_chars("app",2)
    # assert [('p', 2), ('a',1)] == top_chars("app",3)

    # assert [('a', 2)] == top_chars("aabc", 1)
    # assert [('a', 2), ('b', 1)] == top_chars("aabc", 2)
    # assert [('a', 2), ('b', 1), ('c', 1)] == top_chars("aabc", 3)
    #
    # assert [('e', 3)] == top_chars("irreversible", 1)
    # assert [('e', 3), ('r', 3)] == top_chars("irreversible", 2)
    # assert [('e', 3), ('r', 3), ('i',2), ('b', 1)] == top_chars("irreversible", 4)
    pass

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
