import unittest
from models.user import User


class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_shopping_list_initialy_empty(self):
        self.assertEqual(self.user.shopping_lists, {})

    def test_create_shopping_list_successfully(self):
        initial_room_count = len(self.user.shopping_lists)
        cuttlery_list = self.user.create_shopping_list('Cuttlery')
        self.assertTrue(cuttlery_list)
        new_room_count = len(self.user.shopping_lists)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_shopping_list_when_list_already_exists(self):
        self.user.shopping_lists = {'Shoes': ['flats']}
        self.assertEqual(self.user.create_shopping_list('Shoes', 'flats'),
                         'Shopping List already exists!', msg='Shopping List already exists!')

    def test_update_shopping_list(self):
        self.user.shopping_lists = {'shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list(
            'shoes', 'flat_shoes'), {'flat_shoes': ['flats']})

    def test_updating_non_existing_shopping_list(self):
        self.user.shopping_lists = {'Shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list('Shoe', 'flats'),
                         'list name does not exist here', msg='list name does not exist here')

    def test_update_shopping_list_item(self):
        self.user.shopping_lists = {'shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list_item(
            'shoes', 'flats', 'flat'), {'shoes': ['flat']})

    def test_updating_non_existing_shopping_list_item(self):
        self.user.shopping_lists = {'Shoes': ['flats']}
        self.assertEqual(self.user.update_shopping_list_item('Shoes', 'flas', 'flat'),
                         'Item not in list', msg='Item not in list')

    def test_read_shopping_list_items(self):
        self.user.shopping_lists = {'shoes': ['flats', 'highs']}
        self.assertEqual(self.user.read_list('shoes'), ['flats', 'highs'])

    def test_delete_shopping_list(self):
        self.user.shopping_lists = {'shoes': ['flats', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list(
            'shoes'), {'grocery': ['onions', 'tomatoes']})

    def test_delete_shopping_list_item(self):
        self.user.shopping_lists = {'shoes': ['flats', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list_item('shoes', 'flats'), {
                         'shoes': ['highs'], 'grocery': ['onions', 'tomatoes']})
