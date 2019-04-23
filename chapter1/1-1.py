"""
通过重写__len__() 和 __getitem__() 来实现对特定对象执行len()和[]操作
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
