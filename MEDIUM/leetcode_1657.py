# 1657. Determine if Two Strings Are Close
# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



# Solution -
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if length of both words is not equal then return False immediately
        if len(word1) != len(word2):
            return False
        
        # Count freqency of letters in both words
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # If both word have same set of letters AND
        # frequency of letters are same irrespective of letter
        # then it will alwasy possible to convert word1 to word2
        return set(word1) == set(word2) and sorted(list(counter1.values())) == sorted(list(counter2.values()))




        
