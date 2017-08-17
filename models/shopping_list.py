import sys

sys.path.append('..')

class ShoppingList(object):
    def __init__(self, name, items):
        self.name = name
        self.description = ''
        self.items = []

    def __repr__(self):
        return 'Shopping list: ' + name + ', '.join(item for item in self.items)
