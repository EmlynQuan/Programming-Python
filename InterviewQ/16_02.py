# coding=utf-8

import collections

class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        self.hashMap = collections.Counter(book)

    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.hashMap[word]

