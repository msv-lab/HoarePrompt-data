#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

for line in stdin:
    number, weight, height = line.split(',')
    if 25.0 <= float(weight) / (float(height) ** 2):
        print(number)