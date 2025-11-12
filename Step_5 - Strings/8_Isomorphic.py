# CLEVER ONE-LINER APPROACH USING SET AND ZIP -
def func(s,t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# HASHING 2 DICT -
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False  # Different lengths can't be isomorphic

    s_to_t = {}
    t_to_s = {}

    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2:
            return False  # Conflict in mapping s → t
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False  # Conflict in mapping t → s

        s_to_t[c1] = c2
        t_to_s[c2] = c1

    return True


# EZ-
def func(s1,s2):
    if len(s1)!=len(s2):
        return False
    hashmap={}
    for i in range(len(s1)):
        if s1[i] in hashmap and hashmap[s1[i]]!=s2[i]:
            return False
        if s2[i] in hashmap and hashmap[s2[i]]!=s1[i]:
            return False
        hashmap[s1[i]]=s2[i]
        hashmap[s2[i]]=s1[i]
    return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_t={}
        t_s={}
        for i in range(len(s)):
            if s[i] in s_t:
                if s_t[s[i]]!=t[i]:
                    return False
            if t[i] in t_s:
                if t_s[t[i]]!=s[i]:
                    return False
            if s[i] not in s_t:
                s_t[s[i]]=t[i]
            if t[i] not in t_s:
                t_s[t[i]]=s[i]
        return True        


