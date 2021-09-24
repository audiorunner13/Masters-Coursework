#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:13:38 2021

@author: Audiorunner13
"""
import math
import unittest
import numpy as np
import requests as r

def histogram(s):
    d = dict()

    for c in s:
        print(c)
#        print(d[c])

        if c not in d:
            d[c] = 1
            print(d)            
        else:         
            d[c] += 1
            print(d)
            
    return d

h = histogram('brontosaurus')

print(h)


