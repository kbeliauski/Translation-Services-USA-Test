import unittest
from src import *


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"id": 1, "create": "14.04.2023", "title": "array1"},
            {"id": 4, "create": "09.02.2023", "title": "array4"},
            {"id": 2, "create": "03.07.2023", "title": "array2"},
            {"id": 1, "create": "22.04.2023", "title": "array1"},
            {"id": 4, "create": "12.12.2023", "title": "array4"},
            {"id": 3, "create": "04.04.2023", "title": "array3"}
        ]
        self.empty_data = []
        self.null_data = None
        self.missing_id_data = [
            {"create": "14.04.2023", "title": "array1"},
            {"id": 2, "create": "12.12.2023", "title": "array4"}
        ]

    def test_filter_unique_records(self):
        unique_records = filter_unique_records(self.sample_data)
        self.assertEqual(len(unique_records), 4)
        self.assertEqual(unique_records[0]['id'], 4)
        self.assertEqual(unique_records[1]['id'], 3)
        self.assertEqual(unique_records[2]['id'], 2)
        self.assertEqual(unique_records[3]['id'], 1)
        
    def test_filter_unique_records_empty(self):
        with self.assertRaises(ValueError):
            filter_unique_records(self.empty_data)

    def test_filter_unique_records_none(self):
        with self.assertRaises(ValueError):
            filter_unique_records(self.null_data)  # Should raise ValueError

    def test_filter_unique_records_missing_id(self):
        with self.assertRaises(KeyError):
            filter_unique_records(self.missing_id_data)  # Should raise KeyError

    def test_sort_array_by_key(self):
        # Not checking the actual creation time here, just the string.
        sorted_array = sort_array_by_key(self.sample_data, "create")
        self.assertEqual(sorted_array[0]["title"], "array2")
        self.assertEqual(sorted_array[-1]["title"], "array1")

    def test_sort_array_by_key_empty(self):
        with self.assertRaises(ValueError):
            sort_array_by_key(self.empty_data, "create")

    def test_filter_by_condition(self):
        filtered = filter_by_condition(self.sample_data, "id", 2)
        self.assertEqual(len(filtered), 1)  # Should return 1 records
        self.assertTrue(all(item['id'] == 2 for item in filtered))

    def test_filter_by_condition_not_found(self):
        filtered = filter_by_condition(self.sample_data, "id", 999)
        self.assertEqual(filtered, [])  # No records should match

    def test_filter_by_condition_empty(self):
        with self.assertRaises(ValueError):
            filter_by_condition(self.empty_data, "id", 1)

    def test_transform_to_key_value(self):
        transformed = transform_to_key_value(self.sample_data)
        self.assertEqual(transformed["array1"], 1)
        self.assertEqual(transformed["array4"], 4)

    def test_transform_to_key_value_empty(self):
        with self.assertRaises(ValueError):
            transform_to_key_value(self.empty_data)

    def test_transform_to_key_value_missing_title(self):
        with self.assertRaises(KeyError):
            transform_to_key_value(self.missing_id_data)


if __name__ == "__main__":
    unittest.main()
