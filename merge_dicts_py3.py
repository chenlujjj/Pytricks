#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# note: only work for python 3.5+

x = {'name': 'clx', 'age': 23}
y = {'name': 'lxchen', 'gender': 'male'}

# Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.
z1 = {**x, **y}
print(z1)

z2 = {**y, **x}
print(z2)

# 这个方法同样适用于三个及以上的字典合并
w = {'name': 'chenlx', 'company': 'yitu'}
z3 = {**x, **y, **w}
print(z3)
