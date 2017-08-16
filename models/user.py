from shopping_list import ShoppingList
from list_item import ListItem


class User(object):

    def __init__(self):
        self.shopping_lists = {}

    def create_shopping_list(self, name, *items):
        '''
        method creates shopping list and allows users to add an item or multiple items to the list
        '''
        items = list(items)
        if name not in self.shopping_lists.keys():
            shop_list = ShoppingList(name, items)
            for item in items:
                new_item = ListItem(item)
            self.shopping_lists[name] = [item for item in items]
        elif name in self.shopping_lists.keys():
            return 'Shopping List already exists!'
        return self.shopping_lists

    def read_list(self, name):
        '''
        Returns items from specified list
        '''
        items = []
        if name in self.shopping_lists.keys():
            items = [item for item in self.shopping_lists[name]]
        return items

    def update_shopping_list(self, list_name, new_name):
        '''
        creates shopping list name
        '''
        if list_name in self.shopping_lists.keys():
            # new_name = ShoppingList.name
            self.shopping_lists[new_name] = self.shopping_lists.pop(list_name)
        else:
            return "list name does not exist here"
        return self.shopping_lists

    def update_shopping_list_item(self, list_name, item_name, new_name):
        '''
        creates shopping list name
        '''
        if list_name in self.shopping_lists.keys():
            for item in self.shopping_lists[list_name]:
                if item == item_name:
                    self.shopping_lists[list_name].remove(item)
                    self.shopping_lists[list_name].append(new_name)
                else:
                    return 'Item not in list'
        else:
            return "list name doesn't exist"
        return self.shopping_lists

    def delete_shopping_list(self, list_name):
        '''
        deletes shopping list
        '''
        if list_name in self.shopping_lists.keys():
            del self.shopping_lists[list_name]
        else:
            return 'List name does not exist in the system'
        return self.shopping_lists

    def add_shopping_list_item(self, list_name, *items):
        '''
        method adds shopping list items
        '''
        items = list(items)
        if list_name in self.shopping_lists.keys():
            for item in items:
                if item not in self.shopping_lists[list_name]:
                    self.shopping_lists[list_name].append(item)
        else:
            if list_name not in self.shopping_lists:
                for item in items:
                    self.shopping_lists[list_name] = [item for item in items]

    def delete_shopping_list_item(self, list_name, item):
        '''
        method deletes item in a shopping list
        '''
        if item in self.shopping_lists[list_name]:
            self.shopping_lists[list_name].remove(item)
        else:
            return 'item not in list'
        return self.shopping_lists

    def __repr__(self):
        return 'user shopping lists are: ' + ', '.join(name for name in self.shopping_lists)
