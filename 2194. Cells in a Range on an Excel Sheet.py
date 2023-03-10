class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1=ord(s[0])
        row1=ord(s[1])
        col2=ord(s[3])
        row2=ord(s[4])
        ans=[]
        while col1<=col2:
            row=row1
            col=chr(col1)
            while row<=row2:
                ans.append(col+chr(row))
                row+=1
            col1+=1
        return ans
