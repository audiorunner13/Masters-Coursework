#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 05:52:48 2021

@author: Audiorunner13
"""

# cars = ["Honda","Toyota","Mitsubishi",'Tesla']

# print(cars[0])

# print(cars[0:2])  # 1st index is inclusive, 2nd is exclusive

# cars.append('Lamboghini')

# print(cars[0:3])

# print(cars[:3])

# print(cars[0:])

# print(cars[2:])

# cars.append('Bugati')

# print(cars[2:])

# cars.append('Jeep')

# cars[2] = 'Volkswagen'

# del cars[0]

# cars.append('Honda')

# cars.remove('Tesla')

# cars.clear()

# cars.reverse()

# print(cars)

# cars.sort()

# cars.reverse()

# cars.insert(1,'Ford')

# more_cars = ['GM', 'Fiat']

# cars.extend(more_cars)

# cars.sort()

# print(cars)

# print(len(cars))

# prices = [3,7,9,11,2,1]

# print(max(prices))
# print(min(prices))
# print(sum(prices))

# for c in cars:
#     print(c)

# if('Bugati' in cars):
#     print('yes it is')

#numbers = [1,2,3]
# numbers = [[1,2,3],[4,5,6],[10,12,14]]

# print(numbers[0])
# print(numbers[0][1])
# print(numbers[0][2])
# print(numbers[2][2])

listOfStuff = [1,'Hello',3.14159,'Bye']
print(listOfStuff)

for i in listOfStuff:
    print(i)

# DICTIONARIES

grades = {'Sally':99, 'Greg':99, 'George':58}

# print(grades['George'])

# del grades['George']

# print(grades)

for k,v in grades.items():
    print(v)

# TUPLES

cars = ('Hyundai','GM', 'Ford', 'Porsche')  # Can't use insert or removed because tuples are immutable
print(cars)
print(cars[0])

for c in cars:
    print(c)

print(len(cars))