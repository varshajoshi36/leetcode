"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    caps_range = range(65, 91)
    word_ord = [ord(x) for x in word]

    caps_indices = [word_ord.index(x) for x in word_ord if x in caps_range]

    if len(caps_indices) != len(word) and len(caps_indices) != 1  and len(caps_indices) != 0:
        return False

    if len(caps_indices) == 1 and caps_indices[0] != 0:
        return False

    return True

word = 'U'
print detectCapitalUse(word)
