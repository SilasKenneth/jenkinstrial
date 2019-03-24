import unittest
from app.operations import add

class TestAddition(unittest.TestCase):
	def test_correct_for_numbers(self):
		self.assertEqual(add(2,3), 5)
	def test_add_plus_zero(self):
		self.assertEqual(add(0, 3), 3)
	def test_can_add_strings(self):
		self.assertEqual(add('s', 's'), 'ss')
	def test_correct_for_decimals(self):
		self.assertEqual(add(1, 0.45), 1.45)

	def test_fails_for_unmatching_types(self):
		self.assertEqual(add('s', 19), 0)