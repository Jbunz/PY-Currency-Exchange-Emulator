class Currency:

    currencies = {
        'CHF': 0.930023,  # Swiss franc
        'CAD': 1.264553,  # Canadian dollar
        'GBP': 0.737414,  # British pound
        'JPY': 111.019919,  # Japanese yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0  # US dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        Changes the Currency object's unit from self.unit to new_unit.
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        """
        Defines the '+' operator.
        If other is a Currency object, the currency values are added,
        and the result will be in the unit of self.
        If other is an int or a float, other will be treated as a USD value.
        """
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value + x, self.unit)

    def __iadd__(self, other):
        """
        Similar to __add__ but modifies self in-place.
        """
        if isinstance(other, (int, float)):
            self.value += other * Currency.currencies[self.unit]
        else:
            self.value += other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return self

    def __radd__(self, other):
        """
        Defines the behavior of the '+' operator when Currency object is on the right-hand side.
        """
        res = self + other
        if res.unit != "USD":
            res.changeTo("USD")
        return res

    def __sub__(self, other):
        """
        Defines the '-' operator.
        If other is a Currency object, the currency values are subtracted,
        and the result will be in the unit of self.
        If other is an int or a float, other will be treated as a USD value.
        """
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        """
        Similar to __sub__ but modifies self in-place.
        """
        if isinstance(other, (int, float)):
            self.value -= other * Currency.currencies[self.unit]
        else:
            self.value -= other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return self

    def __rsub__(self, other):
        """
        Defines the behavior of the '-' operator when Currency object is on the right-hand side.
        """
        res = other - self.value
        if self.unit != "USD":
            res = Currency(res, "USD")
        return res


# Example usage:
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")

print(v1 + v2)  # Output: 41.21 EUR
print(v2 + v1)  # Output: 43.34 USD
print(v1 + 3)   # Output: 26.28 EUR
print(3 + v1)   # Output: 26.28 EUR
print(v1 - 3)   # Output: 20.43 EUR
print(30 - v2)  # Output: 10.03 USD