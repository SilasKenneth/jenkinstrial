import unittest
from app.operations import multiply


class TestMultiply(unittest.TestCase):
	def test_correct_for_numbers(self):
		self.assertEqual(multiply(2,3), 6)
	def test_multiply_by_zero(self):
		self.assertEqual(multiply(0, 3), 0)
	def test_can_duplicate_strings(self):
		self.assertEqual(multiply('s', 4), 'ssss')

	def test_fails_for_unmatching_types(self):
		self.assertEqual(multiply('a', 'a'), 0)