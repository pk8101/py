#balance parenthesis problem
def isBalance(string):
    s=[]
    for char in string:
        if char in '({[':
            s.append(char)
        elif char in ')':
            if not s or s[-1]!='(':
                return False
            s.pop()

        elif char in '}':
            if not s or s[-1]!='{':
                return False
            s.pop()

        elif char in ']':
            if not s or s[-1]!='[':
                return False
            s.pop()
    if not s:
        return True
    return False

stri=input()
ans=isBalance(stri)
print(ans)