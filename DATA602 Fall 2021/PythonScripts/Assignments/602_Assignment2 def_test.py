#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 06:26:46 2021

@author: Audiorunner13
"""

'''
Assignment #2
1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not 
    guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 07_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables unless stated to do so
7. Make sure your work is committed to your master branch in Github
Installation requirements:
1. Please install numpy: pip install numpy
'''
import math
import unittest
import numpy as np
import requests as r
import copy

def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. 
    # For example exercise05(5) will return 120. No Python functions are to be used.

    # ------ Place code below here \/ \/ \/ ------

    # pass # Remove this line
    
    if n == 0:
        return 1
    
    # print(n)
        
    return n * exercise05(n-1)

class TestAssignment2(unittest.TestCase):
    
    def test_exercise05(self):
        print('Testing exercise 5')
        self.assertEqual(exercise05(5), 120)
        self.assertEqual(exercise05(10), 3628800)

if __name__ == '__main__':
    unittest.main()