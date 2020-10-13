"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = [self.flavor, self.price]

    def add_stock(self, amount):
        self.qty = self.qty + amount
        return self.qty

    def sell(self, amount):
        while (self.qty - amount) >= 0:
            if self.qty == 0:
                print('Sorry, these cupcakes are sold out')
            else:
                self.qty -= amount
            else:
                print("nope")
            break
        
    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
