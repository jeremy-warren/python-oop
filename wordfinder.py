"""Word Finder: finds random words from a dictionary."""
import random

words = open('words.txt', 'r')
allWords = words.read()


class WordFinder:
    """class that finds a random word from the words.txt file"""

    def findWord():
        """prints a random word in words.txt"""
        print(random.choice(allWords))
