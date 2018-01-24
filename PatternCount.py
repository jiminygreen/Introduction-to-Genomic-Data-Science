#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestDnaFixture(unittest.TestCase):
    
    def PatternCount(self, Text, Pattern):
        # fill in your function here
        count = 0
        i = 0
        patternLength = len(Pattern)
        while i < len(Text) - (patternLength-1):
            testPattern = Text[i: i + patternLength]
            if testPattern == Pattern:
                count +=1
            i += 1
        return count