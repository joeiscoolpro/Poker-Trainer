class Card:
    """
    Playing cards used in 52 card decks

    === Attributes ===
    value: the value of the card, 2-10 (inclusive), jack, queen, king, or ace
    suit: the suit of the card, spades, clubs, diamonds, hearts

    === Representation Invariants ===
    - 1 <= value <= 13
    - suit in ["s", "c", "h", "d"]
    """
    _value: int
    _suit: str
    _is_hidden: bool

    def __init__(self, value: int, suit: str, is_hidden: bool = True) -> None:
        if suit not in ['s', 'c', 'd', 'h']:
            raise InvalidSuit()
        if not 1 <= value <= 13:
            raise InvalidValue()
        self._value = value
        self._suit = suit
        self._is_hidden = is_hidden

    def __str__(self):
        return f'{str(self._value)}{self._suit} is_hidden={self._is_hidden}'

    def flip_card(self) -> None:
        self._is_hidden = not self._is_hidden

    def val(self) -> int:
        return self._value

    def suit(self) -> str:
        return self._suit

    def check_hidden(self) -> bool:
        return self._is_hidden

class InvalidSuit(Exception):
    def __init__(self):
        super().__init__(self, "Invalid card suit when initializing Card, not of format 's', 'c', 'd', or 'h'")

class InvalidValue(Exception):
    def __init__(self):
        super().__init__(self, "Invalid card value passed when initializing Card, not int value from [1, 13]")

if __name__ == '__main__':
    card = Card(0, "d")
    print(card)
