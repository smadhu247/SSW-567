# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(8,15,17),'Right','8,15,17 is a Right triangle')
    
    
    def testEquilateralTriangleA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    def testEquilateralTriangleC(self): 
        self.assertEqual(classify_triangle(12,12,12),'Equilateral','12,12,12 should be equilateral')


    def testIsocelesTriangleA(self): 
        self.assertEqual(classify_triangle(6,6,8),'Isoceles','6,6,8 is a Isoceles triangle')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classify_triangle(4,6,6),'Isoceles','4,6,6 is a Isoceles triangle')

    def testIsocelesTriangleC(self): 
        self.assertEqual(classify_triangle(21,14,14),'Isoceles','21,14,14 is a Isoceles triangle')


    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(4,6,8),'Scalene','4,6,8 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classify_triangle(15,34,32),'Scalene','15,34,32 is a Scalene triangle')

    def testScaleneTriangleC(self): 
        self.assertEqual(classify_triangle(21,14,12),'Scalene','21,14,12 is a Scalene triangle')


    def testNotATriangleTriangleA(self): 
        self.assertEqual(classify_triangle(4,5,10),'NotATriangle','4,5,10 is NotATriangle')

    def testNotATriangleTriangleB(self): 
        self.assertEqual(classify_triangle(4,4,9),'NotATriangle','4,4,8 is NotATriangle')

    def testNotATriangleTriangleC(self): 
        self.assertEqual(classify_triangle(2,2,19),'NotATriangle','21,12,14 is a triangle')


    def testInvalidInputA(self): 
        self.assertEqual(classify_triangle(250,5,10),'InvalidInput','Argument A is greater than 200')

    def testInvalidInputB(self): 
        self.assertEqual(classify_triangle(4,-4,9),'InvalidInput','Argument B is less than 0')

    def testInvalidInputC(self): 
        self.assertEqual(classify_triangle(2,2,"19"),'InvalidInput','Argument C is not of type int')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

