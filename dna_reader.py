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

def frequent_words(Text, k, t = 1):
    frequent_patterns = dict()
    search_len = len(Text) - k
    for i in range(0, search_len):
        pattern = Text[i: i+k] # the k-mer
        if pattern not in frequent_patterns:
            patt_count = pattern_count(Text, pattern)
            frequent_patterns[pattern] = patt_count

    max_freq_value = max(frequent_patterns.values())
    print('max freq: ' + str(max_freq_value))
    max_freq_array = [p for p, c in frequent_patterns.items() if c == max_freq_value and c >= t]

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

def reverse_complement(Pattern):
    result = ''
    for n in Pattern:
        if n == 'A': result += 'T'
        elif n == 'T': result += 'A'
        elif n == 'C': result += 'G'
        elif n == 'G': result += 'C'

    return result[::-1]


def pattern_matching(Pattern, Genome):
    pos_record = []
    patternLength = len(Pattern)
    search_len = len(Genome) - patternLength+1 

    for i in range(0, search_len):
        if Pattern == Genome[i: i + patternLength]:
            pos_record.append(i)

    return pos_record

def clump_finding(genome, k, L, t):
    #print(len(genome))
    clump = [0] * (4**k) # declare an array of zeros

    text = genome[0: L]
    print(text)
    frequency_array = computing_frequencies(text, k)
    print('freq array')
    print(frequency_array)
    for i in range(0, len(frequency_array)):
        if frequency_array[i] >= t: clump[i] = 1

    for i in range(1, len(genome) - L):
        first_pattern = genome[i - 1: k]
        index = pattern_to_number(first_pattern)
        frequency_array[index] -= 1

        last_pattern = genome[i + L - k: k]
        index = pattern_to_number(last_pattern)
        frequency_array[index] += 1

        print('freq for: ' + str(i))
        print(frequency_array)

        if frequency_array[index] >= t:
            clump[index] = 1

    print(clump)

    frequency_patterns = []
    for i in range(0, 4 * k - 1):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequency_patterns.append(pattern)

    return frequency_patterns

    # BetterClumpFinding(Genome, k, t, L)
    #     FrequentPatterns ← an empty set
    #     for i ← 0 to 4k − 1
    #         Clump(i) ← 0
    #     Text ← Genome(0, L)
    #     FrequencyArray ← ComputingFrequencies(Text, k)
    #     for i ← 0 to 4k − 1
    #         if FrequencyArray(i) ≥ t
    #             Clump(i) ← 1
    #     for i ← 1 to |Genome| − L
    #         FirstPattern ← Genome(i − 1, k)
    #         index ← PatternToNumber(FirstPattern)
    #         FrequencyArray(index) ← FrequencyArray(index) − 1
    #         LastPattern ← Genome(i + L − k, k)
    #         index ← PatternToNumber(LastPattern)
    #         FrequencyArray(index) ← FrequencyArray(index) + 1
    #         if FrequencyArray(index) ≥ t
    #             Clump(index) ← 1
    #     for i ← 0 to 4k − 1
    #         if Clump(i) = 1
    #             Pattern ← NumberToPattern(i, k)
    #             add Pattern to the set FrequentPatterns
    #     return FrequentPatterns