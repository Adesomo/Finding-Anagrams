# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    if sorted(word) == sorted(anagram): 
        return True
       
    else:
        return False
    #return True
print(find_anagram('silent','listen'))
print(find_anagram('elle','belle'))
print(find_anagram('elbow','Below'))
print(find_anagram('rebel','beret'))
