class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(' ')
        new_words=['']*len(words)

        for word in words:
            index=ord(word[-1])-49
            new_words[index]=word[:-1]
        return ' '.join(new_words)
