from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagram("evil", "vile"))       
print(is_anagram("hello", "world"))