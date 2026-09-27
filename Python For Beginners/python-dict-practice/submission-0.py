from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    #key is char (individual letters in a word)
    # value is the count - int amount of times a char in words

    count= {}
    for char in word:
        if char not in count:
            count[char] = 0
        
        count[char] += 1
    return count
        
    
        







# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
