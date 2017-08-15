import unittest

class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_shopping_list_initialy_empty(self):
        self.assertEqual(self.shop.shopping_lists, {})

    def test_create_shopping_list_successfully(self):
        initial_room_count = len(self.user.shopping_lists)
        cuttlery_list = self.user.create_shopping_list('Cuttlery', 'fork')
        self.assertTrue(cuttlery_list)
        new_room_count = len(self.user.shopping_list)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_shopping_list_when_list_already_exists(self):
        self.user.shopping_list = {'Shoes': ['flats']}
        self.assertEqual(self.user.create_shopping_list('Shoe', 'flats'),
                         'list already exists!', msg='list already exists!')

    def test_update_shopping_list(self):
        self.user.shopping_list = {'shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list(
            'shoes', 'flat_shoes'), {'flat_shoes': ['flats']})

    def test_update_shopping_list_item(self):
        self.user.shopping_list = {'shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list_item('flats', 'flat'), {'shoes': ['flat']})

    def test_read_shopping_list_items(self):
        self.user.shopping_list = {'shoes': ['flats', 'highs']}
        self.assertEqual(self.user.print_shopping_list('shoes'), ['flats', 'highs'])

    def test_delete_shopping_list(self):
        self.user.shopping_list = {'shoes': ['flats', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list(
            'shoes'), {'grocery': ['onions', 'tomatoes']})

    def test_delete_shopping_list_item(self):
        self.user.shopping_list = {'shoes': ['flats', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list('shoes', 'flats'), {
                         'shoes': ['highs'], 'grocery': ['onions', 'tomatoes']})
