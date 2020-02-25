# John Hrabar
# Assignment 1
# I Pledge My Honor That I Have Abided By The Stevens Honor System
# This program will use pytest to test the classify_triangle program

from classify_triangle import *
import unittest
from math import sqrt

class TestTriangle(unittest.TestCase):
	def test_Valid_Sides(self):
		assert classify_triangle("A", "b ", "c") == "All three side lengths must be valid floats"
		assert classify_triangle(-1, 1, 1) == "All three side lengths must be greater than zero"
		assert classify_triangle(1, 0, 1) == "All three side lengths must be greater than zero"
		assert classify_triangle(1, 1, 5) == "Triangle has invalid side lengths"

	def test_Equilateral(self):
		assert classify_triangle(2, 2, 2) == "Equilateral"
		assert classify_triangle(5, 5, 5) == "Equilateral"

	def test_Isosceles(self):
		assert classify_triangle(2, 2, 3) == "Isosceles"
		assert classify_triangle(5, 5, 9) == "Isosceles"
		assert classify_triangle(1.0005, 1.0005, 2) == "Isosceles"
		assert classify_triangle(1, 1, sqrt(2)) == "Right and Isosceles"
		assert classify_triangle(1, sqrt(2), 1) == "Right and Isosceles"
		assert classify_triangle(sqrt(2), 1, 1) == "Right and Isosceles"

	def test_Scalene(self):
		assert classify_triangle(2, 3, 4) == "Scalene"
		assert classify_triangle(5, 7, 9) == "Scalene"
		assert classify_triangle(3, 4, 5) == "Right and Scalene"
		assert classify_triangle(5, 4, 3) == "Right and Scalene"
		assert classify_triangle(4, 3, 5) == "Right and Scalene"
		assert classify_triangle(3, 5, 4) == "Right and Scalene"

if __name__ == '__main__':
    unittest.main()