def func1(s):
    reversedStr=""
    for i in range(len(s)-1,-1,-1):
        reversedStr+=s[i]
    return reversedStr
