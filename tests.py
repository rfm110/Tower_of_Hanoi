import unittest
from tower_of_hanoi_manual import move_is_legal
from recursive_tower_of_hanoi import recursive_tower_of_hanoi


class TestHanoi(unittest.TestCase):

    selection_dictionary = {1: [4, 3, 2, 1],
                            2: [],
                            3: []}

    def test_rejection(self):
        expected_result = False
        self.selection_dictionary[1] = [4, 3, 2]
        self.selection_dictionary[3] = [1]
        disk_from = 1
        disk_to = 3
        actual_result = move_is_legal(self.selection_dictionary, disk_from, disk_to)
        self.assertTrue(expected_result-actual_result == 0)

    def test_ordering_acceptance(self):
        expected_result = True
        self.selection_dictionary[1] = [4, 3, 1]
        self.selection_dictionary[3] = [2]
        disk_from = 1
        disk_to = 3
        actual_result = move_is_legal(self.selection_dictionary, disk_from, disk_to)
        self.assertTrue(expected_result-actual_result == 0)

    def test_empty_rod_acceptance(self):
        expected_result = True
        self.selection_dictionary[1] = [4, 3, 2, 1]
        self.selection_dictionary[3] = []
        disk_from = 1
        disk_to = 3
        actual_result = move_is_legal(self.selection_dictionary, disk_from, disk_to)
        self.assertTrue(expected_result-actual_result == 0)

    def test_recursive(self):
        pin_1, pin_2, pin_3 = ([4, 3, 2, 1], [], [])
        recursive_tower_of_hanoi(pin_1, pin_2, pin_3, 4)
        self.assertTrue(pin_3 == [4, 3, 2, 1])

if __name__ == "__main__":
    unittest.main()
