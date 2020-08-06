# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# Your code here
import re
import string
def crack_caesar(s):
    all_freq = {} 
    most_frequent = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
                     "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z", " "]
    for i in s: # O(n)
        if i.isalpha(): # O(1)
            if i in all_freq: # O(1)
                all_freq[i] += 1 # O(1)
            else: 
                all_freq[i] = 1  # O(1)
    
    sorted_freq = {k: v for (k, v) in sorted(all_freq.items(), key= lambda item: item[1], reverse = True)} #O(n * log n)
    i = 0
    for key in sorted_freq:
        sorted_freq[key] = most_frequent[i] # O(1)
        i += 1 
    s_copy = list(s) #O(n)
    for i in range(len(s_copy)):#O(n)
        if s_copy[i] in sorted_freq: #O(1)
            s_copy[i] = sorted_freq[s_copy[i]] #O(1)
    
    return "".join(s_copy) #O(n)

    

f = open("applications\crack_caesar\ciphertext.txt", 'r')
print(crack_caesar(f.read()))