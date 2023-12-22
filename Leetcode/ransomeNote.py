class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        magazine_chr = list(magazine)
        for i in ransomNote:
            if i not in magazine_chr:
                return False
            magazine_chr.remove(i)

        return True