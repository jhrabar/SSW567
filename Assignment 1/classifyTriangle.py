# John Hrabar
# Assignment 1
# I Pledge My Honor That I Have Abided By The Stevens Honor System
# This program accepts three inputs from the user where the inputs 
# are the side lengths of a triangle, and returns the classification of the triangle.

from math import isclose

def determine_triangle_type(a, b, c):
	if(isclose(a,b) and isclose(b,c)):
		return "Equilateral"
	elif (isclose(a * a + b * b, c * c) or isclose(a*a + c*c, b * b) or isclose( b * b + c * c, a * a)):
		if( isclose(a, b) or isclose(a,c) or isclose(b, c)):
			return "Right and Isosceles"
		else:
			return "Right and Scalene"
	else:
		if( isclose(a,b) or isclose(a,c) or isclose(b,c)):
			return "Isosceles"
		else:
			return "Scalene"

def classify_triangle(a, b, c):
	try:
		aNum = float(a)
		bNum = float(b)
		cNum = float(c)
	except:
		return "All three side lengths must be valid floats"
	if(aNum <= 0 or bNum <= 0 or cNum <= 0):
		return "All three side lengths must be greater than zero"
	elif (aNum + bNum > cNum and aNum + cNum > bNum and bNum + cNum > aNum):
		return determine_triangle_type(aNum, bNum, cNum)
	else:
		return "Triangle has invalid side lengths"

def main():
	print(classify_triangle(2, 2, 3.3))

main()
