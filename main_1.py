from unittest import TestCase, mock, main

from app import get_doc_owner_name, add_new_doc, documents, directories, delete_doc


class TestBookkeeping(TestCase):
    def setUp(self):
        pass

    def test_get_doc_owner_name(self):
        with mock.patch('builtins.input', return_value='2207 876234'):
            self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')

    def test_add_new_doc(self):
        with mock.patch('builtins.input', side_effect=['passport', '1234 567890', 'Name', '6']):
            self.assertIn(add_new_doc(), directories)

    def test_delete_doc(self):
        with mock.patch('builtins.input', return_value='11-2'):
            doc_number, deleted = delete_doc()
            for current_document in documents:
                self.assertNotIn(doc_number, current_document['number'])

    def tearDown(self):
        pass



if __name__ == '__main__':
    main()


