import unittest

from yandex import create_folder, check_folder


class TestBookkeeping(unittest.TestCase):
    def setUp(self):
        tocken = input('Введите токен: ')
        oauth_tocken = ('OAuth ' + tocken)
        self.header = {'Authorization': oauth_tocken}
        self.folder = 'file'
        self.param = {"path": '/' + self.folder}


    def test_create_folder_positive(self):
        list_before_creation = []
        response_folder = check_folder(self.header, self.param)
        for element in response_folder['items']:
            list_before_creation.append(element['name'])
        self.assertNotIn(self.folder, list_before_creation)

        response = str(create_folder(self.header, self.param))
        self.assertEqual(response, '<Response [200]>')

        list_after_creation = []
        response_folder = check_folder(self.header, self.param)
        for element in response_folder['items']:
            list_after_creation.append(element['name'])
        self.assertIn(self.folder, list_before_creation)

    def test_create_folder_negative(self):
        response = str(create_folder(self.header, self.param))
        self.assertEqual(response, '<Response [409]>')

        list_of_folder = []
        response_folder = check_folder(self.header, self.param)
        for element in response_folder['items']:
            list_of_folder.append(element['name'])
        self.assertIn(self.folder, list_of_folder)


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()

