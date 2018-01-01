#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than defining a class manually
# And it is self-documented

from collections import namedtuple

iCar = namedtuple('Car', 'color brand mileage')

my_car = iCar('red', 'BMW', 5000)

# Access value by name
print my_car.color, my_car.brand, my_car.mileage

# Access value by index
print my_car[0], my_car[1], my_car[2]

# use getattr() to access value
print getattr(my_car, 'color')

print my_car.__doc__
print my_car

# Like tuples, named tuples are immutable(can't be changed in-place in memory)
try:
    my_car.color = 'green'
except AttributeError as e:
    print e

# 如果需要mutable的namedtuple，试试recordclass

# as namedtuple instances do not have per-instance dictionaries,
# namedtuple比字典占用内存少，速度更快

# 类型转换
# namedtuple ==> dictionary
my_car_dict = my_car._asdict()
print my_car_dict

# list ==> namedtuple
li = ['black', 'VW', 2000]
print iCar._make(li)

# dictionary ==> namedtuple
di = {'color': 'white', 'brand': 'KIA', 'mileage': 3500}
print iCar(**di)

# Use _fields to display all keynames of a nametuple
print 'All the fields of a car are: {}'.format(iCar._fields)

# Use _replace to change the attribute values of namedtuple
another_car = my_car._replace(color='blue')
print 'The modified namedtuple is: {}'.format(another_car)
