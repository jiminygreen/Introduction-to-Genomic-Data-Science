#!/usr/bin/env python
# -*- coding: utf-8 -*-

#class TestDnaHelper:
def pattern_count(Text, Pattern):
    # fill in your function here
    count = 0
    patternLength = len(Pattern)
    for i in range(0, len(Text) - patternLength+1):
        if Pattern == Text[i: i + patternLength]:
            count += 1
    return count

def frequent_words(Text, k):
    frequent_patterns = dict()
    i = 0
    text_len = len(Text)
    while i < (text_len - k):
        pattern = Text[i: i+k] # the k-mer
        print(pattern)
        if pattern not in frequent_patterns:
            patt_count = pattern_count(Text, pattern)
            frequent_patterns[pattern] = patt_count
        i += 1

    max_freq_value = max(frequent_patterns.values())
    max_freq_array = [p for p, c in frequent_patterns.items() if c == max_freq_value]

    return max_freq_array

def get_last_symbol(pattern):
    return pattern[-1]

def symbol_to_number(symbol):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[symbol]

def number_to_symbol(number):
    return {0:'A', 1:'C', 2:'G', 3:'T'}[number]

def get_prefix(pattern):
    #remove the last charater
    return pattern[0 : -1]

def pattern_to_number(pattern):
    if len(pattern) == 0:
        #recursion is done
        return 0

    last_symbol = get_last_symbol(pattern)
    prefix = get_prefix(pattern)
    result = 4 * pattern_to_number(prefix) + symbol_to_number(last_symbol)
   # print(str(last_symbol) + ' ' + str(result))
    return result

def number_to_pattern(index, k):
    if k == 1: return number_to_symbol(index)

    qr = divmod(index, 4)
    pattern_prefix = number_to_pattern(qr[0], k - 1)
    return pattern_prefix + number_to_symbol(qr[1])


def computing_frequencies(Text, k):
    
    frequencys = [0] * (4**k) # declare an array of zeros
    
    n = len(Text)
    for i in range(0, n - k + 1):
        pattern = Text[i:i+k]
        j = pattern_to_number(pattern)
        frequencys[j] += 1

    return frequencys

# ComputingFrequencies(Text, k)
#         for i ← 0 to 4k − 1
#             FrequencyArray(i) ← 0
#         for i ← 0 to |Text| − k
#             Pattern ← Text(i, k)
#             j ← PatternToNumber(Pattern)
#             FrequencyArray(j) ← FrequencyArray(j) + 1
#         return FrequencyArray

# def finding_frequent_words_by_sorting(Text, k):
#     frequent_patterns = []

#     while i in 

# FindingFrequentWordsBySorting(Text , k)
#         FrequentPatterns ← an empty set
#         for i ← 0 to |Text| − k
#             Pattern ← Text(i, k)
#             Index(i) ← PatternToNumber(Pattern)
#             Count(i) ← 1
#         SortedIndex ← Sort(Index)
#         for i ← 1 to |Text| − k
#             if SortedIndex(i) = SortedIndex(i − 1)
#                 Count(i) = Count(i − 1) + 1
#         maxCount ← maximum value in the array Count
#         for i ← 0 to |Text| − k
#             if Count(i) = maxCount
#                 Pattern ← NumberToPattern(SortedIndex(i), k)
#                 add Pattern to the set FrequentPatterns
#         return FrequentPatterns

# NumberToPattern(index, k)
#     if k = 1
#         return NumberToSymbol(index)
#     prefixIndex ← Quotient(index, 4)
#     r ← Remainder(index, 4)
#     symbol ← NumberToSymbol(r)
#     PrefixPattern ← NumberToPattern(prefixIndex, k − 1)
#     return concatenation of PrefixPattern with symbol

# A 0
# T 3
# G 14
# C 57
# A 228
# A 912

# def PatternToNumber(pattern):
#     if pattern == '': return 0
#     return 4 * PatternToNumber(pattern[0 : - 1]) + {'A': 0, 'C': 1, 'G': 2, 'T': 3}[pattern[-1]]


# def pattern_to_number(pattern):
#     if pattern == '': return 0
#     return 4 * pattern_to_number(pattern[0 : - 1]) + {'A': 0, 'C': 1, 'G': 2, 'T': 3}[pattern[-1]]
# def computing_frequencies(Text, k):
#     frequencys = [0] * (4**k) # declare an array of zeros
#     for i in range(0, len(Text) - k + 1):
#         pattern = Text[i:i+k]
#         j = pattern_to_number(pattern)
#         frequencys[j] += 1
#     return frequencys