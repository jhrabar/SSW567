# John Hrabar
# Assignment 1
# I Pledge My Honor That I Have Abided By The Stevens Honor System
""" This program accepts three inputs from the user where the inputs
 are the side lengths of a triangle, and returns the classification of the triangle."""

from math import isclose

def determine_triangle_type(s_1, s_2, s_3):
    '''Return the triangle classification.'''
    if(isclose(s_1, s_2) and isclose(s_2, s_3)):
        return "Equilateral"
    if(isclose(s_1*s_1+s_2*s_2, s_3*s_3)
       or isclose(s_1*s_1+s_3*s_3, s_2*s_2)
       or isclose(s_2*s_2+s_3*s_3, s_1*s_1)):
        if(isclose(s_1, s_2) or isclose(s_1, s_3) or isclose(s_2, s_3)):
            return "Right and Isosceles"
        return "Right and Scalene"
    if(isclose(s_1, s_2) or isclose(s_1, s_3) or isclose(s_2, s_3)):
        return "Isosceles"
    return "Scalene"

def classify_triangle(s_1, s_2, s_3):
    '''Gather side lengths from user and return triangle classification.'''
    try:
        s_1_num = float(s_1)
        s_2_num = float(s_2)
        s_3_num = float(s_3)
    except ValueError:
        return "All three side lengths must be valid floats"
    if(s_1_num <= 0 or s_2_num <= 0 or s_3_num <= 0):
        return "All three side lengths must be greater than zero"
    if (s_1_num+s_2_num > s_3_num and s_1_num+s_3_num > s_2_num and s_2_num+s_3_num > s_1_num):
        return determine_triangle_type(s_1_num, s_2_num, s_3_num)
    return "Triangle has invalid side lengths"

def main():
    '''Call classify_triangle'''
    print(classify_triangle(2, 2, 3.3))

main()
