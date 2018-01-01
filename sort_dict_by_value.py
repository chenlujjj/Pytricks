#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = {'a': 1, 'b': 3, 'c': 2, 'd': 4}

print x.items()
print sorted(x.items())

# Method 1
print sorted(x.items(), key=lambda y: y[1])
print sorted(x.items(), key=lambda y: y[1], reverse=True)  # 降序

# Method 2
import operator
print sorted(x.items(), key=operator.itemgetter(1))
