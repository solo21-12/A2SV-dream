class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = "" 
        l,r=0
        while l < len(word1) and r < len(word2):
            new_word += word1[l]
            new_word += word2[r]
            l+=1
            r+= 1
        new_word += word1[l:] + word2[r:]
        return new_word



        