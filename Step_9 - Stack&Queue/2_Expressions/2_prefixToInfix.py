def prefixToInfix(s):
    st=[]
    i=len(s)-1
    while i>-1:
        if s[i].isalnum():
            st.append(s[i])
        else:
            el1=st.pop()
            el2=st.pop()
            result=(f"({el1}{s[i]}{el2})")
            st.append(result)
        i-=1
    return st[-1]  