from Card import Card
from random import shuffle
from collections import deque

class Deck:
    """
    Deck of 52 cards

    === Attributres ===

    === Representation Invariants ===
    - The leftmost card is the top and the rightmost card is the bottom
    """
    _cards: [Card]
    def __init__(self):
        self._cards = deque()
        self._populate_cards()

    def __str__(self):
        s = []
        for i in range(len(self._cards)):
            s.append(f'{self._cards[i].val()}{self._cards[i].suit()} hidden={self._cards[i].check_hidden()}')
        return "[" +  ", ".join(s) + "]\n" + f"{len(self._cards)} cards."


    def shuffle_cards(self) -> None:
        """
        Rearrange positions of each card randomly
        """
        shuffle(self._cards)

    def check_top(self) -> Card:
        return self._cards[0]

    def get_top(self) -> Card:
        return self._cards.popleft()

    def _populate_cards(self) -> None:
        """
        Add 52 unique cards to deck
        """
        for suit in ['s', 'c', 'd', 'h']:
            for value in range(1, 14):
                self._cards.append(Card(value, suit))


if __name__ == '__main__':
    deck1 = Deck()
    print(deck1)
    deck1.shuffle_cards()
    print(deck1)
