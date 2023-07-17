import unittest
from models.base import Base


class BaseTest(unittest.TestCase):

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)

        json_string = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary(), b3.to_dictionary()])
        expected_json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        self.assertEqual(json_string, expected_json_string)

        empty_list_json_string = Base.to_json_string([])
        self.assertEqual(empty_list_json_string, "[]")

        none_json_string = Base.to_json_string(None)
        self.assertEqual(none_json_string, "[]")

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(len(list_objs), 3)
        self.assertEqual(list_objs[0].id, 1)
        self.assertEqual(list_objs[1].id, 2)
        self.assertEqual(list_objs[2].id, 3)

        empty_list_json_string = "[]"
        empty_list_objs = Base.from_json_string(empty_list_json_string)
        self.assertEqual(len(empty_list_objs), 0)

        none_json_string = ""
        none_list_objs = Base.from_json_string(none_json_string)
        self.assertEqual(len(none_list_objs), 0)

    def test_create(self):
        b1 = Base.create(id=1)
        self.assertEqual(b1.id, 1)

        b2 = Base.create()
        self.assertEqual(b2.id, 1)

        b3 = Base.create(id=10, dummy_attr="dummy")
        self.assertEqual(b3.id, 10)

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        Base.save_to_file([b1, b2, b3])

        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 3)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[2].id, 3)

        empty_list_loaded_objs = Base.load_from_file()
        self.assertEqual(len(empty_list_loaded_objs), 0)

    def test_save_to_file_csv(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        Base.save_to_file_csv([b1, b2, b3])

        with open("Base.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 4)  # Header + 3 object lines

        empty_list_file = open("Base.csv", "w")
        empty_list_file.close()

    def test_load_from_file_csv(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        Base.save_to_file_csv([b1, b2, b3])

        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 3)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[2].id, 3)

        empty_list_loaded_objs = Base.load_from_file_csv()
        self.assertEqual(len(empty_list_loaded_objs), 0)

        empty_list_file = open("Base.csv", "w")
        empty_list_file.close()

if __name__ == '__main__':
    unittest.main()
