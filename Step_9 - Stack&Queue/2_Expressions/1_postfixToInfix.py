def postfixToInfix(s):
    st=[]
    i=0
    while i<len(s):
        if s[i].isalnum():
            st.append(s[i])
        else:
            el2=st.pop()
            el1=st.pop()
            result=(f"({el1}{s[i]}{el2})")
            st.append(result)
        i+=1
    return st[-1] 