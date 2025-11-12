# APPROACH 1
def func1(s):
    words=s.split()
    return " ".join(reversed(words))

n=str(input("Enter string : "))
print(func1(n))

# APPROACH 2
def func2(s):
    n = len(s)
    words = ""
    temp = []
    for i in range(n):
        if s[i] != ' ':  # Assuming space is the delimiter between words
            words += s[i]
        elif words:
            temp.insert(0, words)  # Insert the current word at the beginning of the list
            words = ""  # Reset words to collect the next word
    if len(words) > 0:
        temp.insert(0, words)  # Insert the last word into the list if any
    return " ".join(temp)  # Join the reversed list of words into a string 


from typing import List
class Solution:
    def func(self, s1: str) -> str:
        res=[]
        word=""
        for i in range(len(s1)):
            if s1[i]==" ":
                if word:
                    res.append(word)
                    word=""
            else:
                word+=s1[i]
        if word:
            res.append(word)
        res.reverse()
        return ' '.join(res)

def main():
    s1=Solution()
    string1=str(input("Enter String 1: "))
    print(s1.func(string1))
main()