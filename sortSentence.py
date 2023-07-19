class Solution:
    def sortSentence(self, s: str) -> str:
        string_arr = s.split()
        ans = [''] * (len(string_arr) + 1)
        for i in string_arr:
            index = int(i[-1])
            ans[index] = i[:-1]

        sentence = ' '.join(ans)
        sentence = sentence.replace(' ', '', 1)

        return sentence
