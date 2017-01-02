__author__ = 'Narendra'

notes = '''
This assignment requires you to use all that you have learnt to write elegant and compact code to build up this project,
we will add more requirement to this project every day.

1. Download the english word list from http://dreamsteep.com/projects/the-english-open-word-list.html and unzip it
   to some directory. You will see a list of word files in your directory. for e.g C:\work\EOWL-words\LF Delimited Format

2. Take the directory above as an argument to this program when you run it from command line (as python project_01.py <root>)

3. Read all the *words.txt files and populate words from each into a single list. As you read each file, print out the
   number of words in each file. Finally print out the total number of words read. These should match the counts mentioned
   in the above url.

4. We will extend this module to do many things over the next few days.

'''

import sys
import os

path = '/home/narendra/github/Piazza-Python-Course/projects/EOWL/LF Delimited Format/'

#returns a merged list of all words
def load_words(base_dir):
    all_words = []
    for file in os.listdir(base_dir):
        if file.endswith(".txt"):
            print file
            data = open(path + file)
            read_data = data.read()
            words_lines = read_data.splitlines()
        all_words += words_lines

    return all_words


def main(argv = sys.argv):
    # add arguments checks here...

    words = load_words(sys.argv[1])
    # words = load_words(path)
    assert "apple" in words
    assert 128985 == len(words)


if __name__ == "__main__":
    main()
