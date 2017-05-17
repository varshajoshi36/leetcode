"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

def groupAnagramsUsingPrime(strs):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    product_dict = {}
    for word in strs:
        prime_product = 1
        for letter in word:
            prime_product *= prime[ord(letter) - ord('a')]
        if prime_product in product_dict.keys():
            product_dict[prime_product] += [word]
        else:
            product_dict[prime_product] = [word]

    return product_dict.values()

def groupAnagrams(strs):
    sorted_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in sorted_dict.keys():
            sorted_dict[sorted_word] += [word]
        else:
            sorted_dict[sorted_word] = [word]

    return sorted_dict.values()

def main():
    print groupAnagrams(map(str.strip, raw_input().split(',')))

if __name__ == '__main__':
    main()
