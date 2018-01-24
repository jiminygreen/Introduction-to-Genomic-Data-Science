#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
#from FrequentWords import TestDnaHelper
import dna_reader

class TestDnaFixture(unittest.TestCase):

    def test_pattern_count_is_true(self):
        #TestDnaHelper.pattern_count(self, 'GCGCG', 'GCG') # Also works
        count = dna_reader.pattern_count('GCGCG', 'GCG')
        self.assertEqual(2, count)
        self.assertEqual(5, dna_reader.pattern_count('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC', 'CGCG'))


    def test_frequent_word_count_correct(self):
        #dna = TestDnaHelper()
        self.assertEqual(['GCAT', 'CATG'], dna_reader.frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))

        print(dna_reader.frequent_words('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3))

    def test_symbol_to_number_returns_correct_value(self):
        
        self.assertEqual(0, dna_reader.symbol_to_number('A'))
        self.assertEqual(1, dna_reader.symbol_to_number('C'))
        self.assertEqual(2, dna_reader.symbol_to_number('G'))
        self.assertEqual(3, dna_reader.symbol_to_number('T'))

    def test_get_last_symbol_returns_correct_result(self):
        self.assertEqual('G', dna_reader.get_last_symbol('ASDFG'))


    def test_get_prefix_removes_everything_except_the_last_character(self):
        self.assertEqual('ASDF', dna_reader.get_prefix('ASDFG'))

    def test_pattern_to_number_returns_correct_output(self):
        self.assertEqual(11, dna_reader.pattern_to_number('AGT'))


    def test_pattern_to_6_kmer_number_returns_correct_output(self):
        self.assertEqual(912, dna_reader.pattern_to_number('ATGCAA'))

#0*4 + 3*4 + 2*4 + 1*4 + 0*4 + 0
# 0 + 12 + 8 + 4 + 0 + 0
# bedmas

    def test_number_to_pattern_is_correct(self):
        self.assertEqual('ATGCAA', dna_reader.number_to_pattern(912, 6))
        self.assertEqual('AGTC', dna_reader.number_to_pattern(45, 4))
        self.assertEqual('CCCATTC', dna_reader.number_to_pattern(5437, 7))
        self.assertEqual('ACCCATTC', dna_reader.number_to_pattern(5437, 8))
        
    def test_computing_frequencies(self):
        self.assertEqual([2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0], 
        dna_reader.computing_frequencies('ACGCGGCTCTGAAA', 2))

if __name__ == '__main__':
    unittest.main()