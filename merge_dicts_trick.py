#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = {'name': 'clx', 'age': 23}
y = {'name': 'lxchen', 'gender': 'male'}

# Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.
z1 = dict(x, **y)
print z1

z2 = dict(y, **x)
print z2
