class User(object):
    '''
    hhhghghh
    '''

    def __init__(self):
        self.shopping_lists = {}

    def create_shopping_list(self, name):
        '''
        creates shopping list
        '''
        if name not in self.shopping_lists:
            #shop_list = ShoppingList(name, description)
            self.shopping_lists[name] = []
        elif name in self.shopping_lists:
            return 'Shopping List already exists'
        return self.shopping_lists

    def read_list(self, name):
        '''
        Returns items from specified list
        '''
        if name in self.shopping_lists:
            for item in self.shopping_lists[name]:
                print(item)

    def update_shopping_list(self, list_name, new_name):
        '''
        creates shopping list name
        '''
        if list_name in self.shopping_lists:
            #new_name = ShoppingList.name
            self.shopping_lists[new_name] = self.shopping_lists.pop(list_name)
        else:
            return "list name doesn't exist"

    def delete_shopping_list(self, list_name):
        '''
        deletes shopping list
        '''
        if list_name in self.shopping_lists:
            del self.shopping_lists[list_name]
        else:
            return 'List name does not exist in the system'
        return self.shopping_lists

    def create_shopping_list_item(self, list_name, *items):
        '''
        creates shopping list items
        '''
        items = list(items)
        if list_name in self.shopping_lists:
            for item in items:
                self.shopping_lists[list_name].append(item)
        else:
            if list_name not in self.shopping_lists:
                self.shopping_lists[list_name] = []
                for item in items:
                    self.shopping_lists[list_name].append(item)

#
# def main():
#     user1 = User()
#     user1.create_shopping_list('food')
#     print(user1.shopping_lists)
#     user1.create_shopping_list_item('food', 'tomato', 'carrot', 'onion')
#     print(user1.shopping_lists)
#     user1.create_shopping_list_item('sheets', 'bed', 'chair', 'sofa')
#     print(user1.shopping_lists)
#     user1.delete_shopping_list('sheets')
#     print(user1.shopping_lists)
#     user1.update_shopping_list('food', 'food_stuffs')
#     print(user1.shopping_lists)
#
#
# if __name__ == '__main__':
#     main()
