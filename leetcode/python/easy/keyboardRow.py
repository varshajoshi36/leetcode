"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
"""

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    keyboard_rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    
    single_row_words = []
    for row in keyboard_rows:
        single_row_words += [word for word in words if len(set(list(word.upper())) - set(list(row))) == 0]

    return single_row_words

words = ["Hello", "Alaska", "Dad", "Peace"]
print findWords(words)
