class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters=['*']*26
        letter=97

        id=0
        while id!=len(key) and letter!=123:
            if key[id]==' ':
                id+=1
                continue
            idx=ord(key[id])-97
            id+=1
            if letters[idx]=="*":
                letters[idx]=chr(letter)
                letter+=1
        answer=''
        for i in range(len(message)):
            if message[i]==' ':answer+=message[i]
            else:answer+=letters[ord(message[i])-97]
        return answer
