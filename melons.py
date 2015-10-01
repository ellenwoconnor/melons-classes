"""This file should have our melon-type classes in it."""

from data import melons as melons_data

BASE_PRICE = 5.0
print melons_data

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        if qty >= 3:
            total = qty * 5.0 * 0.75
        else:
            total = qty * 5.0

        return total # TODO, calculate the real amount!


class Cantaloupe(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        if qty >= 5:
            total = qty * 5.0 * 0.5
        else:
            total = qty * 5.0

        return total # TODO, calculate the real amount!

class Casaba(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * (5.0 + 1) * 1.5)

        return total # TODO, calculate the real amount!

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * 5.0 * 1.5)

        return total # TODO, calculate the real amount!

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * 5.0  * 1.5)

        return total # TODO, calculate the real amount!

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = qty * 5.0

        return total # TODO, calculate the real amount!

class HornedMelonOrder(object):
    species = "Horned_Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * 5.0  * 1.5)

        return total # TODO, calculate the real amount!


class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * 5.0  * 2 * 1.5)

        return total # TODO, calculate the real amount!

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
    
        total = (qty * (5.0 +1))

        return total # TODO, calculate the real amount!















