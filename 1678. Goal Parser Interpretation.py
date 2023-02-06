class Solution:
    def interpret(self, command: str) -> str:
        res=[]
        for i in range(len(command)-1):
            if command[i]=='(' and command[i+1]==')':
                res.append('o')
            elif command[i]=='(' and command[i+1]=='a':
                res.append('al')
            elif command[i]=='G' :
                res.append('G')
        if command[len(command)-1]=='G':
            res.append('G')
        return ''.join(res)
