# Problem: Find the K-th Character in String Game I
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k :
            m = len(word)
            for i in range(m):
                if word[i] == 'z' :
                    word+= 'a'
                word += chr(ord(word[i])+1)
        return word[k-1]

        