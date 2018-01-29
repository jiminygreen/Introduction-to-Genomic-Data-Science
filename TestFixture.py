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
        self.assertEqual(['GCAT', 'CATG'], dna_reader.frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))

        #print(dna_reader.frequent_words('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3))

        #print(dna_reader.frequent_words('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5))

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


    def test_number_to_pattern_is_correct(self):
        self.assertEqual('ATGCAA', dna_reader.number_to_pattern(912, 6))
        self.assertEqual('AGTC', dna_reader.number_to_pattern(45, 4))
        self.assertEqual('CCCATTC', dna_reader.number_to_pattern(5437, 7))
        self.assertEqual('ACCCATTC', dna_reader.number_to_pattern(5437, 8))


    def test_computing_frequencies(self):
        self.assertEqual([2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0], 
        dna_reader.computing_frequencies('ACGCGGCTCTGAAA', 2))

        # print(dna_reader.computing_frequencies('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGA', 5))
        # print(dna_reader.pattern_matching('CGACA', 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGA'))
        # print(dna_reader.pattern_count('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGA','CGACA'))
        


    def test_reverse_complement(self):
        self.assertEqual('ACCGGGTTTT', dna_reader.reverse_complement('AAAACCCGGT') )


    def test_pattern_matching(self):
        self.assertEqual([1, 3, 9], dna_reader.pattern_matching('ATAT', 'GATATATGCATATACTT'))
        print(dna_reader.pattern_matching('CGC', 'ATGACTTCGCTGTTACGCGC')) 


    def test_clump_finding(self):
        self.assertEqual(['CGACA', 'GAAGA'], dna_reader.clump_finding(
            'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4))
            #CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGA
    # def test_pattern_matching_large_data_set(self):
    #     f = open("./Vibrio_cholerae.txt", 'r')
    #     genome = f.read()
    #     f.close()
    #     print(dna_reader.pattern_matching('CTTGATCAT', genome))
    #     print(dna_reader.pattern_matching('ATGATCAAG', genome)) # the reverce compliment
# [60039, 98409, 129189, 152283, 152354, 152411, 163207, 197028, 200160, 357976, 376771, 392723, 532935, 600085, 622755, 1065555]
# [116556, 149355, 151913, 152013, 152394, 186189, 194276, 200076, 224527, 307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368]        

        # print(dna_reader.computing_frequencies(genome, 9).count()) # not working. looks to be a bad charater not handled in symbol_to_number(...)

    def test_clump_with_e_coli(self):
        print('reading file...')
        f = open("./E_coli_genome.txt", 'r')
        genome = f.read()
        f.close()
        print('file read')
        
        print('finding clumps...')
        #clumps = dna_reader.clump_finding(genome, 9, 500, 3) #1904
        clumps = dna_reader.clump_finding(genome, 9, 500, 4) #588
        
        print(len(clumps))
        print(len(set(clumps)))


if __name__ == '__main__':
    unittest.main()